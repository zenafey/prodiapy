import subprocess
import sys
import os

def install(packages):
    subprocess.check_call([sys.executable, "-m", "pip", "install", *packages])

# Example usage:
packages = ['imaginepy', 'tk', 'ttkthemes', 'aiohttp', 'prodiapy==3.3']
install(packages)

print("Finished installing requirements.")

from prodia import Client, Model, Sampler
import requests
import os
import sys
import shutil
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
import threading
import io
import uuid
import requests
import webbrowser
import subprocess
from imaginepy import Imagine  # New import statement

progress_popover = None  # Global variable to store the progress popover

styles = [
    "NONE: ",
    "UNIVERSAL ANIMAL: extreme detail, very detailed, focused subject, photorealistic shot, highly detailed, detailed face, realistic skin and fur, detailed eyes, cinematic composition, 4K, UHD, backlit, pensive and curious expression, artstation, trending, beautiful background, extreme lighting effects, breathtaking lighting effects, realism, Beautiful lively background, sunshafts, cinematic lighting, spectacular lighting, very detailed, beautiful, High Quality, 8K, Cinematic Lighting, Stunning background, focused subject, high detail, realistic, incredible 16k resolution produced in Unreal Engine 5 and Octane Render for background",
    "UNIVERSAL LANDSCAPE: extreme detail, very detailed, focused subject, beautiful background, landscape, beautiful landscape, stunning landscape, landscape lighting effects, breathtaking landscape, realism, Beautiful lively background, sunshafts, cinematic lighting, spectacular lighting, very detailed, beautiful, High Quality, 8K, Cinematic Lighting, Stunning background, focused subject, high detail, realistic, incredible 16k resolution produced in Unreal Engine 5 and Octane Render for background",
    "UNIVERSAL PERSON: extreme detail, very detailed, focused subject, photorealistic shot, highly detailed, detailed face, realistic skin, detailed eyes, cinematic composition, 4K, UHD, backlit, pensive and curious expression, artstation, trending, beautiful background, extreme lighting effects, breathtaking lighting effects, realism, Beautiful lively background, sunshafts, cinematic lighting, spectacular lighting, very detailed, beautiful, High Quality, 8K, Cinematic Lighting, Stunning background, focused subject, high detail, realistic, incredible 16k resolution produced in Unreal Engine 5 and Octane Render for background",
    "ABSTRACT_CITYSCAPE: abstract cityscape, Ultra Realistic Cinematic Light abstract, futuristic, cityscape, out of focus background and incredible 16k resolution produced in Unreal Engine 5 and Octane Render",
    "ABSTRACT EXPRESSIONISM: abstract expressionist style, gestural brushstrokes, bold and expressive, emotional and spontaneous, Jackson Pollock-inspired, non-representational",
    "ABSTRACT_VIBRANT: vibrant, editorial, abstract elements, colorful, color splatter, realism, inspired by the style of Ryan Hewett, dynamic realism, soft lighting and intricate details",
    "AQUASTIC: graceful movement with intricate details, inspired by artists like Lotte Reiniger, Carne Griffiths and Alphonse Mucha. Dreamy and surreal atmosphere, twirling in an aquatic landscape with water surface",
    "AQUATIC: vast and diverse underwater ecosystems, vivid blues and greens, ethereal lighting, sea creatures, coral reefs, undulating oceanic forms. The atmosphere is tranquil, inviting exploration and discovery. Techniques include gradient shading, texturing to mimic water surfaces, and a blend of realism and fantasy. Key influences might include traditional marine art, scientific illustrations, and the fantastical representations of the sea in animated films.",
    "AMAZONIAN: Amazonian cave, landscape, jungle, waterfall, moss-covered ancient ruins, dramatic lighting and intense colors, mesmerizing details of the environment and breathtaking atmosphere",
    "ANIME: anime atmospheric, atmospheric anime, anime character; full body art, digital anime art, beautiful anime art style, anime picture, anime arts, beautiful anime style, digital advanced anime art, anime painting, anime artwork, beautiful anime art, detailed digital anime art, anime epic artwork",
    "ARCHITECTURE: modern architecture design, luxury architecture, bright, very beautiful, trending on Unsplash, breathtaking",
    "ART: Painting, by Salvador Dali, allegory, surrealism, religious art, genre painting, portrait, painter, still life",
    "ASSET_RENDER: isometric, polaroid Octane Render, 3D render 1.5 0 mm lens, KeyShot product render, rendered, KeyShot product render Pinterest, 3D product render, 3D CGI render, 3D CGI render, ultra wide-angle isometric view",
    "AVATAR: avatar movie, avatar with blue skin, vfx movie, cinematic lighting, utopian jungle, pandora jungle, sci-fi nether world, lost world, pandora fantasy landscape, lush green landscape, high quality render",
    "BAUHAUS: Bauhaus art movement, by Wassily Kandinsky, Bauhaus style painting, geometric abstraction, vibrant colors, painting",
    "CANDYLAND: candy land style, whimsical fantasy landscape art, japanese pop surrealism, colorful digital fantasy art, made of candy and lollipops, whimsical and dreamy",
    "CLAYMATION: clay animation, as a claymation character, claymation style, animation key shot, plasticine, clay animation, stopmotion animation, aardman character design, plasticine models",
    "COLORING_BOOK: line art illustration, lineart Behance HD, illustration line art style, line art coloring page, decora inspired illustrations, coloring pages, digital line-art, line art!!, thick line art, coloring book page, clean coloring book page, black ink line art, coloring page, detailed line art",
    "COMIC_BOOK: Comic cover, 1960s Marvel comic, comic book illustrations",
    "COSMIC: in cosmic atmosphere, humanitys cosmic future, space art concept, space landscape, scene in space, cosmic space, beautiful space star planet, background in space, realistic, cinematic, breathtaking view",
    "CUBISM: cubist Picasso, cubism, a cubist painting, heavy cubism, cubist painting, by Carlo Carrà, style of Picasso, modern cubism, futuristic cubism",
    "CYBERPUNK: synthwave image, (neotokyo), dreamy colorful cyberpunk colors, cyberpunk Blade Runner art, retrofuturism, cyberpunk, beautiful cyberpunk style, CGSociety 9",
    "DIGITAL GLITCH ART: Highly saturated and contrasting colors, heavy use of black and bright neons, Texture Pixelated, distorted, or 'glitchy', this style intentionally harnesses digital errors for aesthetic effect, Abstract form, irregular, and chaotic, often featuring repeated motifs or patterns, Can evoke feelings of confusion, excitement, and a sense of being 'plugged in' to the digital age",
    "DISNEY: disney animation, disney splash art, disney color palette, disney renaissance film, disney pixar movie still, disney art style, disney concept art :: nixri, wonderful compositions, pixar, disney concept artists, 2d character design",
    "DYSTOPIAN: cifi world, cybernetic civilizations, peter gric and dan mumford, brutalist dark futuristic, dystopian brutalist atmosphere, dark dystopian world, cinematic 8k, end of the world, doomsday",
    "ELVEN: elven lifestyle, photoreal, realistic, 32k quality, crafted by Elves and engraved in copper, elven fantasy land, hyper detailed",
    "EXTRA_TERRESTRIAL: deepdream cosmic, painting by Android Jones, cosmic entity, humanoid creature, James Jean soft light 4k, sci-fi, extraterrestrial, cinematic",
    "FANTASY: fantasy matte painting, fantasy landscape, ( ( Thomas Kinkade ) ), whimsical, dreamy, Alice in Wonderland, daydreaming, epic scene, high exposure, highly detailed, Tim White, Michael Whelan",
    "FIREBENDER: fire elements, fantasy, fire, lava, striking. A majestic composition with fire elements, fire and ashes surrounding, highly detailed and realistic, cinematic lighting",
    "FORESTPUNK: forestpunk, vibrant, HDRI, organic motifs and pollen in the air, bold vibrant colors and textures, spectacular sparkling rays, photorealistic quality with Hasselblad",
    "FRACTAL: fractal patterns, fractal geometry, psychedelic mandala, fractal mandala art, fractal patterns, abstract fractal",
    "FRESCO: fresco painting, wall frescoes, frescoes, from the history, detailed fresco, fresco, renaissance, fresco in a church",
    "FUTIRISTIC CITYSCAPE: Dominated by blues, silvers, and neon accents like purples, pinks, cyans, Texture Smooth and polished surfaces contrast with gritty, urban elements, There can be high-contrast lighting and reflections, Geometric form, angular, and sometimes asymmetrical shapes, The skyline would be a common motif, A sense of anticipation and excitement, mixed with a feeling of isolation and the unknown",
    "GHOTIC: goth lifestyle, dark goth, grunge, cinematic photography, dramatic dark scenery, dark ambient beautiful",
    "GLASS_ART: inside glass ball, translucent sphere, CGSociety 9, glass orb, Behance, polished, beautiful digital artwork, exquisite digital art, in a short round glass vase, Octane Render",
    "GLITCH: glitch, glitch art, glitched, glitchy, glitch aesthetic, colorful glitched, glitchy, glitching",
    "GRAFFITI: graffiti background, colorful graffiti, graffiti art style, colorful mural, ravi supa, symbolic mural, juxtapoz, pablo picasso, street art",
    "GREEK_MYTHOLOGY: Greek mythology, mythology art, Olympus gods, dramatic lighting and intense colors, attention to detail and to the ancient history, ancient Greek myths",
    "GTA: gta iv art style, gta art, gta loading screen art, gta chinatown art style, gta 5 loading screen poster, grand theft auto 5, grand theft auto video game",
    "HALLOWEEN: in Halloween style, Halloween, dark, moody, atmospheric, horror art style, Halloween fantasy art, Halloween concept, CGSociety 7, halloween, creepy",
    "HAUNTED: horror CGI 4k, scary color art in 4k, horror movie cinematography, Insidious, La Llorona, still from animated horror movie, film still from horror movie, haunted, eerie, unsettling, creepy",
    "HD QUALITY LIGHTING: Beautiful lively background, sunshafts, cinematic lighting, spectacular lighting, very detailed, beautiful",
    "High QUALITY: High Quality, 8K, Cinematic Lighting, Stunning background, focused subject, high detail, realistic, incredible 16k resolution produced in Unreal Engine 5 and Octane Render for background, sunshafts",
    "HISTORICAL: 18th-century French fashion, oil painting, historical figure, in the style of Rococo, based on historical costumes, history, historical, classical",
    "HORROR: classic horror, classic horror movie style, in a creepy atmosphere, in a horrifying atmosphere, CGSociety 5, horror art style",
    "ICON: single vector graphics icon, iOS icon, smooth shape, vector",
    "ILLUSTRATION: minimalistic vector art, illustrative style, style of Ian Hubert, style of Gilles Beloeil, inspired by Hsiao-Ron Cheng, style of Jonathan Solter, style of Alexandre Chaudret, by Echo Chernik",
    "IMPRESSIONISM: impressionism, impressionist, impressionist painting, post-impressionism, style of impressionism, impressionistic, style of Monet",
    "INK: Black Ink, Hand drawn, Minimal art, ArtStation, ArtGem, monochrome",
    "INDUSTRIAL: industrial, digital art, dystopian cityscape, intense color, complex composition, post-industrial, urban",
    "INTERIOR: modern architecture by Makoto Shinkai, Ilya Kuvshinov, Lois van Baarle, Rossdraws, and Frank Lloyd Wright",
    "JAPANESE: with Japanese themes, Japan, Japanese woodblock print, ukiyo-e, Japan, Japanese woodblock style, Hiroshige, Hokusai",
    "JUNGLE: Jungle scene, jungle atmosphere, lush green jungle, jungle landscape, deep in the jungle, realistic jungle, jungle CGSociety 3",
    "KAWAII_CHIBI: kawaii chibi romance, fantasy, illustration, colorful idyllic cheerful, kawaii chibi inspired",
    "KNOLLING_CASE: in square glass case, glass cube, glowing, knolling case, Ash Thorp, studio background, Desktopography, CGSociety 9, CGSociety, mind-bending digital art",
    "LANDSCAPE: landscape, beautiful landscape, stunning landscape, mountainous landscape, beautiful digital landscape, landscape painting, breathtaking landscape, realism",
    "LOGO: creative logo, unique logo, visual identity, geometric type, graphic design, logotype design, brand identity, vector based, trendy typography, best of Behance",
    "LUMINOUS: ethereal, glowing, soft light, luminous colors, dreamlike, celestial, radiant, otherworldly, transcendent, mystical, heavenly",
    "MACRO_PHOTOGRAPHY: macro photography, award winning macro photography, depth of field, extreme closeup, 8k hd, focused",
    "MAGICAL: magical, magical world, magical realism, magical atmosphere, in a magical world, magical fantasy art",
    "MAGIC EYE: Stereogram, magic eye, autostereogram, different colors, patterns or dots, when viewed with crossed eyes a 3D object should emerge,  when viewed with crossed eyes a 3D object should emerge",
    "MANDALA: mandala, mandala design, intricate mandala, mandala art, complex mandala, beautiful mandala",
    "MANGA: manga style, comic book art, black and white ink, dynamic poses, expressive characters, manga panel layout, action-packed scenes",
    "MARBLE: in greek marble style, classical antiquities, ancient greek classical ancient greek art, marble art, realistic, cinematic",
    "MARBLEIZED: marble texture, abstract patterns, vibrant colors, fluid and organic shapes, mesmerizing and unique, inspired by marbling techniques, surreal atmosphere",
    "MARVEL: album art, Poster, layout, typography, logo, risography, Ghibli, Simon Stålenhag, insane detail, ArtStation, 8k",
    "MATISSE: Matisse, Matisse cutouts, Matisse style, Matisse painting, Henri Matisse, Matisse's",
    "MECHA: futuristic mech design, robotic, mechanical, cybernetic, sleek and angular, high-tech, mechanical details, sci-fi battle scene, metallic textures",
    "MECHANICAL: mechanical gears, steampunk, mechanical devices, intricate details, metallic textures, gears and cogs, mechanical clockwork, industrial aesthetic",
    "MEDIEVAL: movie still from Game of Thrones, powerful fantasy epic, middle ages, lush green landscape, olden times, Roman Empire, 1400 CE, highly detailed background, cinematic lighting, 8k render, high quality, bright colors",
    "METROPOLIS: urban cityscape, towering skyscrapers, bustling streets, neon lights, futuristic elements, cyberpunk-inspired, dynamic composition",
    "MINECRAFT: minecraft build, style of minecraft, pixel style, 8 bit, epic, cinematic, screenshot from minecraft, detailed natural lighting, minecraft gameplay, mojang, minecraft mods, minecraft in real life, blocky like minecraft",
    "MINIMALISM: minimalism, minimalist, minimalist aesthetic, minimalistic style, minimalist art, clean and minimal",
    "MINIMALIST: minimalist art, minimalistic design, clean lines, simplicity, negative space, minimal color palette, minimalistic composition",
    "MOONLIT: moonlit scenery, night sky, soft moonlight, stars, tranquil atmosphere, dreamy and ethereal, nocturnal landscape",
    "MOTION_BLUR: dynamic motion blur, fast movement, blurred lines, sense of speed, energetic composition, action-packed, motion blur effect",
    "MYSTICAL: fireflies, deep focus, D&D, fantasy, intricate, elegant, highly detailed, digital painting, ArtStation, concept art, matte, sharp focus, illustration, Hearthstrom, Gereg Rutkowski, Alphonse Mucha, Andreas Rocha",
    "MYSTICAL JUNGLE: Primarily deep greens, bursts of vibrant tropical flower colors like pinks, yellows, and reds, hints of sky blues and dappled sunlight,Texture Rich and detailed, with heavy use of leafy patterns, floral shapes, and animal textures like fur or feathers, Abstract form, organic forms, but sometimes sharply focused to resemble flora or fauna, Invokes a sense of adventure and mystery, with an undercurrent of serenity",
    "MONOCHROME: black-and-white, monochrome, grayscale, noir, black-and-white photography, monochromatic",
    "NEO_FAUVISM: neo-fauvism painting, neo-fauvism movement, digital illustration, poster art, CGSociety saturated colors, fauvist",
    "NEON: neon art style, night time dark with neon colors, blue neon lighting, violet and aqua neon lights, blacklight neon colors, rococo cyber neon lighting"
    "NEO_NOIR: neo-noir cinematography, dark and moody atmosphere, film noir-inspired lighting, shadows, and high contrast, urban setting, mysterious and atmospheric, cinematic quality",
    "NFT: NFT art style, NFTs, NFT art, digital NFT, NFT",
    "NIGHTMARE: nightmarish, nightmare, scary, creepy, unsettling, creepy horror",
    "NORDIC: Nordic landscapes, serene and tranquil, snowy mountains, fjords, minimalist design, earthy tones, natural beauty",
    "NOSTALGIA: nostalgic, vintage-inspired, retro colors, old film aesthetic, grainy texture, 80s vibes, sentimental, warm and cozy, reminiscent of childhood",
    "OCEAN: Ocean scene, under the sea, deep sea, sea creature, ocean landscape, beautiful underwater",
    "OCEANIC: underwater world, vibrant coral reefs, tropical fish, shimmering water, ethereal lighting, dreamlike and immersive",
    "OLD_WESTERN: Old Western, Wild West, cowboy era, rustic landscapes, dusty trails, vintage sepia tones, rugged charm",
    "ORIENTAL: oriental landscape painting, traditional Asian art style, Chinese ink painting, delicate brushwork, tranquil and serene, cherry blossoms, pagodas, and mountains, harmonious color palette",
    "ORIGAMI: polygonal art, layered paper art, paper origami, wonderful compositions, folded geometry, paper craft, made from paper",
    "PAPERCUT_STYLE: layered paper art, paper modeling art, paper craft, paper art, papercraft, paper cutout, paper cut out collage artwork, paper cut art",
    "PAINTING: atmospheric dreamscape painting, by Mac Conner, vibrant gouache painting scenery, vibrant painting, vivid painting, a beautiful painting, dream scenery art, Instagram art, psychedelic painting, lo-fi art, bright art",
    "PALETTE_KNIFE: detailed impasto brush strokes, detail acrylic palette knife, thick impasto technique, palette knife, vibrant 8k colors",
    "PASTEL DREAM: pastel colors, dreamy atmosphere, soft and gentle, whimsical, fantasy world, delicate brushstrokes, light and airy, tranquil, serene, peaceful, nostalgic",
    "PICASO: painting, by Pablo Picasso, cubism",
    "PIXEL: pixel art, pixelated, pixel-style, 8-bit style, pixel game, pixel",
    "PIXEL_HORROR: pixel horror game, pixel horror, horror pixel, scary pixel, horror game pixel art, 8-bit horror",
    "PIXIE_DUST: pixie dust, fairy dust, magical, shimmering, glowing, sparkling, ethereal",
    "POLAROID: old polaroid, 35mm",
    "POLY_ART: low poly, ArtStation, studio lighting, stainless steel, grey color scheme",
    "POP_ART: Pop art, Roy Lichtenstein, Andy Warhol, pop art style, comic book, pop",
    "POSTER_ART: album art, Poster, layout, typography, logo, risography, Ghibli, Simon Stålenhag, insane detail, ArtStation, 8k",
    "POST_APOCALYPTIC: post-apocalyptic landscape, post-apocalyptic, dystopian, end of the world, post-apocalypse, wasteland",
    "PRIMITIVE: prehistoric cave painting, cave art, ancient art, primitive style, tribal, caveman",
    "PRODUCT_PHOTOGRAPHY: product photo studio lighting, high detail product photo, product photography, commercial product photography, realistic, light, 8k, award winning product photography, professional closeup",
    "RAINFOREST: intricate rainbow environment, rainbow bg, from lorax movie, pixar color palette, volumetric rainbow lighting, gorgeous digital painting, 8k cinematic",
    "RENDER: isometric, polaroid Octane Render, 3D render 1.5 0 mm lens, KeyShot product render, rendered, KeyShot product render Pinterest, 3D product render, 3D CGI render, 3D CGI render, ultra wide-angle isometric view",
    "RENAISSANCE: Renaissance period, neo-classical painting, Italian Renaissance workshop, pittura metafisica, Raphael high Renaissance, ancient Roman painting, Michelangelo painting, Leonardo da Vinci, Italian Renaissance architecture",
    "RETRO: retro futuristic illustration, featured on Illustrationx, Art Deco illustration, beautiful retro art, stylized digital illustration, highly detailed vector art, Mads Berg, automotive design art, epic smooth illustration, by Mads Berg, stylized illustration, Ash Thorp Khyzyl Saleem, clean vector art",
    "RETROWAVE: Illustration, retrowave art, neon light, retro, digital art, trending on ArtStation",
    "ROCOCO: François Boucher oil painting, rococo style, rococo lifestyle, a Flemish Baroque, by Karel Dujardin, vintage look, cinematic hazy lighting",
    "ROMANTIC: romantic scene, romantic atmosphere, romantic style, romance, love, affection",
    "SALVADOR_DALI: Painting, by Salvador Dali, allegory, surrealism, religious art, genre painting, portrait, painter, still life",
    "SAMURAI: samurai lifestyle, Miyamoto Musashi, Japanese art, ancient Japanese samurai, feudal Japan art, feudal Japan art",
    "SCATTER: breaking pieces, exploding pieces, shattering pieces, disintegration, contemporary digital art, inspired by Dan Hillier, inspired by Igor Morski, dramatic digital art, Behance art, CGSociety 9, 3D advanced digital art, mind-bending digital art, disintegrating",
    "SCIFI: science fiction, futuristic, alien planet, space, otherworldly, cosmic",
    "SHAMROCK_FANTASY: shamrock fantasy, fantasy, vivid colors, grapevine, celtic fantasy art, lucky clovers, dreamlike atmosphere, captivating details, soft light and vivid colors",
    "SILHOUETTE: silhouette, dark figure, silhouette against the sunset, shadowy, outline, figure",
    "SKETCH: pencil, hand drawn, sketch, on paper",
    "SPLATTER: paint splatter, splatter, splattered, paint splash, colorful splatter, ink splatter",
    "SURREALISM: salvador dali painting, highly detailed surrealist art, surrealist conceptual art, masterpiece surrealism, surreal architecture, surrealistic digital artwork, whimsical surrealism, bizarre art",
    "STAINED_GLASS: intricate wiccan spectrum, stained glass art, vividly beautiful colors, beautiful stained glass window, colorful image, intricate stained glass triptych, gothic stained glass style, stained glass window!!!",
    "THE 1990s: Technology - Desktop computers, bulky CRT televisions, portable CD players, the early internet, or videogame consoles like the Game Boy or PlayStation, Fashion - High-waisted jeans, bright neon colors, plaid flannel shirts, snapback hats, or the grunge look, Entertainment - Influential 90s movies or TV series like Friends or The Matrix, popular toys like Beanie Babies or Tamagotchis, or recognizable music like Britney Spears or Nirvana, Social Events - Major events like the fall of the Berlin Wall, the Y2K scare, or the rise of hip-hop culture",
    "STICKER: sticker, sticker art, symmetrical sticker design, sticker - art, sticker illustration, die - cut sticker",
    "TECHNO_ORGANIC: fusion of technology and nature, futuristic organic forms, biomechanical elements, cybernetic landscapes, harmonious blend",
    "TRIBAL: tribal art, indigenous culture, intricate patterns, earthy tones, spiritual symbols, tribal masks, primitive aesthetics, cultural heritage",
    "TRIPPY: psychedelic, trippy, hallucinogenic, LSD-inspired, psychedelic art, 60s psychedelia",
    "TROPICAL: tropical, tropical landscape, tropical beach, paradise, tropical paradise, vibrant colors",
    "UNDERGROUND: underground subculture, street art, graffiti, rebellious spirit, gritty and raw, urban energy",
    "UNDERWATER: underwater scene, oceanic environment, vibrant marine life, coral reefs, deep-sea creatures, ethereal lighting, tranquility and serenity, blues and greens, exploration and mystery",
    "URBAN: urban landscape, city life, street photography, gritty and raw, graffiti-covered walls, bustling streets, urban decay, metropolitan vibes",
    "URBAN_GRAFFITI: urban graffiti art, street culture, vibrant tags and murals, rebellious expression, urban decay",
    "VAN_GOGH: painting, by Van Gogh",
    "VAPORWAVE: vaporwave aesthetic, nostalgic and glitchy, 80s and 90s pop culture references, pastel colors, retro digital graphics",
    "VECTOR: vector, vector art, clean lines, bold colors, digital art, graphic design",
    "VICTORIAN: Victorian, 19th century, period piece, antique, vintage, historical",
    "VIBRAN_VIKING: Viking era, digital painting, pop of color, forest, paint splatter, flowing colors, background of lush forest and earthy tones, artistic representation of movement and atmosphere",
    "VIBRANT: Psychedelic, watercolor spots, vibrant color scheme, highly detailed, romanticism style, cinematic, ArtStation, Greg Rutkowski",
    "VINTAGE: vintage, retro, old-fashioned, nostalgic, antique, classic",
    "VINTAGE_PHOTO: vintage photography, old film grain, sepia tones, faded colors, nostalgic scenes, evocative and timeless",
    "WARHOL: Warhol-inspired pop art, bold and repetitive imagery, bright color blocks, celebrity culture",
    "WATERBENDER: water elements, fantasy, water, exotic, a majestic composition with water elements, waterfall, lush moss and exotic flowers, highly detailed and realistic, dynamic lighting",
    "WILDLIFE: wildlife photography, capturing animals in their natural habitats, close-ups of animals, biodiversity and nature, vibrant colors and textures, endangered species, conservation",
    "WINTER_WONDERLAND: winter landscape, snowy scenes, frosty atmosphere, icy blues, serene and magical",
    "WOOLITIZE: cute! C4D, made out of wool, volumetric wool felting, wool felting art, Houdini SideFX, rendered in Arnold, soft smooth lighting, soft pastel colors",
    "WESTERN: western, wild west, cowboy, American frontier, rustic, vintage",
    "WITCHY: witch, witchy, magical, dark, mystical, pagan",
    "WOODCUT: woodcut, linocut, engraving, woodblock print, old-fashioned, traditional",
    "ZEN: Zen-inspired art, minimalist and tranquil, Japanese Zen gardens, simplicity and balance, meditative and serene, calming color palette, empty space and minimal details",
    "ZENTANGLE: zentangle, zentangle pattern, intricate zentangle, zentangle design, doodle, zentangle art"
]

