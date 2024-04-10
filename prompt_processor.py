# This will replace __token__ recursively with a value from wildcard/token.txt. spaces working, added missing error message 
# https://gist.github.com/h-a-te/30f4a51afff2564b0cfbdf1e490e9187

import math
import os
import sys
import traceback
import random
import re
from random import choices


import modules.scripts as scripts
import modules.images as images
import gradio as gr

from modules.processing import Processed, process_images
from PIL import Image
from modules.shared import opts, cmd_opts, state
from modules.styles import StyleDatabase



class Script(scripts.Script):
    def title(self):
        return "Wildcards recursive"

    def ui(self, is_img2img):
        same_seed = gr.Checkbox(label='Use same seed for each image', value=False)

        return [same_seed]

    re_combinations = re.compile(r"\{([^{}]*)}")
    invalid_wildcards = []

    def replace_combinations(self, match):
        if match is None or len(match.groups()) == 0:
            return ""

        variants = [s.strip() for s in match.groups()[0].split("|")]
        weights = []
        for i, variant in enumerate(variants):
            first = variant.split("%")
            if len(first) == 2:
                num, first_variant = first
                variants[i] = first_variant
                try:
                    weights.append(int(num))
                except ValueError:
                    weights.append(0)
            else:
                weights.append(0)
        summed = sum(weights)
        zero_weights = weights.count(0)
        weights = list(map(lambda x: (100 - summed) / zero_weights if x == 0 else x, weights))

        try:
            picked = choices(variants, weights)[0]
            return picked
        except ValueError as e:
            return ""

        return ""

    def replace_wildcard(self, chunk):
        file_dir = os.path.dirname("E:\\AI TESTS\\stable-diffuse\\")
        replacement_file = os.path.join(file_dir, f"scripts\\wildcards\\{chunk}.txt")
        if os.path.exists(replacement_file):
            with open(replacement_file, encoding="utf8") as f:
                return random.choice(f.read().splitlines())
        print(f'could not find chunk: {chunk}')
        self.invalid_wildcards.append(chunk)
        return chunk

    def replace_wildcard_recursive(self, prompt):
        p = prompt
        matches = re.findall('__.*?__', p)
        if matches:
            for match in matches:
                p = p.replace(match, self.replace_wildcard(match.replace("__", "")))
            if p != prompt:
                return self.replace_wildcard_recursive(p)

        return p

    def pick_variant(self, template):
        if template is None:
            return None

        return self.re_combinations.sub(self.replace_combinations, template)

    def generate_prompt(self, template):
        while template != self.pick_variant(self.replace_wildcard_recursive(template)):
            template = self.pick_variant(self.replace_wildcard_recursive(template));

        return template


    def run(self, p, same_seed):
        file_dir = os.path.dirname(os.path.realpath("__file__"))
        style_file = os.path.join(file_dir, "styles.csv")
        styledb = StyleDatabase(style_file)
        styledb.apply_styles(p)
        p.styles = ['None', 'None']

        original_prompt = p.prompt[0] if type(p.prompt) == list else p.prompt
        all_prompts = [self.generate_prompt(original_prompt) for _ in range(p.batch_size * p.n_iter)]

        # TODO: Pregenerate seeds to prevent overlaps when batch_size is > 1
        # Known issue: Clicking "recycle seed" on an image in a batch_size > 1 may not get the correct seed.
        # (unclear if this is an issue with this script or not, but pregenerating would prevent). However,
        # filename and exif data on individual images match correct seeds (testable via sending png info to txt2img).
        all_seeds = []
        infotexts = []

        initial_seed = None
        initial_info = None

        print(f"Will process {p.batch_size * p.n_iter} images in {p.n_iter} batches.")

        state.job_count = p.n_iter
        p.n_iter = 1

        original_do_not_save_grid = p.do_not_save_grid

        p.do_not_save_grid = True

        output_images = []

        print('Invalid wildcards that were found ', self.invalid_wildcards)
        for batch_no in range(state.job_count):
            state.job = f"{batch_no+1} out of {state.job_count}"
            p.prompt = all_prompts[batch_no*p.batch_size:(batch_no+1)*p.batch_size]
            if cmd_opts.enable_console_prompts:
                print(f"wildcards.py: {p.prompt}")
            proc = process_images(p)
            output_images += proc.images
            # TODO: Also add wildcard data to exif of individual images, currently only appear on the saved grid.
            infotext = ""
            if len(self.invalid_wildcards) > 0:
                invalid_cards = ",".join(list(set(self.invalid_wildcards)))
                infotext += f"Invalid wildCards: {invalid_cards} \n"
                self.invalid_wildcards = []

            infotext += "Wildcard prompt: "+original_prompt+"\nExample: "+proc.info
            all_seeds.append(proc.seed)
            infotexts.append(infotext)
            if initial_seed is None:
                initial_info = infotext
                initial_seed = proc.seed
            if not same_seed:
                p.seed = proc.seed

        p.do_not_save_grid = original_do_not_save_grid

        unwanted_grid_because_of_img_count = len(output_images) < 2 and opts.grid_only_if_multiple
        if (opts.return_grid or opts.grid_save) and not p.do_not_save_grid and not unwanted_grid_because_of_img_count:
            grid = images.image_grid(output_images, p.batch_size)

            if opts.return_grid:
                infotexts.insert(0, initial_info)
                all_seeds.insert(0, initial_seed)
                output_images.insert(0, grid)

            if opts.grid_save:
                images.save_image(grid, p.outpath_grids, "grid", all_seeds[0], original_prompt, opts.grid_format, info=initial_info, short_filename=not opts.grid_extended_filename, p=p, grid=True)

        return Processed(p, output_images, initial_seed, initial_info, all_prompts=all_prompts, all_seeds=all_seeds, infotexts=infotexts, index_of_first_image=0)