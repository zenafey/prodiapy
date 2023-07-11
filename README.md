# prodiapy
This module makes generation of image by Prodia API easier

### Installation 
```
pip install prodiapy==3.4
```
For using this script you need to get your Prodia api key, you can make it on https://app.prodia.com/api


### Example of txt2img usage
```python
import prodia

key = "your-prodia-key"

client = prodia.Client(api_key=key)

image = client.txt2img(prompt="kittens on cloud", model="dreamlike-diffusion-2.0.safetensors [fdcf65e7]")
print(image.url)
```
`image` variable will be a class with attributes:

- url - url of generated image
- payload - used payload
- response - retrieved response
- seed() - function that return seed of generated image
- pnginfo() - function that return a dict with pnginfo of image



# HuggingFace Demo

https://huggingface.co/spaces/zenafey/prodia

![image](https://github.com/zenafey/prodiapy/assets/118455214/4692d825-1d9f-4e4e-a041-40b0e31dc96e)


# Prodia Desktop Studio
```
git clone https://github.com/zenafey/prodiapy
cd prodiapy
python tk_gui.py
```
![image](https://github.com/zenafey/prodiapy/assets/118455214/ff949765-307a-4460-87b9-c1a255f169c9)


[Full Documentation](https://prodiapy.readme.io/)

Feel free to join out [Discord server](https://discord.gg/PtdHCVysfj) and ask question!

![7eacddcb-3a45-4114-b731-3cd7af9522e1](https://user-images.githubusercontent.com/118455214/233359979-80274381-10dd-4ced-b7fa-d45437ef5bce.png)



