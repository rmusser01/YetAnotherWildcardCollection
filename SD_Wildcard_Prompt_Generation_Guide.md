# Stable Diffusion WildCard Prompt Catalogue

------------------------------------------------------------------------------------------------------------
## Table of Contents
- [Stable Diffusion 101](#sd101)
- [Writing Prompts](#writeprompt)
- [Prompt Pieces](#ppieces)

------------------------------------------------------------------------------------------------------------


Gen Process: https://github.com/adieyal/sd-dynamic-prompts/blob/main/docs/tutorial.md
	* https://github.com/adieyal/sd-dynamic-prompts/blob/main/docs/SYNTAX.md
	* https://github.com/adieyal/sd-dynamic-prompts/blob/main/docs/tutorial.md
	* https://github.com/Siberpone/lazy-pony-prompter
	* https://github.com/Siberpone/pd-styles


Catalogs:
	* List of: https://github.com/adieyal/sd-dynamic-prompts?tab=readme-ov-file#collections
	* https://github.com/Vetchems/sd-danbooru-tags
	* https://github.com/aoirusann/my-sd-wildcard
	* https://github.com/LulzRose/YetAnotherWildcardCollection
	* https://github.com/adieyal/sd-dynamic-prompts/tree/main/collections/jumbo
	* https://rentry.org/NAIwildcards
	* https://github.com/adieyal/sd-dynamic-prompts/tree/main/collections/nsp
	* https://github.com/adieyal/sd-dynamic-prompts/tree/main/collections/devilkkw




Prompt Cleaners:
	* https://github.com/techvishnu/SDPromptGenerator



https://github.com/Stability-AI/StableSwarmUI/discussions/11
Wildcards! You can now create wildcard files and use them. You can manage the entirely in the UI, -or- just go store some .txt files into Swarm/Data/Wildcards (or configure the path in server settings).

Use in a prompt like <wildcard:animals>, or just click the card in the UI.

Wildcard files are simple text - one entry per line.
Wildcards can contain prompt-syntax (eg another wildcard inside the wildcard, or a preset, or whatever you want)
Use # to comment a line (not count in the options list).





---------------------------------------------------------------------------------------------------------
### 101/What is this?
- **101**
	* This is a repo/guide whose purpose is to help facilitate and improve the process of generating images using wildcards.
- **Links**
	* `stable-diffusion-webui-wildcards` extension: https://github.com/AUTOMATIC1111/stable-diffusion-webui-wildcards
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
---------------------------------------------------------------------------------------------------------





---------------------------------------------------------------------------------------------------------
## <a name="ppieces"></a> Prompt Pieces
### Booru tag structure
#### Visual characteristics
- **Image composition and style**
	- **Artistic license(fanfiction changes)**
		* Major changes
		* Changes of the whole attire
		* Changes of specific clothes or accessories
		* Changes of body parts other than hair and eyes
		* Changes of hair
		* Changes of eyes
		* Changes of personality and roles
		* Changes of overall colors
		* Changes of age
		* Other changes
	- **Image composition**
		* View Angle
		* Perspective / Depth
		* Composition
		* Format
		* Subject matter
		* Framing the body
		* Styles
		* Techniques
		* Traditional Japanese Patterns
		* Other Patterns
		* Flaws
		- **Backgrounds**
			* Colors
			* Multiple Colors
			* Patterns
			* Other
		- **Censorship**
			* Censored and uncensored things
			* Visual Forms of Censorship
			* Auditory forms of censorship
		- **Colors**
			* Single color themes
			* Color Palettes
			* Coloring and Shading Styles
			* Miscellaneous
		- **Focus tags**
			* Body parts
			* Gender
			* Object
			* Other
		- **Prints**
			* Patterns
			* Specific Prints
			* Patterned Things
			* Print Items
		- **List of style parodies**
			* General style parodies
			* By Decade
			* By Design
			* By Copyright
			* Artist styles
	- **Text**
		* Misc
		* Literary devices
		* Specific pieces of text
		* Actions
		* Did not create txts for language lists.
	- **Symbols**
	- **Year tags**
		* Nah.
- **Body**
	- **Body parts**
		- **Ass**
		- **Breasts tags**
		- **Face tags**
			- **Eyes tags**
		- **Ears tags**
		- **Hair**
			- **Hair color**
			- **Hair styles**
		- **Hands**
			- **Gestures**
		- **Neck and neckwear**
		- **Posture**
		- **Pussy**
		- **Shoulders**
		- **Skin color**
		- **Tail**
		- **Wings**
	- **Injury**
- **Attire and body accessories**
	- **Attire**
		- **Dress
		- **Headwear**
		- **Legwear**
		- **Neck and neckwear**
		- **Sexual attire**
			- **Bra**
			- **Panties**
		- **Sleeves**
		- **Swimsuit**
	- **Eyewear**
	- **Nudity**
- **Sex**
	* (For intimate attire, see "Attire" section above)
	* (For sexual objects, see "Objects" section below)
	- **Sex acts**
		- **Sexual positions**
- **Objects**
	- **Computer**
	- **Airplanes**
	- **Armor**
	- **Ground Vehicles**
	- **Helicopters**
	- **Pokemon objects**
	- **Ships**
	- **Weapons**
	- **Audio tags**
	- **Cards**
		- **List of playing card faces**
	- **Eyewear**
	- **Piercings**
	- **Sex objects**
- **Creatures**
	- **List of animals**
		- **Birds**
		- **Cats**
		- **Dogs**
	- **Legendary creatures**
- **Plants**
	- **Plant**
		- **Tree**
	- **Flowers**
- **Games**
	- **List of game activities**
	- **Board games**
	- **Sports**
	- **Video game**
- **Real World**
	- **Companies and brand names**
	- **Holidays and celebrations**
	- **Jobs**
	- **Locations**
	- **People**
	- **Real world locations**
- **More**
	- **Family relationships**
	- **Food tags**
	- **Fire**
	- **Groups**
	- **Meme**
	- **Phrases**
	- **Scan**
	- **Subjective**
	- **Technology (includes Sci-Fi)**
	- **Verbs and Gerunds**
	- **Water**

#### <a name="capm"></a>Copyrights, artists, projects and media
- **Genres of video games**
	- **Fighting games**
	- **Platform games**
	- **Role-playing games**
	- **Shooter games**
	- **Visual novel games**
- **Artists**
	- **List of named artists(non-mainstream commercial)**
	- **Pixiv projects**
- **Characters**
	- **Ace Attorney characters**
	- **Arknights characters**
	- **Atelier characters**
	- **Azur Lane characters**
	- **Bleach characters**
	- **Bokujou Monogatari characters**
	- **Brave Girl Ravens characters**
	- **Danganronpa characters**
	- **Digimon**
		- **Digimon characters**
	- **Dragon Ball characters**
	- **Dragon Quest characters**
	- **Fate Series characters**
	- **Final Fantasy characters**
	- **Fire Emblem characters**
	- **Flower Knight Girl characters**
	- **Gensou Suikoden characters**
	- **Girls' Frontline characters
	- **Girls und Panzer characters**
	- **Hunter x Hunter characters**
	- **JoJo no Kimyou na Bouken characters**
	- **Kamen Rider characters**
	- **Kantai Collection characters**
	- **Kingdom Hearts characters**
	- **Mahou Sensei Negima characters**
	- **Meitantei Conan characters**
	- **Naruto characters**
	- **Nippon Ichi characters**
	- **One Piece characters**
	- **Oshiro Project characters**
	- **Pokémon characters**
		- **Elite Four Members**
		- **Gym Leaders**
		- **families of Pokémon main characters**
		- **Pokémon Ranger characters**
		- **Pokémon Trainer classes**
	- **Pokémon**
	- **Pretty Cure characters**
	- **Ragnarok Online characters**
	- **Rosenkreuzstilette characters**
	- **Sailor Moon characters**
	- **World Witches Series characters**
	- **Tales of... characters**
	- **Toaru Majutsu no Index characters**
	- **Touhou characters**
	- **Touken Ranbu characters**
	- **Umamusume characters**
	- **Vocaloid characters**
	- **Yu-Gi-Oh! characters**
	- **genderswap characters**
	- **Official Mascots**

#### <a name="more"></a>More
- **List of disambiguation pages**
- **Magazine Publications**
- **Special Moves**
- **Uniforms**
- **Pokemon media**
- **Tagged Songs**
- **Vocaloid Derivatives**
- **Vocaloid songs**
- **Vocal synthesizers**
- **DeeMo songs**
- **Zaku II variants**








































https://github.com/AUTOMATIC1111/stable-diffusion-webui-wildcards