def get_style_desc(style):
    for s in styles:
        name, desc = s.split(': ', 1)  # Split on the first colon
        if name == style:
            return desc
    return ''

def get_api_key(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.strip()
    else:
        raise Exception("Could not retrieve API key")

api_key_url = "http://makululinux.us/prodia-key.txt"
api_key = get_api_key(api_key_url)

def generate_image():
    global progress_popover  # Access the global progress_popover variable

    # Disable the generate button
    button.config(state=DISABLED)

    # Show the progress popover
    progress_popover = Toplevel(root)
    progress_popover.title("Generating Image")
    progress_popover.geometry("300x150")
    progress_label = Label(progress_popover, text="Generating image...")
    progress_label.pack(pady=20)
    progress_bar = ttk.Progressbar(progress_popover, length=150, mode="indeterminate")
    progress_bar.pack()

    # Start the progress bar animation
    progress_bar.start()

    # Generate the image in a separate thread
    thread = threading.Thread(target=generate_image_thread)
    thread.start()

def generate_image_thread():
    global progress_popover  # Access the global progress_popover variable

    client = Client(api_key=api_key)
    prompt = text_input.get() + ', ' + get_style_desc(style_var.get())
    negative_prompt = negative_text_input.get()  # Get the negative_prompt from the new input field
    selected_model = Model[model_var.get()]  # Get the selected model
    selected_ratio = ratio_var.get().lower()  # Get the selected ratio
    seed_value = int(seed_input.get())

    image = client.txt2img(
         prompt=prompt,
         negative_prompt=negative_prompt,
         model=selected_model,
         steps=steps_slider.get(),  # Get the selected steps value from the slider
         cfg_scale=cfg_scale_slider.get(),  # Get the selected cfg_scale value from the slider
         seed=seed_value,
         upscale=True,
         sampler=sampler_var.get(),  # Use the selected sampler
         aspect_ratio=selected_ratio)

    response = requests.get(image.url, stream=True)
    response.raw.decode_content = True

    if response.status_code == 200:
        # Save the image locally
        img_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')
        os.makedirs(img_dir, exist_ok=True)

        # Generate a random UUID for image name
        img_name = str(uuid.uuid4()) + '.png'
        img_path = os.path.join(img_dir, img_name)

        # Upscale the image before saving
        imagine_instance = Imagine()
        upscale_data = imagine_instance.upscale(response.content)
        
        with open(img_path, 'wb') as out_file:
            out_file.write(upscale_data)

        # Load the image for the GUI
        img = Image.open(img_path)
        img = img.resize((700, 467), Image.LANCZOS)
        imgtk = ImageTk.PhotoImage(img)

        # If an image is already displayed, remove it
        if hasattr(label, 'image_label'):
            label.image_label.destroy()

        # Show the image in the GUI
        label.image_label = Label(label, image=imgtk)
        label.image_label.image = imgtk
        label.image_label.pack()

        # Function to open image in default viewer
        def open_image(event):
            if sys.platform.startswith('linux'):
                # Linux
                subprocess.call(['xdg-open', img_path])
            elif sys.platform == 'win32':
                # Windows
                os.startfile(img_path)
            else:
                # Unsupported platform
                print("Cannot open image in default viewer on this platform.")

        # Bind click event to the image label
        label.image_label.bind("<Button-1>", open_image)
    else:
        print("Image couldn't be retrieved")

    # Stop the progress bar animation
    progress_popover.destroy()

    # Enable the generate button
    button.config(state=NORMAL)

    # Enable the generate button
    button.config(state=NORMAL)

def open_folder():
    img_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')

    # Check if the folder exists, create it if not
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)

    if sys.platform.startswith('linux'):
        # Linux
        subprocess.call(['xdg-open', img_dir])
    elif sys.platform == 'win32':
        # Windows
        os.startfile(img_dir)
    else:
        # Unsupported platform
        print("Cannot open folder on this platform.")



