# prodiapy 
This module makes generation of image by Prodia API easier

[Full Documentation](https://prodiapy.readme.io/) 

### Installation 
```
pip install prodiapy -U
```
For using this script you need to get your Prodia api key, you can make it on https://app.prodia.com/api


### Example of txt2img usage
```python
from prodiapy import StableDiffusionXL

pipe = StableDiffusionXL(
    api_key="YOUR_PRODIA_KEY"
)

job = pipe.generate(prompt="cat")
result = pipe.wait_for(job)

print(result['imageUrl'])
```

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



