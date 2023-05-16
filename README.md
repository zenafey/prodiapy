# prodia-python
This module makes generation of image by Prodia API easier

### Installation 
```
pip install prodiapy==2.4
```
For using this script you need to get your Prodia api key, you can make it on https://app.prodia.com/api


### Example of txt2img usage
```python
import prodia

key = "your-prodia-key"

prodia.Client(api_key=key)

image = prodia.txt2img(prompt="kittens on cloud", model="dreamlike-diffusion-2.0.safetensors [fdcf65e7]")
print(image)
```
`image` variable will be a url of your image

### Example of img2img usage
```python
import prodia

key = 'your-prodia-key'

prodia.Client(api_key=key)

image_url = 'https://images.prodia.xyz/a77bfbb2-4808-4178-8bed-eed51077a476.png' #here should be url of your image

image = prodia.img2img(imageUrl=image_url, prompt="winter nature wallpaper")

print(image)
```

### Asynchronous usage
```py
import prodia
import asyncio
prodia.Client(api_key='your-api-key')

async def test():
#...
    text2image = await prodia.arunv1(prompt="clouds")
    image2image = await prodia.arunv2(imageUrl="here-url", prompt="clouds")
    print(text2image, image2image)

asyncio.run(test)
```

### Additional info

All available arguments for txt2img():
- prompt:str(required)
- negative_prompt:str
- model:str check all available models on https://docs.prodia.com/reference/generate
- sampler:str check all available samplers on https://docs.prodia.com/reference/generate
- steps:int from 1 to 50
- cfg_scale:int from 1 to 20
- seed:int leave blank for random(or use -1 for random)
- upscale:bool Enable/Disable 2x upscaling of image
- aspect_ratio:str available: "square", "landscape", "portrait"

All available arguments for img2img():
- imageUrl:str(required)
- model:str check all available models on https://docs.prodia.com/reference/generate
- sampler:str check all available samplers on https://docs.prodia.com/reference/generate
- prompt:str(required)
- denoising_strength:float default is 0.7
- negative_prompt:str
- steps:int from 1 to 50
- cfg_scale:int from 1 to 20
- seed:int leave blank for random(or use -1 for random)
- upscale:bool Enable/Disable 2x upscaling of image

Feel free to join out [Discord server](https://discord.gg/eAcrtqaE) and ask question!

![7eacddcb-3a45-4114-b731-3cd7af9522e1](https://user-images.githubusercontent.com/118455214/233359979-80274381-10dd-4ced-b7fa-d45437ef5bce.png)