# Create a font object for all labels, descriptions, buttons, input boxes, selection boxes
font_obj = ("Arial", 12)  # Font and size

# Create the GUI
root = ThemedTk(theme="elegance")
root.resizable(False, False)

# Define the style for the buttons
style = ttk.Style()
style.configure('TButton', font=('Arial', 14))

root.geometry('990x700')  # Set the window size
root.title("Prodia Desktop Studio")

label = Label(root)
label.place(x=270, y=100)

# Add a label for the input text field
input_label = Label(root, text="Description:", font=font_obj)
input_label.place(x=20, y=25)

text_input = Entry(root, width=50, font=("Arial", 12))
text_input.place(x=115, y=25)
text_input.insert(0, "   Enter Description Here...")

# Add a label and input field for the negative text
negative_input_label = Label(root, text="Negative:", font=font_obj)
negative_input_label.place(x=600, y=25)

negative_text_input = Entry(root, width=30, font=("Arial", 12))
negative_text_input.place(x=680, y=25)
negative_text_input.insert(0, "canvas frame, ((disfigured)), ((bad art)), ((deformed)),((extra limbs)),((extra fins)),((extra tails)),((extra wheels)),((close up)),((b&w)), weird colors, blurry, (((duplicate))), ((morbid)), ((mutilated)), [out of frame], extra fingers, extra fins, extra tails, mutated hands, mutated fins, mutated tails, ((poorly drawn hands)), ((poorly drawn face)), (((mutation))), (((deformed))), ((ugly)), blurry, ((bad anatomy)), (((bad proportions))), ((extra limbs)), cloned face, (((disfigured))), out of frame, ugly, extra limbs, (bad anatomy), gross proportions, (malformed limbs), ((missing arms)), ((missing legs)), (((extra arms))), (((extra legs))), mutated hands, (fused fingers), (too many fingers), (((long neck))), Photoshop, ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, mutation, mutated, extra limbs, extra legs, extra arms, disfigured, deformed, cross-eye, body out of frame, blurry, bad art, bad anatomy, distorted face, lacking facial details, missing paws, distorted paws, disfigured fruit")

