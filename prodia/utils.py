import re
import requests
from PIL import Image
from io import BytesIO
from colorama import Fore, init, Style
from .constants import * #######

def get_pnginfo(imageurl):
    response = requests.get(imageurl)
    targetImage = Image.open(BytesIO(response.content))
    try:
        metadata = targetImage.text
        data = {key: value for key, value in metadata.items()}
    except AttributeError:
        data = "Sorry, there is no pnginfo in this image"
    return data

def get_seed(image_url):
    string = requests.get(image_url)
    pattern = r'Seed: (\d+)'
    match = re.search(pattern, str(string.content[:4000]))
    if match:
        return match.group(1)
    else:
        return None

def save_image(image, path="./out0.png"):
    response = requests.get(image)
    with open(path, 'wb') as f:
        f.write(response.content)

def is_empty_or_whitespace(s):
    if s is None:
        return True
    return all(c.isspace() for c in s)

def validate_ratio(ratio):
    if ratio not in [ratio for ratio in Ratio] and ratio not in [ratio.value[0] for ratio in Ratio]:
        return True
    else:
        return False

def validate_sampler(sampler):
    if sampler not in [v for v in Sampler] and sampler not in [v.value[0] for v in Sampler]:
        return True
    else:
        return False

def validate_model(model):
    if model not in [v for v in Model] and model not in [v.value[0] for v in Model]:
        return True
    else:
        return False

def validate_control(model):
    if model not in [v for v in Control] and model not in [v.value[0] for v in Control]:
        return True
    else:
        return False


def validate_steps(steps):
    if steps < 1 or steps > 50:
        return True
    else:
        return False

def validate_cfg(cfg_scale):
    if cfg_scale < 1.0 or cfg_scale > 20.0:
        return True
    else:
        return False

def validate_denoise(ds):
    if ds < 0.1 or ds > 0.9:
        return True
    else:
        return False

def error(msg):
    print(Fore.RED + f"ERROR: {msg}" + Fore.RESET)

def warn(msg):
    print(Fore.YELLOW + f"WARNING: {msg}" + Fore.RESET)

def failed(msg):
    print(Fore.RED + f"FAILED: {msg}" + Fore.RESET)

def models():
    for model in Model:
        print(f"{model.value[0]} - {model.value[1]} - {model.value[2]}")

def controlnet_models():
    for model in Control:
        print(f"{model.value[0]} - {model.value[1]} - {model.value[2]}")

def samplers():
    for sampler in Sampler:
        print(f"{sampler.value[0]} - {sampler.value[1]}")

