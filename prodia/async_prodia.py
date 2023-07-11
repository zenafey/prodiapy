from .constants import *
from .utils import *
from .exceptions import *
from .templates import *
import aiohttp
import asyncio
import time


class AsyncClient:
    def __init__(self, api_key: str = None, delay: int = 1):
        if api_key is None:
            raise ClientError(
                "\n\n\nNo API key provided, please get API key from https://app.prodia.com/ and try again\nExample of usage:\n\nclient = prodia.Client(api_key='xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx')")
        self.key = api_key
        self.base = Endpoint.base
        self.delay = delay

    async def txt2img(self, model: str = Model.SD_V15.value[0], prompt: str = None,
                      negative_prompt: str = "badly drawn, blurry, low quality",
                      steps: int = 30, cfg_scale: float = 9.5, seed: int = -1, upscale: bool = False,
                      sampler: str = "DDIM", aspect_ratio: str = "square"):
        if is_empty_or_whitespace(prompt):
            raise InvalidParameter("\n\n\nPrompt cannot be empty or whitespace")
        if validate_ratio(aspect_ratio):
            raise InvalidParameter(
                f"\n\n\nEntered aspect_ratio isnt valid\nvalid ratios:\n['square', 'portrait', 'landscape']\nYou provided: {aspect_ratio}")
        if validate_sampler(sampler):
            warn(
                f"The sampler you used probably does not exist\nYour sampler: {sampler}\nAvailable: {[v.value[0] for v in Sampler]}")
        if validate_model(model):
            warn(f"The model you used probably does not exist\nYour model: {model}")
        if validate_steps(steps):
            raise InvalidParameter(f"\n\n\nsteps must be between 1 and 50\nYour value: {steps}")
        if validate_cfg(cfg_scale):
            raise InvalidParameter(f"\n\n\ncfg_scale must be between 1.0 and 20.0\nYour value: {cfg_scale}")
        if "bool" not in str(type(upscale)):
            raise InvalidParameter("\n\n\nupscale value must be boolean:\nTrue, False")
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
        start_time = time.time()
        print(f"txt2img with params: {payload}")

        async with aiohttp.ClientSession() as session:
            async with session.post(self.base+"/job", json=payload, headers=headers_create) as response:
                try:
                    response_json = await response.json()
                    job_id = response_json['job']
                except Exception as e:
                    if response.status == 400:
                        raise InvalidParameter(
                            f"\n\n\nProdia API raised Invalid Generation Parameters error(400), check payload for None or invalid parameters\n\nResponse:\n\n{response.text}")
                    else:
                        raise UnknownError(
                            f"\n\n\nProdia API returned unknown error: {e}\n\nResponse:\n\n{response.text}")

                await asyncio.sleep(self.delay)

                while True:
                    elapsed_time = time.time() - start_time
                    print(f"txt2img time elapsed: {elapsed_time:.2f}", end="\r")
                    async with session.get(self.base + f"/job/{job_id}", headers=headers_retrieve) as response_retrieve:
                        try:
                            response_retrieve_json = await response_retrieve.json()
                            status = response_retrieve_json['status']
                        except Exception as e:
                            if response_retrieve.text == "Invalid Generation Parameters":
                                raise InvalidParameter(
                                    f"\n\n\nProdia API raise Invalid Generation Parameters error, check payload for None or invalid parameters\n\nResponse:\n\n{response_retrieve.text}")
                            else:
                                raise UnknownError(f"\n\n\nProdia API returned unknown error: {e}\n\nResponse:\n\n{response_retrieve.text}")
                        if status == "succeeded":
                            print(f"\nImage {job_id} generated!")
                            image_url = response_retrieve_json['imageUrl']
                            return ProdiaResponse(image_url, payload, response_retrieve_json)
                        elif status == "queued":
                            await asyncio.sleep(self.delay)
                        elif status == "generating":
                            await asyncio.sleep(self.delay)
                        else:
                            failed(f"\nGeneration of {job_id} failed or another error occurred: {status}")
                            return status
    async def img2img(self, imageUrl:str=None, model: str = Model.SD_V15.value[0], prompt:str=None, negative_prompt:str="badly drawn, blurry, low quality",
                      steps:int=30, denoising_strength:float=0.5, cfg_scale:float=9.5, seed:int=-1, upscale:bool=False, sampler: str = "DDIM"):
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
            raise InvalidParameter(f"\n\n\nCFG scale must be between 1.0 and 20.0\nYour value: {cfg_scale}")
        if validate_denoise(denoising_strength):
            raise InvalidParameter(f"\n\n\nDenoising Strength must be between 0.1 and 0.9\nYour value: {denoising_strength}")
        if "bool" not in str(type(upscale)):
            raise InvalidParameter("\n\n\nUpscale value must be boolean:\nTrue, False")
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
        start_time = time.time()
        print(f"img2img with params:\n{payload}")

        async with aiohttp.ClientSession() as session:
            async with session.post(self.base+"/transform", json=payload, headers=headers_create) as response:
                try:
                    response_json = await response.json()
                    job_id = response_json['job']
                except Exception as e:
                    if response.status == 400:
                        raise InvalidParameter(
                            f"\n\n\nProdia API raised Invalid Generation Parameters error(400), check payload for None or invalid parameters\n\nResponse:\n\n{response.text}")
                    else:
                        raise UnknownError(
                            f"\n\n\nProdia API returned unknown error: {e}\n\nResponse:\n\n{response.text}")

                await asyncio.sleep(self.delay)

                while True:
                    elapsed_time = time.time() - start_time
                    print(f"img2img time elapsed: {elapsed_time:.2f}", end="\r")
                    async with session.get(self.base + f"/job/{job_id}", headers=headers_retrieve) as response_retrieve:
                        try:
                            response_retrieve_json = await response_retrieve.json()
                            status = response_retrieve_json['status']
                        except Exception as e:
                            if response_retrieve.text == "Invalid Generation Parameters":
                                raise InvalidParameter(
                                    f"\n\n\nProdia API raise Invalid Generation Parameters error, check payload for None or invalid parameters\n\nResponse:\n\n{response_retrieve.text}")
                            else:
                                raise UnknownError(
                                    f"\n\n\nProdia API returned unknown error: {e}\n\nResponse:\n\n{response_retrieve.text}")
                        if status == "succeeded":
                            print(f"\nImage {job_id} generated!")
                            image_url = response_retrieve_json['imageUrl']
                            return ProdiaResponse(image_url, payload, response_retrieve_json)
                        elif status == "queued":
                            await asyncio.sleep(self.delay)
                        elif status == "generating":
                            await asyncio.sleep(self.delay)
                        else:
                            failed(f"\nGeneration of {job_id} failed or another error occurred: {status}")
                            return status


        ###DEPRECATED###

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
