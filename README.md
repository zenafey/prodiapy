# Description
prodiapy is an unofficial lightweight Python package for Prodia Stable Diffusion API

# Installation 
```commandline
pip install -U prodiapy
```

# text2img example

```python
from prodiapy import Prodia

prodia = Prodia(
    api_key="YOUR_PRODIA_KEY"
)

job = prodia.sd.generate(prompt="cat")
result = prodia.wait(job)

print(result.image_url)
```
# Contact
Join our discord to get help with package - https://discord.gg/7NbzdD6qg8