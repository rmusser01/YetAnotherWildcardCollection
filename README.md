# Stable Diffusion WildCard Prompt Catalogue

------------------------------------------------------------------------------------------------------------
## Table of Contents
- [101/What is this?](#101)
- [Stable Diffusion 101](#sd101)
- [Writing Prompts](#writeprompt)
- [Prompt samples/Bases](#promptsamples)
------------------------------------------------------------------------------------------------------------
(Forked from LulzRose's) YetAnotherWildcardCollection

[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](https://opensource.org/licenses/unlicense)



## TODO

- [ ] Improve naming schema
- [X] Add content from: https://github.com/adieyal/sd-dynamic-prompts/tree/main/collections/nsp
- [X] Add content from: https://github.com/adieyal/sd-dynamic-prompts/tree/main/collections/parrotzone
- [X] Add content from:	https://github.com/adieyal/sd-dynamic-prompts/tree/main/collections/devilkkw
- [ ] Add content from: https://github.com/adieyal/sd-dynamic-prompts/tree/main/collections/jumbo
- [ ] Add content from: https://github.com/Lopyter/sd-artists-wildcards
- [ ] Add content from: https://github.com/Lopyter/stable-soup-prompts/tree/main/wildcards
- [ ] Add content from: https://github.com/jtkelm2/stable-diffusion-webui-1/tree/master/scripts/wildcards
- [ ] Add content from: https://rentry.org/NAIwildcards
- [ ] Add content from: https://github.com/jtkelm2/stable-diffusion-webui-1/tree/main/scripts/wildcards
- [ ] Add content from: https://github.com/Vetchems/sd-danbooru-tags
- [ ] Add content from wildcard zips
- [ ] Add content from links

For items in catalogues that were NSFW, here is a list of URLs containing individual files that were not added:
	* Deleted fetishes folder
	* https://github.com/adieyal/sd-dynamic-prompts/tree/main/collections/devilkkw/pose
	* https://github.com/adieyal/sd-dynamic-prompts/tree/main/collections/devilkkw/body-1
	* https://github.com/adieyal/sd-dynamic-prompts/tree/main/collections/devilkkw/body-2



https://github.com/AUTOMATIC1111/stable-diffusion-webui-wildcards
Text Files

    faces https://rentry.org/pu8z5
    focus https://rentry.org/rc3dp
    poses https://rentry.org/hkuuk
    times https://rentry.org/izc4u
    views https://rentry.org/pv72o
    Clothing: https://pastebin.com/EyghiB2F
    316 colors list: https://pastebin.com/s4tqKB8r
    82 colors list: https://pastebin.com/kiSEViGA
    Backgrounds: https://pastebin.com/FCybuqYW
    More clothing: https://pastebin.com/DrkG1MRw
    Styles: https://pastebin.com/71HTfsML
    Word list (small): https://cdn.lewd.host/EtbKpD8C.zip
    Emotions/expressions: https://pastebin.com/VVnH2b83
    Clothing: https://pastebin.com/cXxN1fJw
    Locations: https://pastebin.com/R6ugwd2m
    Clothing/outfits: https://pastebin.com/Xhhnyfvj
    Locations: https://pastebin.com/uyDJMnvC
    Clothes: https://pastebin.com/HaL3rW3j
    Color (has nouns): https://pastebin.com/GTAaLLnm
    Artists: https://pastebin.com/1HpNRRJU
    Animals: https://pastebin.com/aM4PJ2YY
    Food: https://pastebin.com/taFkYwt9
    Characters: https://files.catbox.moe/xe9qj7.txt
    Backgrounds: https://pastebin.com/gVue2q8g
    Outfits: https://files.catbox.moe/y75qda.txt
    Settings + Minerals: https://pastebin.com/9iznuYvQ
    Hairstyles: https://pastebin.com/X39Kzxh7
    Hairstyles 2: https://pastebin.com/bRWu1Xvv
    Outfits: https://pastebin.com/Z9aHVpEy
    Clothes: https://pastebin.com/4a0BscGr
    Angles: https://pastebin.com/T8w8HEED

---------------------------------------------------------------------------------------------------------
### <a name="101"></a> 101/What is this?
* This is a compilation of more than a dozen wildcard collections pruned for any errors and duplicates and organized for ease of use. This fork is focused on non-NSFW entries. All NSFW entries I've come across while compiling this have been dumped into the NSFW folder. It's unsorted. My goal was to consolidate all the wildcard dumps I could find, but dind't want to necessarily throw some away because I personally don't want them, so instead they just go into the NSFW folder.
- **101**
	* This is a repo/guide whose purpose is to help facilitate and improve the process of generating images using wildcards.
	* Split into a few folders, the 
		* `Combined-structure` does have NSFW tags. I don't believe anything crazy is in there, but this folder was a straight copy/paste for content that didn't already exist.
		* `NSFW_dump` - self explanatory, dump of all NSFW wildcard collections I came across that weren't weirder than usual.
		* `Unreviewed_prompts` - again, as the name implies. These are prompts I came across that I didn't review or skimmed and figured I should throw them in there anyways. No intention of sorting/catalogueing.
		* `Wildcard_Dumps` - These are wildcard zip files I came across and merged (most) into the `Combined-structure` folder.
			* Have kept these for anyone else interested in the source materials.
		- `Booru-only` - Folder matching tag structure of Danbooru.
			* 99% clean of NSFW tags, might be a few in there but is meant to be non-nsfw (so you can add your own if you wish).
				* Original idea was to try and map out the non-nsfw space of PonyXL, and then well, here we are.
			* Also 96% of all tags.
			- Booru Prompts tag categories not included:
				- symbols
					* Symbols from the real world
					* Symbols of specific series/mangas/games/etc.
				- Body :
					* face -> Sexual
					* Upper Torso -> Breasts
					* Lower Toros -> All of them.
					* Anything involving genitals
				- Attire and body accessories
					* Sexual attire
					* Nudity
				- Sex
				- Objects:
					* Piercings -> Genital piercings
					* Sex objects
				- Booru tags not sorted fully:(and likely wont be)
					* https://danbooru.donmai.us/wiki_pages/list_of_ships
					* https://danbooru.donmai.us/wiki_pages/list_of_ground_vehicles
- **Links**
	* `stable-diffusion-webui-wildcards` extension: https://github.com/AUTOMATIC1111/stable-diffusion-webui-wildcards
	- **List of Wildcard Catalogs**
		* List of: https://github.com/adieyal/sd-dynamic-prompts?tab=readme-ov-file#collections
		* https://github.com/Vetchems/sd-danbooru-tags
		* https://github.com/aoirusann/my-sd-wildcard
		* https://github.com/LulzRose/YetAnotherWildcardCollection
		* https://github.com/adieyal/sd-dynamic-prompts/tree/main/collections/jumbo
		* https://rentry.org/NAIwildcards
		* https://github.com/adieyal/sd-dynamic-prompts/tree/main/collections/nsp
		* https://github.com/adieyal/sd-dynamic-prompts/tree/main/collections/devilkkw
		* https://github.com/mattjaybe/sd-wildcards
---------------------------------------------------------------------------------------------------------




---------------------------------------------------------------------------------------------------------
### Stable Diffusion 101<a name="sd101"></a>
- **Manual**
	* https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Features
	- CFG Scale
		* https://getimg.ai/guides/interactive-guide-to-stable-diffusion-guidance-scale-parameter
	- CLIP
		* https://github.com/pharmapsychotic/clip-interrogator/tree/main
- **Steps**
	1. Define your vision - what will the finished product be?
	2. Decide the art style
	3. Describe the subject
	4. Define compositional elements
	5. Reference existing works.
	6. Specify Techniques
	7. Experiment
	8. Refine and iterate
- **Generation Process**
	* https://github.com/adieyal/sd-dynamic-prompts/blob/main/docs/tutorial.md
	* https://github.com/adieyal/sd-dynamic-prompts/blob/main/docs/SYNTAX.md

---------------------------------------------------------------------------------------------------------




---------------------------------------------------------------------------------------------------------
### <a name="writeprompt"></a>Writing Prompts
- **Sample Structure**
	- `[image content/subject, description of action, state, and mood] / B.[art form, style, and artist references] / C.[additional settings, such as lighting, colors, and framing]`
 		* `[image content/subject]` - The choice of image content or subject defines what the image is about. It provides the primary focus and narrative of the visual. Whether it's a natural landscape, a person, an object, or an abstract concept, the subject sets the stage for the viewer's understanding and emotional response. 
 		* `description of action` - The action in an image represents what's happening within the visual. Action can range from dynamic and energetic movements to static and contemplative scenes. It adds life and depth to the image, influencing the viewer's perception of the moment captured. 
		* `state` - The state of objects, people, or elements in an image conveys their condition or position. States can be descriptive in terms of physical attributes or emotional states. 
		* `art form` - Different art forms, such as illustration, painting, photography, or graphic design, provide a framework for conveying ideas and emotions. When choosing an art form for image prompts, it sets the medium through which the message or concept will be visualized.
 		* `style` - Artistic style encompasses the unique visual language of an artist or a genre. It plays a crucial role in conveying the mood, tone, and atmosphere of an image. 
		* `artist` - Referencing specific artists or their works can provide a rich source of inspiration and context. Artists often have signature techniques, themes, and visual motifs that can be used to guide the creation of images. 
		* `lighting` - Lighting profoundly influences the mood, depth, and emphasis within an image. The choice of lighting can range from natural daylight to dramatic and moody settings. It impacts the visibility of details, the presence of shadows, and the overall ambiance.
		* `colors` - The color palette in an image can convey emotions, symbolism, and themes. The selection of colors influences the visual harmony and can create stark contrasts or subtle tonal variations. 
 		* `framing` - Framing dictates the composition and perspective of the image. It can range from close-up shots to wide-angle views and various angles. 
 	- Example:
		* `A serene forest glade, A fox resting beneath a sun-dappled oak tree, its tail curled around its body in contentment, Peaceful and contemplative, Watercolor,  Impressionist, Inspired by the works of Claude Monet, particularly "Water Lilies", Soft, diffused morning sunlight filtering through the leaves, A pastel palette dominated by shades of green, with hints of pink and blue in the flowers, A wide-angle view capturing the entire forest glade, with the fox as the central focus`
- **Structure for a good prompt**
	1. Subject (required)
    2. Medium
    3. Style
    4. Artist
    5. Website
    6. Resolution
    7. Additional details
    8. Color
    9. Lighting
- Prompt Examples
	* Capture image of multiple character poses
		* `create a storyboard sequence of a <character/subject> <performing action>`
- **Alternative Sample Structure**
	- Structure: `{Medium/+ opt. Mod/Main style}`,`{Object/Subject}`,`{Details}`,`{Background}`,`{Mods/Embeddings}`
		* `{Medium/+ opt. Mod/Main style}` - What medium and style to use?
		* `{Object/Subject}` - What will be the focus of the image?
		* `{Details}` - What level of detail should be used?
		* `{Background}` - What is in the background/setting for the picture?
		* `{Mods/Embeddings}` - any extras or LORAs
	- Examples:
- **Using ChatGPT/LLMs to Write Prompts for You**
1. From: https://gist.github.com/bluelovers/92dac6fe7dcbafd7b5ae0557e638e6ef
```
Stable Diffusion is an AI art generation model similar to DALLE-2.
Below is a list of prompts that can be used to generate images with Stable Diffusion:

- portait of a homer simpson archer shooting arrow at forest monster, front game card, drark, marvel comics, dark, intricate, highly detailed, smooth, artstation, digital illustration by ruan jia and mandy jurgens and artgerm and wayne barlowe and greg rutkowski and zdislav beksinski
- pirate, concept art, deep focus, fantasy, intricate, highly detailed, digital painting, artstation, matte, sharp focus, illustration, art by magali villeneuve, chippy, ryan yee, rk post, clint cearley, daniel ljunggren, zoltan boros, gabor szikszai, howard lyon, steve argyle, winona nelson
- ghost inside a hunted room, art by lois van baarle and loish and ross tran and rossdraws and sam yang and samdoesarts and artgerm, digital art, highly detailed, intricate, sharp focus, Trending on Artstation HQ, deviantart, unreal engine 5, 4K UHD image
- red dead redemption 2, cinematic view, epic sky, detailed, concept art, low angle, high detail, warm lighting, volumetric, godrays, vivid, beautiful, trending on artstation, by jordan grimmer, huge scene, grass, art greg rutkowski
- a fantasy style portrait painting of rachel lane / alison brie hybrid in the style of francois boucher oil painting unreal 5 daz. rpg portrait, extremely detailed artgerm greg rutkowski alphonse mucha greg hildebrandt tim hildebrandt
- athena, greek goddess, claudia black, art by artgerm and greg rutkowski and magali villeneuve, bronze greek armor, owl crown, d & d, fantasy, intricate, portrait, highly detailed, headshot, digital painting, trending on artstation, concept art, sharp focus, illustration
- closeup portrait shot of a large strong female biomechanic woman in a scenic scifi environment, intricate, elegant, highly detailed, centered, digital painting, artstation, concept art, smooth, sharp focus, warframe, illustration, thomas kinkade, tomasz alen kopera, peter mohrbacher, donato giancola, leyendecker, boris vallejo
- ultra realistic illustration of steve urkle as the hulk, intricate, elegant, highly detailed, digital painting, artstation, concept art, smooth, sharp focus, illustration, art by artgerm and greg rutkowski and alphonse mucha

I want you to write me a list of detailed prompts exactly about the idea written after IDEA. Follow the structure of the example prompts. This means a very short description of the scene, followed by modifiers divided by commas to alter the mood, style, lighting, and more.

IDEA: Write your idea here
```

2. Single Shot with much longer context, from: https://www.reddit.com/r/StableDiffusion/comments/12xr1ns/modified_chatgpt_to_generate_prompts/ (ymmv)
```
I want you to act as a prompt generator for stable diffusion artificial intelligence program. Your job is to provide detailed and creative descriptions that will inspire unique and interesting images from the AI. Keep in mind that the AI is capable of understanding a wide range of language and can interpret abstract concepts, so feel free to be as imaginative and descriptive as possible. The more detailed and imaginative your description, the more interesting the resulting image will be. I am going to provide you with sample prompts so you understand how the syntax for such images is this prompts also sometimes include negative prompts which i also want you to understand. I am also gona provide you with sample parameters which include sampling steps, the sampling method, CFG scale so you better understand how to generate such images. I want you to keep the same style as the provided prompts, so that u include parameters like cinematic lighting or hyperrealistic or anthing fitting to the scene so the image qualtiy will improve. The sampling method which i have available are: Euler A, Euler, LMS, Heun, DPM2, DPM2 a, DPM++ 2S a, DPM++ 2M, DPM++ SDE, DPM fast, DPM adaptive, LMS Karras, DPM2 Karras, DPM2 a Karras, DPM++ 2S a Karras, DPM++ 2M Karras, DPM++ SDE Karras, DDIM, PLMS; so only use those ase parameters. If you understood only reply with "ok give me some image content data"!!!

Prompt: Iron Man, (Arnold Tsang, Toru Nakayama), Masterpiece, Studio Quality, 6k , toa, toaair, 1boy, glowing, axe, mecha, science_fiction, solo, weapon, jungle , green_background, nature, outdoors, solo, tree, weapon, mask, dynamic lighting, detailed shading, digital texture painting
Negative prompt: un-detailed skin, semi-realistic, cgi, 3d, render, sketch, cartoon, drawing, ugly eyes, (out of frame:1.3), worst quality, low quality, jpeg artifacts, cgi, sketch, cartoon, drawing, (out of frame:1.1)
Parameters: Steps: 50, Sampler: Euler a, CFG scale: 7.0

Prompt: (Pope Francis) wearing leather jacket is a DJ in a nightclub, mixing live on stage, giant mixing table, 4k resolution, a masterpiece
Negative prompt: white robe, easynegative, bad-hands-5, grainy, low-res, extra limb, poorly drawn hands, missing limb, blurry, malformed hands, blur
Parameters: Steps: 40, Sampler: DDIM, CFG scale: 8.0

Prompt: I want to generate a group avatar for a Feishu group chat. The role of this group is daily software technical communication. Now the subject technology stacks that members of this group discuss daily include: algorithms, data structures, optimization, functional programming, and the programming languages often discussed are: TypeScript, Java, python, etc. I hope this avatar has a simple aesthetic, this avatar is a single person avatar
Negative prompt: Too complicated lines, too many colors, human, old-fashioned
Parameters: Steps: 20, Sampler: Euler a, CFG scale: 7.0

Prompt: portrait Anime black girl cute-fine-face, pretty face, realistic shaded Perfect face, fine details. Anime. realistic shaded lighting by Ilya Kuvshinov Giuseppe Dangelico Pino and Michael Garmash and Rob Rey, IAMAG premiere, WLOP matte print, cute freckles, masterpiece
Parameters: Steps: 29, Sampler: Euler a, CFG scale: 8.0

Prompt: young Disney socialite wearing a beige miniskirt, dark brown turtleneck sweater, small neckless, cute-fine-face, anime. illustration, realistic shaded perfect face, brown hair, grey eyes, fine details, realistic shaded lighting by ilya kuvshinov giuseppe dangelico pino and michael garmash and rob rey, iamag premiere, wlop matte print, 4k resolution, a masterpiece
Negative prompt: ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, extra limbs...
Parameters: Steps: 29, Sampler: Euler a, CFG scale: 7.0

Prompt: Cute small cat sitting in a movie theater eating chicken wiggs watching a movie ,unreal engine, cozy indoor lighting, artstation, detailed, digital painting,cinematic,character design by mark ryden and pixar and hayao miyazaki, unreal 5, daz, hyperrealistic, octane render
Negative prompt: ugly, ugly arms, ugly hands,
Parameters: Steps: 25, Sampler: Euler a, CFG scale: 8.0

Prompt: Parisian luxurious interior penthouse bedroom, dark walls, wooden panels
Negative prompt: no gold, pink
Parameters: Steps: 20, Sampler: Euler a, CFG scale: 7.0

Prompt: cute girl, crop-top, blond hair, black glasses, stretching, with background by greg rutkowski makoto shinkai kyoto animation key art feminine mid shot
Negative prompt: Deformed, blurry, bad anatomy, disfigured, poorly drawn face, mutation, mutated, extra limb, ugly, poorly drawn hands, missing limb, blurry, floating limbs, disconnected limbs, malformed hands, blur, out of focus, long neck, long body, ((((mutated hands and fingers)))), (((out of frame)))
Parameters: Steps: 30, Sampler: DDIM, CFG scale: 12.0

Prompt: houses in front, houses background, straight houses, digital art, smooth, sharp focus, gravity falls style, doraemon style, shinchan style, anime style
Negative prompt: blurry image, watermark, messy
Parameters: Steps: 50, Sampler: Euler a, CFG scale: 8.5

Prompt: High quality 8K painting impressionist style of a Japanese modern city street with a girl on the foreground wearing a traditional wedding dress with a fox mask, staring at the sky, daylight Negative prompt: blur, cars, low quality
Parameters: Steps: 35, Sampler: Euler a, CFG scale: 7.0

Prompt: A hyper realistic avatar of a guy riding on a black honda cbr 650r in leather suit,high detail, high quality,8K,photo realism
Negative prompt: flying mirrors,low quality
Parameters: Steps: 20, Sampler: Euler a, CFG scale: 7.0

Prompt: the street of amedieval fantasy town, at dawn, dark, 4k, highly detailed
Parameters: Steps: 40, Sampler: DPM++ 2M Karras, CFG scale: 7.0

Prompt: overwhelmingly beautiful eagle framed with vector flowers, long shiny wavy flowing hair, polished, ultra detailed vector floral illustration mixed with hyper realism, muted pastel colors, vector floral details in background, muted colors, hyper detailed ultra intricate overwhelming realism in detailed complex scene with magical fantasy atmosphere, no signature, no watermark
Parameters: Steps: 20, Sampler: Euler a, CFG scale: 7.0

Prompt: a highly detailed matte painting of a man on a hill watching a rocket launch in the distance by studio ghibli, makoto shinkai, by artgerm, by wlop, by greg rutkowski, volumetric lighting, octane render, 4 k resolution, trending on artstation, masterpiece | hyperrealism| highly detailed| insanely detailed| intricate| cinematic lighting| depth of field
Parameters: Steps: 36, Sampler: Euler a, CFG scale: 14.0

Prompt: electronik robot and ofice ,unreal engine, cozy indoor lighting, artstation, detailed, digital painting,cinematic,character design by mark ryden and pixar and hayao miyazaki, unreal 5, daz, hyperrealistic, octane render
Negative prompt: ugly hands
Parameters: Steps: 25, Sampler: DDIM, CFG scale: 8.0

Prompt: Cute small Fox sitting in a movie theater eating popcorn watching a movie ,unreal engine, cozy indoor lighting, artstation, detailed, digital painting,cinematic,character design by mark ryden and pixar and hayao miyazaki, unreal 5, daz, hyperrealistic, octane render
Negative prompt: ugly, ugly arms, ugly hands,
Parameters: Steps: 25, Sampler: Euler a, CFG scale: 8.0

Prompt: futuristic lighthouse, flash light, hyper realistic, epic composition, cinematic, landscape vista photography, landscape veduta photo & tdraw, detailed landscape painting rendered in enscape, miyazaki, 4k detailed post processing, unreal engineered
Parameters: Steps: 25, Sampler: Euler a, CFG scale: 5

Prompt: A beautiful painting of water spilling out of a broken pot, earth colored clay pot, vibrant background, by greg rutkowski and thomas kinkade, Trending on artstation, 8k, hyperrealistic, extremely detailed Parameters: Steps: 42, Sampler: PLMS, CFG scale: 7

Prompt: Luminism is an American landscape painting style of the 1850s to 1870s, characterized by effects of light in landscape, through the use of aerial perspective and the concealment of visible brushstrokes. Luminist landscapes emphasize tranquility, and often depict calm, reflective water and a soft, hazy sky. Luminist paintings with their smaller size evoke a quiet spirituality based on closely observed natural phenomena, especially the quality of light. Trending on artstation ...
Parameters: Steps: 40, Sampler: PLMS, CFG scale: 7

Prompt: Cute darth vader style minion, holidays in Paris, unreal engine, octane render, 4k

Prompt: highly detailed albert einstein playing minecraft, epic laboratory office, shelves with detailed items in background, ((long shot)), highly detailed realistic painting by grandmaster, unreal engine, octane render, 4k, by artgerm and Drew Struzan and Krenz Cushart, trending on artstation Parameters: Steps: 50, Sampler: PLMS, CFG scale: 7

Prompt: higly detailed, majestic royal tall ship on a calm sea,realistic painting, by Charles Gregory Artstation and Antonio Jacobsen and Edward Moran, (long shot), clear blue sky, intricated details, 4k Parameters: Steps: 50, Sampler: PLMS, CFG scale: 7.0

Prompt: Ethereal gardens of marble built in a shining teal river in future city, gorgeous ornate multi-tiered fountain, futuristic, intricate elegant highly detailed lifelike photorealistic realistic painting, long shot, studio lighting, octane render, by Dorian Cleavenger
Negative prompt: (disfigured), black and white, bad anatomy, bad hands
Parameters: Steps: 20, Sampler: Euler a, CFG scale: 7.0

Prompt: arcane style. samdoesarts style. A boy standing next to his bicycle watching a rocket blast off. One hand up shielding his eyes. Cinematic. Aesthetically pleasing. Volumetric lighting. Highly detailed. Realistic. Anamorphic lens flare from the rocket engine. Smoke trail from rocket. In the style of Frederick McCubbin, Ivan Aivazovsky, Daniel F Gerhartz, and Simon Stalenhag.
Parameters: Steps: 30, Sampler: DPM++ 2M Karras, CFG scale: 8

Prompt: majestic photorealistic painting of a (beautiful woman sorceress discovering shiny luminescence of magic powers), 8k resolution, shimmering lighting
Parameters: Steps: 20, Sampler: DDIM, CFG scale: 7

Prompt: !1970s teenager disorded and messy bedroom, posters on the wall, vinyl records on the floor, old guitar in the corner, day outside of the window courtains, hippy movement, hyperdetailed analog atmospheric natural lighting, sharp focus, concept art trending on artstation by Stephen Darbishire and greg rutkowski and Kilian Eng, cozy atmospheric and cinematic lighting, hyperdetailed, photorealistic, neat and tidy, magical, ambient light, sharp focus
Parameters: Sampler: dpmpp_2m, Steps: 30, CFG scale: 5

Prompt: sexy girl, full length frame, High detail RAW color art, (((green lingerie))), green eyes, (elegant, beautiful face), piercing, (tattoed), (freckles), pinup makeup, ketch of woman full body, thick thighs, (((cute milky girl))), winter atmosphere, ((toxic long hair)), ((leather underwear)), (detailed skin, skin texture), (intricately detailed, fine details, hyperdetailed), raytracing, subsurface scattering, (winter nature on background), ((muted colors)), diffused soft lighting, shallow depth of field, 28mm lens, F/2. 8, sharp focus bokeh Negative prompt: lowres, text, error, cropped, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, out of frame, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck, username, watermark, signature Parameters: unkown 
```
---------------------------------------------------------------------------------------------------------




---------------------------------------------------------------------------------------------------------
### <a name="promptsamples"></a>Prompt samples/Bases
* General structure: `$medium in $style of <rest of prompt>`
- **Generic**
	1. 
---------------------------------------------------------------------------------------------------------





## License

This project is dedicated to the public domain under the Unlicense.
You can find the full text of the Unlicense in the [UNLICENSE](UNLICENSE) file.
