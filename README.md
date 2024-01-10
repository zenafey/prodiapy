# Description
prodiapy is an unofficial lightweight Python package for [Prodia Stable Diffusion API](https://docs.prodia.com/reference/getting-started)

# Installation 
```commandline
pip install prodiapy==5.0a1
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