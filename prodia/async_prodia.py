from .constants import *
from .utils import *
from .exceptions import *
import requests
import asyncio
import json


class AsyncClient:
    def __init__(self, api_key: str = None):
        if api_key is None:
            raise ClientError("\n\n\nNo API key provided, please get API key from https://app.prodia.com/ and try again\nExample of usage:\n\nclient = prodia.Client(api_key='xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx')")
        self.key = api_key
        self.base = Endpoint.base

    async def retrieve(self, job_id:str=None):
        if job_id is None:
            error("job_id is required!")
            return
        headers_retrieve = {
            "accept": "application/json",
            "X-Prodia-Key": self.key
        }
        response_retrieve = requests.get(self.base + f"/job/{job_id}", headers=headers_retrieve)
        return response_retrieve.json()

    async def create(self, endpoint, imageUrl:str=None, model:str=Model.REALISTICVS_V14.value[0], controlnet_model:str=Control.CANNY.value[0],
                     prompt:str="Cats in clouds", denoising_strength:float=0.5, negative_prompt:str="badly drawn, blurry, low quality",
                      steps:int=30, cfg_scale:float=9.5, seed:int=-1, upscale:bool=False, sampler:str="DDIM", aspect_ratio:str="square"):
        warn("Validators are turned off in create() method")
        if endpoint == "job":
            payload = {
                "prompt": prompt,
                "model": model,
                "sampler": sampler,
                "negative_prompt": negative_prompt,
                "steps": steps,
                "cfg_scale": cfg_scale,
                "seed": seed,
                "upscale": upscale,
                "aspect_ratio": aspect_ratio
            }
            headers_create = {
                "accept": "application/json",
                "content-type": "application/json",
                "X-Prodia-Key": self.key
            }
            print(f"job created:\n{payload}")
            response = requests.post(self.base + "/job", json=payload, headers=headers_create)
            return response.json()
        elif endpoint == "transform":
            payload = {
                "imageUrl": imageUrl,
                "prompt": prompt,
                "model": model,
                "sampler": sampler,
                "negative_prompt": negative_prompt,
                "steps": steps,
                "cfg_scale": cfg_scale,
                "seed": seed,
                "upscale": upscale,
                "denoising_strength": denoising_strength
            }
            headers_create = {
                "accept": "application/json",
                "content-type": "application/json",
                "X-Prodia-Key": self.key
            }
            print(f"job created:\n{payload}")
            response = requests.post(self.base + "/transform", json=payload, headers=headers_create)
            return response.json()
        elif endpoint == "controlnet":
            payload = {
                "imageUrl": imageUrl,
                "prompt": prompt,
                "model": model,
                "controlnet_model": controlnet_model,
                "sampler": sampler,
                "negative_prompt": negative_prompt,
                "steps": steps,
                "cfg_scale": cfg_scale,
                "seed": seed,
                "upscale": upscale,
                "denoising_strength": denoising_strength
            }
            headers_create = {
                "accept": "application/json",
                "content-type": "application/json",
                "X-Prodia-Key": self.key
            }
            print(f"job created:\n{payload}")
            response = requests.post(self.base + "/controlnet", json=payload, headers=headers_create)
            return response.json()



    async def txt2img(self, model: Model = Model.REALISTICVS_V14, prompt:str=None, negative_prompt:str="badly drawn, blurry, low quality",
                      steps:int=30, cfg_scale:float=9.5, seed:int=-1, upscale:bool=False, sampler: Sampler = Sampler.DDIM, aspect_ratio: Ratio = Ratio.SQUARE):
        if is_empty_or_whitespace(prompt):
            raise InvalidParameter("\n\n\nPrompt cannot be empty or whitespace")
        if validate_ratio(aspect_ratio):
            raise InvalidParameter(f"\n\n\nEntered aspect_ratio isnt valid\nvalid ratios:\n['square', 'portrait', 'landscape'] or [Ratio.SQUARE, Ratio.PORTRAIT, 'Ratio.LANDSCAPE']\nYou provided: {aspect_ratio}")
        if validate_sampler(sampler):
            warn(f"The sampler you used probably does not exist\nYour sampler: {sampler}\nAvailable: {[v.value[0] for v in Sampler]}")
        if validate_model(model):
            warn(f"The model you used probably does not exist\nYour model: {model}")
        if validate_steps(steps):
            raise InvalidParameter(f"\n\n\nSteps must be between 1 and 50\nYour value: {steps}")
        if validate_cfg(cfg_scale):
            raise InvalidParameter(f"\n\n\nCFG scale must be between 1.0 and 20.0\nYour value: {steps}")
        if "bool" not in str(type(upscale)):
            raise InvalidParameter("\n\n\nUpscale value must be boolean:\nTrue, False")
        try:
            model = model.value[0]
        except:
            model = model
        try:
            sampler = sampler.value[0]
        except:
            sampler = sampler
        try:
            aspect_ratio = aspect_ratio.value[0]
        except:
            aspect_ratio = aspect_ratio
        payload = {
            "prompt": prompt,
            "model": model,
            "sampler": sampler,
            "negative_prompt": negative_prompt,
            "steps": steps,
            "cfg_scale": cfg_scale,
            "seed": seed,
            "upscale": upscale,
            "aspect_ratio": aspect_ratio
        }
        headers_create = {
            "accept": "application/json",
            "content-type": "application/json",
            "X-Prodia-Key": self.key
        }
        headers_retrieve = {
            "accept": "application/json",
            "X-Prodia-Key": self.key
        }
        print(f"txt2img with params:\n{payload}")
        response = requests.post(self.base + "/job", json=payload, headers=headers_create)
        try:
            job_id = response.json()['job']
        except Exception as e:
            if response.text == "Invalid Generation Parameters":
                raise InvalidParameter(f"\n\n\nProdia API raise Invalid Generation Parameters error, check payload for None or invalid parameters\n\nResponse:\n\n{response.text}")
            else:
                raise UnknownError(f"\n\n\nProdia API returned unknown error: {e}\n\nResponse:\n\n{response.text}")
        await asyncio.sleep(3)

        working = True
        while working is True:
            response_retrieve = requests.get(self.base +f"/job/{job_id}", headers=headers_retrieve)
            try:
                status = response_retrieve.json()['status']
            except Exception as e:
                if response_retrieve.text == "Invalid Generation Parameters":
                    raise InvalidParameter(
                        f"\n\n\nProdia API raise Invalid Generation Parameters error, check payload for None or invalid parameters\n\nResponse:\n\n{response_retrieve.text}")
                else:
                    raise UnknownError(f"\n\n\nProdia API returned unknown error: {e}\n\nResponse:\n\n{response_retrieve.text}")
            if status == "succeeded":
                print(f"Image {job_id} generated!")
                image_url = response_retrieve.json()['imageUrl']
                class prodia_response:
                    url = image_url
                    seed = get_seed(image_url)
                    pnginfo = get_pnginfo(image_url)
                return prodia_response
            elif status == "queued":
                print("Still working...")
                await asyncio.sleep(2)
            elif status == "generating":
                print("Still working...")
                await asyncio.sleep(2)
            else:
                failed(f"Generation of {job_id} failed or another error occurred: {status}")
                return status
    async def img2img(self, imageUrl:str=None, model: Model = Model.REALISTICVS_V14, prompt:str=None, negative_prompt:str="badly drawn, blurry, low quality",
                      steps:int=30, denoising_strength:float=0.5, cfg_scale:float=9.5, seed:int=-1, upscale:bool=False, sampler: Sampler = Sampler.DDIM):
        if is_empty_or_whitespace(prompt):
            raise InvalidParameter("\n\n\nPrompt cannot be empty or whitespace")
        if imageUrl is None:
            error("imageUrl not specified")
            return
        if validate_sampler(sampler):
            warn(f"The sampler you used probably does not exist\nYour sampler: {sampler}\nAvailable: {[v.value[0] for v in Sampler]}")
        if validate_model(model):
            warn(f"The model you used probably does not exist\nYour model: {model}")
        if validate_steps(steps):
            raise InvalidParameter(f"\n\n\nSteps must be between 1 and 50\nYour value: {steps}")
        if validate_cfg(cfg_scale):
            raise InvalidParameter(f"\n\n\nCFG scale must be between 1.0 and 20.0\nYour value: {steps}")
        if validate_denoise(denoising_strength):
            raise InvalidParameter(f"\n\n\nCFG scale must be between 0.1 and 0.9\nYour value: {steps}")
        if "bool" not in str(type(upscale)):
            raise InvalidParameter("\n\n\nUpscale value must be boolean:\nTrue, False")
        try:
            model = model.value[0]
        except:
            model = model
        try:
            sampler = sampler.value[0]
        except:
            sampler = sampler
        payload = {
            "imageUrl":imageUrl,
            "prompt": prompt,
            "model": model,
            "sampler": sampler,
            "negative_prompt": negative_prompt,
            "steps": steps,
            "cfg_scale": cfg_scale,
            "seed": seed,
            "upscale": upscale,
            "denoising_strength":denoising_strength
        }
        headers_create = {
            "accept": "application/json",
            "content-type": "application/json",
            "X-Prodia-Key": self.key
        }
        headers_retrieve = {
            "accept": "application/json",
            "X-Prodia-Key": self.key
        }
        print(f"img2img with params:\n{payload}")
        response = requests.post(self.base + "/transform", json=payload, headers=headers_create)
        try:
            job_id = response.json()['job']
        except Exception as e:
            if response.text == "Invalid Generation Parameters":
                raise InvalidParameter(f"\n\n\nProdia API raise Invalid Generation Parameters error, check payload for None or invalid parameters\n\nResponse:\n\n{response.text}")
            else:
                raise UnknownError(f"\n\n\nProdia API returned unknown error: {e}\n\nResponse:\n\n{response.text}")
        await asyncio.sleep(3)

        working = True
        while working is True:
            response_retrieve = requests.get(self.base +f"/job/{job_id}", headers=headers_retrieve)
            try:
                status = response_retrieve.json()['status']
            except Exception as e:
                if response_retrieve.text == "Invalid Generation Parameters":
                    raise InvalidParameter(
                        f"\n\n\nProdia API raise Invalid Generation Parameters error, check payload for None or invalid parameters\n\nResponse:\n\n{response_retrieve.text}")
                else:
                    raise UnknownError(f"\n\n\nProdia API returned unknown error: {e}\n\nResponse:\n\n{response_retrieve.text}")
            if status == "succeeded":
                print(f"Image {job_id} generated!")
                image_url = response_retrieve.json()['imageUrl']
                class prodia_response:
                    url = image_url
                    seed = get_seed(image_url)
                    pnginfo = get_pnginfo(image_url)
                return prodia_response
            elif status == "queued":
                print("Still working...")
                await asyncio.sleep(2)
            elif status == "generating":
                print("Still working...")
                await asyncio.sleep(2)
            else:
                failed(f"Generation of {job_id} failed or another error occurred: {status}")
                return status

    async def controlnet(self, imageUrl:str=None, model: Model = Model.REALISTICVS_V14, controlnet_model: Control = Control.CANNY, prompt:str=None, negative_prompt:str="badly drawn, blurry, low quality",
                      steps:int=30, cfg_scale:float=9.5, seed:int=-1, sampler: Sampler = Sampler.DDIM):
        warn("THIS METHOD IS BETA AND UNSTABLE! USE IT AT YOUR OWN RISK")
        warn("Make sure that you used right url")
        if imageUrl is None:
            error("imageUrl not specified")
            return
        if is_empty_or_whitespace(prompt):
            raise InvalidParameter("\n\n\nPrompt cannot be empty or whitespace")
        if validate_sampler(sampler):
            warn(f"The sampler you used probably does not exist\nYour sampler: {sampler}\nAvailable: {[v.value[0] for v in Sampler]}")
        if validate_model(model):
            warn(f"The model you used probably does not exist\nYour model: {model}")
        if validate_control(controlnet_model):
            warn(f"The controlnet_model you used probably does not exist\nYour model: {model}")
        if validate_steps(steps):
            raise InvalidParameter(f"\n\n\nSteps must be between 1 and 50\nYour value: {steps}")
        if validate_cfg(cfg_scale):
            raise InvalidParameter(f"\n\n\nCFG scale must be between 1.0 and 20.0\nYour value: {steps}")
        try:
            model = model.value[0]
        except:
            model = model
        try:
            controlnet_model = controlnet_model.value[0]
        except:
            controlnet_model = controlnet_model
        try:
            sampler = sampler.value[0]
        except:
            sampler = sampler
        payload = {
            "imageUrl":imageUrl,
            "prompt": prompt,
            "model": model,
            "controlnet_model": controlnet_model,
            "sampler": sampler,
            "negative_prompt": negative_prompt,
            "steps": steps,
            "cfg_scale": cfg_scale,
            "seed": seed
        }
        headers_create = {
            "accept": "application/json",
            "content-type": "application/json",
            "X-Prodia-Key": self.key
        }
        headers_retrieve = {
            "accept": "application/json",
            "X-Prodia-Key": self.key
        }
        print(f"controlnet with params:\n{payload}")
        response = requests.post(self.base + "/controlnet", json=payload, headers=headers_create)
        try:
            job_id = response.json()['job']
        except Exception as e:
            if response.text == "Invalid Generation Parameters":
                raise InvalidParameter(f"\n\n\nProdia API raise Invalid Generation Parameters error, check payload for None or invalid parameters\n\nResponse:\n\n{response.text}")
            else:
                raise UnknownError(f"\n\n\nProdia API returned unknown error: {e}\n\nResponse:\n\n{response.text}")
        await asyncio.sleep(3)

        working = True
        while working is True:
            response_retrieve = requests.get(self.base +f"/job/{job_id}", headers=headers_retrieve)
            try:
                status = response_retrieve.json()['status']
            except Exception as e:
                if response_retrieve.text == "Invalid Generation Parameters":
                    raise InvalidParameter(
                        f"\n\n\nProdia API raise Invalid Generation Parameters error, check payload for None or invalid parameters\n\nResponse:\n\n{response_retrieve.text}")
                else:
                    raise UnknownError(f"\n\n\nProdia API returned unknown error: {e}\n\nResponse:\n\n{response_retrieve.text}")
            if status == "succeeded":
                print(f"Image {job_id} generated!")
                image_url = response_retrieve.json()['imageUrl']
                class prodia_response:
                    url = image_url
                    seed = get_seed(image_url)
                    pnginfo = get_pnginfo(image_url)
                return prodia_response
            elif status == "queued":
                print("Still working...")
                await asyncio.sleep(2)
            elif status == "generating":
                print("Still working...")
                await asyncio.sleep(2)
            else:
                failed(f"Generation of {job_id} failed or another error occurred: {status}")
                return status
