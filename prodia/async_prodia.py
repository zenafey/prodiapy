from .exceptions import *
from .templates import *
import aiohttp
import asyncio

class AsyncClient:
    def __init__(self, api_key: str = None, delay: int = 0.5):
        if api_key is None:
            raise ClientError(
                "\n\n\nNo API key provided, please get API key from https://app.prodia.com/ and try again\
                \nExample of usage:\n\nclient = prodia.Client(api_key='xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx')")
        self.key = api_key
        self.headers = {
            "accept": "application/json",
            "X-Prodia-Key": api_key
        }
        self.delay = delay

    async def model_list(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(Endpoint.models, headers=self.headers) as response:
                if response.status != 200:
                    error(f"Prodia API returned error({response.status})\nDetails: {response.text}")
                    return {'status': response.status, 'detail': response.text}
                resp_json = await response.json()
                for model in resp_json:
                    print(model)
                return resp_json

    async def sdxl_generate(self, model: str = SdxlModel.BASE_1_0, prompt: str = None,
                            negative_prompt: str = "badly drawn, blurry, low quality", steps: int = 30,
                            cfg_scale: float = 9.5, seed: int = -1, sampler: str = "DDIM"):
        warn('This method is [BETA] and unstable')
        if is_empty_or_whitespace(prompt):
            raise InvalidParameter("\n\n\nPrompt cannot be empty or whitespace")

        payload = {
            "model": model,
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "steps": steps,
            "cfg_scale": cfg_scale,
            "seed": seed,
            "sampler": sampler
        }
        start = asyncio.get_event_loop().time()
        print(f"/sdxl/generate with params: {payload}")

        async with aiohttp.ClientSession() as session:
            async with session.post(Endpoint.sdxlGenerate, json=payload, headers=self.headers) as response:
                if response.status != 200:
                    error(f"Prodia API returned error({response.status})\nDetails: {response.text}")
                    return {'status': response.status, 'detail': response.text}

                response_json = await response.json()
                job_id = response_json['job']

                await asyncio.sleep(self.delay)

                while True:
                    elapsed_time = asyncio.get_event_loop().time() - start
                    print(f"/sdxl/generate time elapsed: {elapsed_time:.2f}", end="\r")
                    async with session.get(Endpoint.retrieve+job_id, headers=self.headers) as response_retrieve:
                        if response_retrieve.status != 200:
                            error(f"Prodia API returned error({response_retrieve.status})\
                            \nDetails: {response_retrieve.text}")
                            return {'status': response_retrieve.status, 'detail': response_retrieve.text}

                        response_retrieve_json = await response_retrieve.json()
                        status = response_retrieve_json['status']

                        if status == "succeeded":
                            print(f"\nImage {job_id} generated!")
                            image_url = response_retrieve_json['imageUrl']
                            return ProdiaResponse(image_url, payload, response_retrieve_json, elapsed_time)
                        elif status == "queued":
                            await asyncio.sleep(self.delay)
                        elif status == "generating":
                            await asyncio.sleep(self.delay)
                        else:
                            failed(f"\nGeneration of {job_id} failed or another error occurred: {status}")
                            return ProdiaFailed

    async def sd_generate(self, model: str = SdModel.SDV1_5, prompt: str = None,
                          negative_prompt: str = "badly drawn, blurry, low quality", steps: int = 30,
                          cfg_scale: float = 9.5, seed: int = -1, upscale: bool = False, sampler: str = "DDIM",
                          aspect_ratio: str = "square"):
        if is_empty_or_whitespace(prompt):
            raise InvalidParameter("\n\n\nPrompt cannot be empty or whitespace")

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
        start = asyncio.get_event_loop().time()
        print(f"/sd/generate with params: {payload}")

        async with aiohttp.ClientSession() as session:
            async with session.post(Endpoint.sdGenerate, json=payload, headers=self.headers) as response:
                if response.status != 200:
                    error(f"Prodia API returned error({response.status})\nDetails: {response.text}")
                    return {'status': response.status, 'detail': response.text}

                response_json = await response.json()
                job_id = response_json['job']

                await asyncio.sleep(self.delay)

                while True:
                    elapsed_time = asyncio.get_event_loop().time() - start
                    print(f"/sd/generate time elapsed: {elapsed_time:.2f}", end="\r")
                    async with session.get(Endpoint.retrieve+job_id, headers=self.headers) as response_retrieve:
                        if response_retrieve.status != 200:
                            error(f"Prodia API returned error({response_retrieve.status})\
                            \nDetails: {response_retrieve.text}")
                            return {'status': response_retrieve.status, 'detail': response_retrieve.text}

                        response_retrieve_json = await response_retrieve.json()
                        status = response_retrieve_json['status']

                        if status == "succeeded":
                            print(f"\nImage {job_id} generated!")
                            image_url = response_retrieve_json['imageUrl']
                            return ProdiaResponse(image_url, payload, response_retrieve_json, elapsed_time)
                        elif status == "queued":
                            await asyncio.sleep(self.delay)
                        elif status == "generating":
                            await asyncio.sleep(self.delay)
                        else:
                            failed(f"\nGeneration of {job_id} failed or another error occurred: {status}")
                            return ProdiaFailed

    async def sd_transform(self, image_url: str = None, model: str = SdModel.SDV1_5, prompt: str = None,
                           negative_prompt: str = "badly drawn, blurry, low quality", steps: int = 30,
                           denoising_strength: float = 0.5, cfg_scale: float = 9.5, seed: int = -1,
                           upscale: bool = False, sampler: str = "DDIM"):
        if is_empty_or_whitespace(prompt):
            raise InvalidParameter("\n\n\nPrompt cannot be empty or whitespace")
        warn("Make sure that you used right url")
        if image_url is None:
            error("image_url not specified")
            return

        payload = {
            "imageUrl": image_url,
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
        start = asyncio.get_event_loop().time()
        print(f"/sd/transform with params:\n{payload}")

        async with aiohttp.ClientSession() as session:
            async with session.post(Endpoint.sdTransform, json=payload, headers=self.headers) as response:
                if response.status != 200:
                    error(f"Prodia API returned error({response.status})\nDetails: {response.text}")
                    return {'status': response.status, 'detail': response.text}

                response_json = await response.json()
                job_id = response_json['job']

                await asyncio.sleep(self.delay)

                while True:
                    elapsed_time = asyncio.get_event_loop().time() - start
                    print(f"/sd/transform time elapsed: {elapsed_time:.2f}", end="\r")
                    async with session.get(Endpoint.retrieve+job_id, headers=self.headers) as response_retrieve:
                        if response_retrieve.status != 200:
                            error(
                                f"\nProdia API returned error({response_retrieve.status})\
                                \nDetails: {response_retrieve.text}")
                            return {'status': response_retrieve.status, 'detail': response_retrieve.text}

                        response_retrieve_json = await response_retrieve.json()
                        status = response_retrieve_json['status']

                        if status == "succeeded":
                            print(f"\nImage {job_id} generated!")
                            image_url = response_retrieve_json['imageUrl']
                            return ProdiaResponse(image_url, payload, response_retrieve_json, elapsed_time)
                        elif status == "queued":
                            await asyncio.sleep(self.delay)
                        elif status == "generating":
                            await asyncio.sleep(self.delay)
                        else:
                            failed(f"\nGeneration of {job_id} failed or another error occurred: {status}")
                            return ProdiaFailed

    async def sd_controlnet(self, image_url: str = None, controlnet_model: str = ControlModels.CANNY,
                            controlnet_module: str = "none", threshold_a: int = 100,
                            threshold_b: int = 200, resize_mode: int = 0, prompt: str = None,
                            negative_prompt: str = "badly drawn, blurry, low quality", steps: int = 30,
                            cfg_scale: float = 9.5, seed: int = -1, sampler: str = "DDIM", width: int = 512,
                            height: int = 512):
        if image_url is None:
            error("image_url not specified")
            return
        if is_empty_or_whitespace(prompt):
            raise InvalidParameter("\n\n\nPrompt cannot be empty or whitespace")

        payload = {
            "imageUrl": image_url,
            "controlnet_model": controlnet_model,
            "controlnet_module": controlnet_module,
            "threshold_a": threshold_a,
            "threshold_b": threshold_b,
            "resize_mode": resize_mode,
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "steps": steps,
            "cfg_scale": cfg_scale,
            "seed": seed,
            "sampler": sampler,
            "height": height,
            "width": width
        }
        start = asyncio.get_event_loop().time()
        print(f"/sd/controlnet with params:\n{payload}")

        async with aiohttp.ClientSession() as session:
            async with session.post(Endpoint.sdControl, json=payload, headers=self.headers) as response:
                if response.status != 200:
                    error(f"Prodia API returned error({response.status})\nDetails: {response.text}")
                    return {'status': response.status, 'detail': response.text}

                response_json = await response.json()
                job_id = response_json['job']

                await asyncio.sleep(self.delay)

                while True:
                    elapsed_time = asyncio.get_event_loop().time() - start
                    print(f"controlnet time elapsed: {elapsed_time:.2f}", end="\r")
                    async with session.get(Endpoint.retrieve+job_id, headers=self.headers) as response_retrieve:
                        if response_retrieve.status != 200:
                            error(
                                f"\nProdia API returned error({response_retrieve.status})\
                                \nDetails: {response_retrieve.text}")
                            return {'status': response_retrieve.status, 'detail': response_retrieve.text}

                        response_retrieve_json = await response_retrieve.json()
                        status = response_retrieve_json['status']

                        if status == "succeeded":
                            print(f"\nImage {job_id} generated!")
                            image_url = response_retrieve_json['imageUrl']
                            return ProdiaResponse(image_url, payload, response_retrieve_json, elapsed_time)
                        elif status == "queued":
                            await asyncio.sleep(self.delay)
                        elif status == "generating":
                            await asyncio.sleep(self.delay)
                        else:
                            failed(f"\nGeneration of {job_id} failed or another error occurred: {status}")
                            return ProdiaFailed
