from .constants import *
from .exceptions import *
from .templates import *
import time
import requests

class Client:
    def __init__(self, api_key: str = None, delay: int = 0.5):
        if api_key is None:
            raise ClientError(
                "\n\n\nNo API key provided, please get API key from https://app.prodia.com/ and try again\nExample of usage:\n\nclient = prodia.Client(api_key='xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx')")
        self.key = api_key
        self.delay = delay

    def model_list(self):
        headers = {
            "accept": "application/json",
            "X-Prodia-Key": self.key
        }
        response = requests.get(Endpoint.models, headers=headers)
        if response.status_code != 200:
            error(f"Prodia API returned error({response.status_code})\nDetails: {response.text}")
            return None
        resp_json = response.json()
        for model in resp_json:
            print(model)
        return resp_json

    def txt2img(self, prompt: str = None,model: str = Model.SD_V15.value[0],
                negative_prompt: str = "badly drawn, blurry, low quality",
                steps: int = 30, cfg_scale: float = 9.5, seed: int = -1, upscale: bool = False,
                sampler: str = "DDIM", aspect_ratio: str = "square"):
        if is_empty_or_whitespace(prompt):
            raise InvalidParameter("Prompt cannot be empty or whitespace")
        if validate_sampler(sampler):
            warn(f"The sampler you used probably does not exist\nYour sampler: {sampler}\nAvailable: {[v.value for v in Sampler]}")
        if validate_model(model):
            warn(f"The model you used probably does not exist, check available models list by using client.model_list()\nYour model: {model}")
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
        start = time.time()
        print(f"txt2img with params: {payload}")

        response = requests.post(Endpoint.txt2img, json=payload, headers=headers_create)
        if response.status_code != 200:
            error(f"Prodia API returned error({response.status_code})\nDetails: {response.text}")
            return None

        response_json = response.json()
        job_id = response_json['job']

        time.sleep(self.delay)

        while True:
            elapsed_time = time.time() - start
            print(f"txt2img time elapsed: {elapsed_time:.2f}", end="\r")
            response_retrieve = requests.get(Endpoint.retrieve.format(job_id), headers=headers_retrieve)
            if response_retrieve.status_code != 200:
                error(f"Prodia API returned error({response_retrieve.status_code})\nDetails: {response_retrieve.text}")
                return None

            response_retrieve_json = response_retrieve.json()
            status = response_retrieve_json['status']

            if status == "succeeded":
                print(f"\nImage {job_id} generated!")
                image_url = response_retrieve_json['imageUrl']
                return ProdiaResponse(image_url, payload, response_retrieve_json, elapsed_time)
            elif status == "queued":
                time.sleep(self.delay)
            elif status == "generating":
                time.sleep(self.delay)
            else:
                failed(f"\nGeneration of {job_id} failed or another error occurred: {status}")
                return ProdiaFailed


    def img2img(self, imageUrl: str = None, model: str = Model.SD_V15.value[0], prompt: str = None,
                negative_prompt: str = "badly drawn, blurry, low quality",
                steps: int = 30, denoising_strength: float = 0.5, cfg_scale: float = 9.5, seed: int = -1,
                upscale: bool = False, sampler: str = "DDIM"):
        if is_empty_or_whitespace(prompt):
            raise InvalidParameter("\n\n\nPrompt cannot be empty or whitespace")
        warn("Make sure that you used right url")
        if imageUrl is None:
            error("imageUrl not specified")
            return
        if validate_sampler(sampler):
            warn(
                f"The sampler you used probably does not exist\nYour sampler: {sampler}\nAvailable: {[v.value for v in Sampler]}")
        if validate_model(model):
            warn(
                f"The model you used probably does not exist, check available models list by using client.model_list()\nYour model: {model}")
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
        headers_retrieve = {
            "accept": "application/json",
            "X-Prodia-Key": self.key
        }
        start = time.time()
        print(f"img2img with params:\n{payload}")

        response = requests.post(Endpoint.img2img, json=payload, headers=headers_create)
        if response.status_code != 200:
            error(f"Prodia API returned error({response.status_code})\nDetails: {response.text}")
            return None

        response_json = response.json()
        job_id = response_json['job']

        time.sleep(self.delay)

        while True:
            elapsed_time = time.time() - start
            print(f"img2img time elapsed: {elapsed_time:.2f}", end="\r")
            response_retrieve = requests.get(Endpoint.retrieve.format(job_id), headers=headers_retrieve)
            if response_retrieve.status_code != 200:
                error(
                    f"\nProdia API returned error({response_retrieve.status_code})\nDetails: {response_retrieve.text}")
                return None

            response_retrieve_json = response_retrieve.json()
            status = response_retrieve_json['status']

            if status == "succeeded":
                print(f"\nImage {job_id} generated!")
                image_url = response_retrieve_json['imageUrl']
                return ProdiaResponse(image_url, payload, response_retrieve_json, elapsed_time)
            elif status == "queued":
                time.sleep(self.delay)
            elif status == "generating":
                time.sleep(self.delay)
            else:
                failed(f"\nGeneration of {job_id} failed or another error occurred: {status}")
                return ProdiaFailed

    def controlnet(self, imageUrl: str = None, model: Model = Model.SD_V15.value[0],
                   controlnet_model: Control = Control.SOFT_EDGE.value[0], prompt: str = None,
                   negative_prompt: str = "badly drawn, blurry, low quality",
                   steps: int = 30, cfg_scale: float = 9.5, seed: int = -1, sampler: str = "DDIM"):
        warn("THIS METHOD IS BETA AND UNSTABLE! USE IT AT YOUR OWN RISK")
        warn("Make sure that you used right url")
        if imageUrl is None:
            error("imageUrl not specified")
            return
        if is_empty_or_whitespace(prompt):
            raise InvalidParameter("\n\n\nPrompt cannot be empty or whitespace")
        if validate_sampler(sampler):
            warn(
                f"The sampler you used probably does not exist\nYour sampler: {sampler}\nAvailable: {[v.value for v in Sampler]}")
        if validate_model(model):
            warn(f"The model you used probably does not exist\nYour model: {model}")
        if validate_control(controlnet_model):
            warn(
                f"The controlnet_model you used probably does not exist, check available models list by using client.model_list()\nYour model: {model}")

        payload = {
            "imageUrl": imageUrl,
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
        start = time.time()
        print(f"controlnet with params:\n{payload}")

        response = requests.post(Endpoint.controlnet, json=payload, headers=headers_create)
        if response.status_code != 200:
            error(f"Prodia API returned error({response.status_code})\nDetails: {response.text}")
            return None

        response_json = response.json()
        job_id = response_json['job']

        time.sleep(self.delay)

        while True:
            elapsed_time = time.time() - start
            print(f"controlnet time elapsed: {elapsed_time:.2f}", end="\r")
            response_retrieve = requests.get(Endpoint.retrieve.format(job_id), headers=headers_retrieve)
            if response_retrieve.status_code != 200:
                error(
                    f"\nProdia API returned error({response_retrieve.status_code})\nDetails: {response_retrieve.text}")
                return None

            response_retrieve_json = response_retrieve.json()
            status = response_retrieve_json['status']

            if status == "succeeded":
                print(f"\nImage {job_id} generated!")
                image_url = response_retrieve_json['imageUrl']
                return ProdiaResponse(image_url, payload, response_retrieve_json, elapsed_time)
            elif status == "queued":
                time.sleep(self.delay)
            elif status == "generating":
                time.sleep(self.delay)
            else:
                failed(f"\nGeneration of {job_id} failed or another error occurred: {status}")
                return ProdiaFailed
