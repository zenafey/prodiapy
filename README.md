# prodiapy
This module makes generation of image by Prodia API easier

[Full Documentation](https://prodiapy.readme.io/)

### Installation 
```
pip install -U prodiapy
```
For using this script you need to get your Prodia api key, you can make it on https://app.prodia.com/api


### Example of txt2img usage
```python
from prodia import Client, Model

client = Client(api_key="YOUR PRODIA API KEY")

image = client.sd_generate(prompt="kittens on cloud", model="Realistic_Vision_V4.0.safetensors [29a7afaa]")
print(image.url)
```
P.S. To see full list of available models: client.model_list()
`image` class attributes:

- url - url of generated image
- payload - used payload
- response - retrieved response
- seed() - function that return seed of generated image
- pnginfo() - function that return a dict with pnginfo of image
- load()/ aload() - function to get image as BytesIO and its async version


# Prodia Desktop Studio
!!WARNING!! Prodia Desktop Studio doesnt support prodiapy 3.6 yet, make sure you are using prodiapy 3.5
```
git clone https://github.com/zenafey/prodiapy
cd prodiapy
python tk_gui.py
```
![image](https://github.com/zenafey/prodiapy/assets/118455214/ff949765-307a-4460-87b9-c1a255f169c9)



Feel free to join out [Discord server](https://discord.gg/PtdHCVysfj) and ask question!

![7eacddcb-3a45-4114-b731-3cd7af9522e1](https://user-images.githubusercontent.com/118455214/233359979-80274381-10dd-4ced-b7fa-d45437ef5bce.png)