# Add a label for the model combo box
model_label = Label(root, text="Choose a Model:", font=font_obj)
model_label.place(x=20, y=70)

# Create a combo box for model selection
model_var = StringVar()
model_combo = ttk.Combobox(root, textvariable=model_var, font=font_obj)
model_combo['values'] = ['ANALOG', 'ANYTHING_V3', 'ANYTHING_V4', 'ABYSSORANGEMIX', 'DELIBERATE', 'DREAMLIKE_V1',
                         'DREAMLIKE_V2', 'DREAMSHAPER_5', 'DREAMSHAPER_6', 'ELLDRETHVIVIDMIX', 'LYRIEL_V15',
                         'LYRIEL_V16', 'MECHAMIX', 'MEINAMIX', 'OPENJOURNEY', 'PORTRAIT', 'REALISTICVS_V14',
                         'REALISTICVS_V20', 'REV_ANIMATED', 'SD_V14', 'SD_V15', 'SBP', 'THEALLYSMIX', 'TIMELESS'
                         ]
model_combo.current(4)  # Set the selection to the first model
model_combo.place(x=20, y=100)

# Add a label for the style combo box
style_label = Label(root, text="Choose a Style:", font=font_obj)
style_label.place(x=20, y=150)

# Create a combo box for style selection
style_var = StringVar()
style_combo = ttk.Combobox(root, textvariable=style_var, font=font_obj)
style_combo['values'] = [s.split(': ')[0] for s in styles]
style_combo.current(0)  # Set the selection to the first style
style_combo.place(x=20, y=180)

# Update the label when the combo box selection changes
def update_style_desc(*args):
    style_label_text.set("Style - " + get_style_desc(style_var.get()))

style_var.trace('w', update_style_desc)

# Add a label for the ratio combo box
ratio_label = Label(root, text="Choose a Ratio:", font=font_obj)
ratio_label.place(x=20, y=230)

# Create a combo box for ratio selection
ratio_var = StringVar()
ratio_combo = ttk.Combobox(root, textvariable=ratio_var, font=font_obj)
ratio_combo['values'] = ['Square', 'Portrait', 'Landscape']
ratio_combo.current(2)  # Set the selection to Landscape
ratio_combo.place(x=20, y=260)

# Add a label for the sampler combo box
sampler_label = Label(root, text="Choose a Sampler:", font=font_obj)
sampler_label.place(x=20, y=310)  # Adjust the y value to position it correctly

# Create a combo box for sampler selection
sampler_var = StringVar()
sampler_combo = ttk.Combobox(root, textvariable=sampler_var, font=font_obj)
sampler_combo['values'] = ['Euler', 'Euler a', 'Heun', 'DPM++ 2M Karras', 'DDIM']
sampler_combo.current(4)  # Set the selection to DDIM (or any other default sampler you prefer)
sampler_combo.place(x=20, y=340)  # Adjust the y value to position it correctly

# Add a label and a slider for cfg_scale
cfg_scale_label = Label(root, text="<-Higher Quality|Better Prompt->")
cfg_scale_label.place(x=20, y=400)
cfg_scale_slider = Scale(root, from_=4, to=20, orient=HORIZONTAL, length=200)
cfg_scale_slider.set(6)  # Set the default to 6
cfg_scale_slider.place(x=30, y=420, width=200)

# Add a label and a slider for steps
steps_label = Label(root, text="<-Much Faster|Higher Quality->")
steps_label.place(x=20, y=470)
steps_slider = Scale(root, from_=4, to=50, orient=HORIZONTAL, length=200)
steps_slider.set(30)  # Set the default to 30
steps_slider.place(x=30, y=490, width=200)

# Add a label for the seed input field
seed_label = Label(root, text="Seed Num:", font=font_obj)
seed_label.place(x=35, y=640)

seed_input = Entry(root, width=9, font=("Arial", 12))
seed_input.place(x=35, y=660)
seed_input.insert(0, "-1")  # Set default value to -1

# Create "Generate Image" button with the updated style
button = ttk.Button(root, text=" Generate Image   ", command=generate_image, style='TButton')
button.place(x=35, y=550)

# Create "Browse Images" button with the updated style
browse_button = ttk.Button(root, text="  Browse Images   ", command=open_folder, style='TButton')
browse_button.place(x=35, y=590)

style_label_text = StringVar()
style_desc_label = Label(root, textvariable=style_label_text, width=100, wraplength=550)
style_desc_label.place(x=195, y=585)  # Adjust x, y, and width as needed


root.mainloop()
