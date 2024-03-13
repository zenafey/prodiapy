from __future__ import annotations

from prodiapy.resources.engine import APIResource
from typing import Union, Optional, Literal
from prodiapy.resources.utils import form_body


class StableDiffusionGeneral(APIResource):
    def __init__(self, client, model_architecture="sd") -> None:
        super().__init__(client)
        self.model_architecture = model_architecture

    def generate(
            self,
            model: Optional[str] = None,
            prompt: Optional[str] = None,
            negative_prompt: Optional[str] = None,
            style_preset: Optional[str] = None,
            steps: Optional[int] = None,
            cfg_scale: Optional[int | float] = None,
            seed: Optional[int] = None,
            sampler: Optional[str] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            dict_parameters: Optional[dict] = None,
            **kwargs
    ) -> dict:
        """
        text2image generation, sources:
https://docs.prodia.com/reference/generate for StableDiffusion
https://docs.prodia.com/reference/sdxl-generate for StableDiffusionXL

        Returns:
            Python dictionary containing job id

        """
        return self._post(
            f"/{self.model_architecture}/generate",
            body=form_body(
                dict_parameters=dict_parameters,
                model=model,
                prompt=prompt,
                negative_prompt=negative_prompt,
                style_preset=style_preset,
                steps=steps,
                cfg_scale=cfg_scale,
                seed=seed,
                sampler=sampler,
                width=width,
                height=height,
                **kwargs
            )
        )

    def transform(
            self,
            image_url: Optional[str] = None,
            image_data: Optional[str] = None,
            model: Optional[str] = None,
            prompt: Optional[str] = None,
            denoising_strength: Optional[float] = None,
            negative_prompt: Optional[str] = None,
            style_preset: Optional[str] = None,
            steps: Optional[int] = None,
            cfg_scale: Optional[int | float] = None,
            seed: Optional[int] = None,
            sampler: Optional[str] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            dict_parameters: Optional[dict] = None,
            **kwargs
    ) -> dict:
        """
        image2image generation, sources:
https://docs.prodia.com/reference/transform for StableDiffusion
https://docs.prodia.com/reference/sdxl-transform for StableDiffusionXL

        Returns:
            Python dictionary containing job id

        """
        return self._post(
            f"/{self.model_architecture}/transform",
            body=form_body(
                dict_parameters=dict_parameters,
                imageUrl=image_url,
                imageData=image_data,
                model=model,
                prompt=prompt,
                denoising_strength=denoising_strength,
                negative_prompt=negative_prompt,
                style_preset=style_preset,
                steps=steps,
                cfg_scale=cfg_scale,
                seed=seed,
                sampler=sampler,
                width=width,
                height=height,
                **kwargs
            )
        )

    def inpainting(
            self,
            image_url: Optional[str] = None,
            image_data: Optional[str] = None,
            mask_url: Optional[str] = None,
            mask_data: Optional[str] = None,
            model: Optional[str] = None,
            prompt: Optional[str] = None,
            denoising_strength: Optional[float] = None,
            negative_prompt: Optional[str] = None,
            style_preset: Optional[str] = None,
            steps: Optional[int] = None,
            cfg_scale: Optional[int | float] = None,
            seed: Optional[int] = None,
            mask_blur: Optional[int] = None,
            inpainting_fill: Optional[Union[int, Literal[0, 1, 2, 3]]] = None,
            inpainting_mask_invert: Optional[Union[int, Literal[0, 1]]] = None,
            inpainting_full_res: Optional[bool] = None,
            sampler: Optional[str] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            dict_parameters: Optional[dict] = None,
            **kwargs
    ) -> dict:
        """
        Controlled image2image generation, sources:
https://docs.prodia.com/reference/inpainting for StableDiffusion
https://docs.prodia.com/reference/sdxl-inpainting for StableDiffusionXL

        Returns:
            Python dictionary containing job id

        """
        return self._post(
            f"/{self.model_architecture}/inpainting",
            body=form_body(
                dict_parameters=dict_parameters,
                imageUrl=image_url,
                imageData=image_data,
                maskUrl=mask_url,
                maskData=mask_data,
                model=model,
                prompt=prompt,
                denoising_strength=denoising_strength,
                negative_prompt=negative_prompt,
                style_preset=style_preset,
                steps=steps,
                cfg_scale=cfg_scale,
                seed=seed,
                mask_blur=mask_blur,
                inpainting_fill=inpainting_fill,
                inpainting_mask_invert=inpainting_mask_invert,
                inpainting_full_res=inpainting_full_res,
                sampler=sampler,
                width=width,
                height=height,
                **kwargs
            )
        )

    def models(self) -> list:
        """
        Actual list of available models, sources:
https://docs.prodia.com/reference/listmodels for StableDiffusion
https://docs.prodia.com/reference/listsdxlmodels for StableDiffusionXL

        Returns:
            Python list containing string names of available models
        """
        return self._get(f"/{self.model_architecture}/models")

    def samplers(self) -> list:
        """
        Actual list of available samplers, sources:
https://docs.prodia.com/reference/listsamplers for StableDiffusion
https://docs.prodia.com/reference/listsdxlsamplers for StableDiffusionXL

        Returns:
             Python list containing string names of available samplers
        """
        return self._get(f"/{self.model_architecture}/samplers")

    def loras(self) -> list:
        """
        Actual list of available LoRa models, sources:
https://docs.prodia.com/reference/listloras for StableDiffusion
https://docs.prodia.com/reference/listsdxlloras for StableDiffusionXL

        Returns:
             Python list containing string names of available LoRa models
        """
        return self._get(f"/{self.model_architecture}/loras")

    def embeddings(self) -> list:
        """
        Actual list of available embedding models, sources:
https://docs.prodia.com/reference/listembeddings for StableDiffusion
https://docs.prodia.com/reference/listsdxlembeddings for StableDiffusionXL

        Returns:
             Python list containing string names of available embedding models
        """
        return self._get(f"/{self.model_architecture}/embeddings")


class AsyncStableDiffusionGeneral(APIResource):
    def __init__(self, client, model_architecture="sd") -> None:
        super().__init__(client)
        self.model_architecture = model_architecture

    async def generate(
            self,
            model: Optional[str] = None,
            prompt: Optional[str] = None,
            negative_prompt: Optional[str] = None,
            style_preset: Optional[str] = None,
            steps: Optional[int] = None,
            cfg_scale: Optional[int | float] = None,
            seed: Optional[int] = None,
            sampler: Optional[str] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            dict_parameters: Optional[dict] = None,
            **kwargs
    ) -> dict:
        """
        text2image generation, sources:
https://docs.prodia.com/reference/generate for StableDiffusion
https://docs.prodia.com/reference/sdxl-generate for StableDiffusionXL

        Returns:
            Python dictionary containing job id

        """
        return await self._post(
            f"/{self.model_architecture}/generate",
            body=form_body(
                dict_parameters=dict_parameters,
                model=model,
                prompt=prompt,
                negative_prompt=negative_prompt,
                style_preset=style_preset,
                steps=steps,
                cfg_scale=cfg_scale,
                seed=seed,
                sampler=sampler,
                width=width,
                height=height,
                **kwargs
            )
        )

    async def transform(
            self,
            image_url: Optional[str] = None,
            image_data: Optional[str] = None,
            model: Optional[str] = None,
            prompt: Optional[str] = None,
            denoising_strength: Optional[float] = None,
            negative_prompt: Optional[str] = None,
            style_preset: Optional[str] = None,
            steps: Optional[int] = None,
            cfg_scale: Optional[int | float] = None,
            seed: Optional[int] = None,
            sampler: Optional[str] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            dict_parameters: Optional[dict] = None,
            **kwargs
    ) -> dict:
        """
        image2image generation, sources:
https://docs.prodia.com/reference/transform for StableDiffusion
https://docs.prodia.com/reference/sdxl-transform for StableDiffusionXL

        Returns:
            Python dictionary containing job id

        """
        return await self._post(
            f"/{self.model_architecture}/transform",
            body=form_body(
                dict_parameters=dict_parameters,
                imageUrl=image_url,
                imageData=image_data,
                model=model,
                prompt=prompt,
                denoising_strength=denoising_strength,
                negative_prompt=negative_prompt,
                style_preset=style_preset,
                steps=steps,
                cfg_scale=cfg_scale,
                seed=seed,
                sampler=sampler,
                width=width,
                height=height,
                **kwargs
            )
        )

    async def inpainting(
            self,
            image_url: Optional[str] = None,
            image_data: Optional[str] = None,
            mask_url: Optional[str] = None,
            mask_data: Optional[str] = None,
            model: Optional[str] = None,
            prompt: Optional[str] = None,
            denoising_strength: Optional[float] = None,
            negative_prompt: Optional[str] = None,
            style_preset: Optional[str] = None,
            steps: Optional[int] = None,
            cfg_scale: Optional[int | float] = None,
            seed: Optional[int] = None,
            mask_blur: Optional[int] = None,
            inpainting_fill: Optional[Union[int, Literal[0, 1, 2, 3]]] = None,
            inpainting_mask_invert: Optional[Union[int, Literal[0, 1]]] = None,
            inpainting_full_res: Optional[bool] = None,
            sampler: Optional[str] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            dict_parameters: Optional[dict] = None,
            **kwargs
    ) -> dict:
        """
        Controlled image2image generation, sources:
https://docs.prodia.com/reference/inpainting for StableDiffusion
https://docs.prodia.com/reference/sdxl-inpainting for StableDiffusionXL

        Returns:
            Python dictionary containing job id

        """
        return await self._post(
            f"/{self.model_architecture}/inpainting",
            body=form_body(
                dict_parameters=dict_parameters,
                imageUrl=image_url,
                imageData=image_data,
                maskUrl=mask_url,
                maskData=mask_data,
                model=model,
                prompt=prompt,
                denoising_strength=denoising_strength,
                negative_prompt=negative_prompt,
                style_preset=style_preset,
                steps=steps,
                cfg_scale=cfg_scale,
                seed=seed,
                mask_blur=mask_blur,
                inpainting_fill=inpainting_fill,
                inpainting_mask_invert=inpainting_mask_invert,
                inpainting_full_res=inpainting_full_res,
                sampler=sampler,
                width=width,
                height=height,
                **kwargs
            )
        )

    async def models(self) -> list:
        """
        Actual list of available models, sources:
https://docs.prodia.com/reference/listmodels for StableDiffusion
https://docs.prodia.com/reference/listsdxlmodels for StableDiffusionXL

        Returns:
            Python list containing string names of available models
        """
        return await self._get(f"/{self.model_architecture}/models")

    async def samplers(self) -> list:
        """
        Actual list of available samplers, sources:
https://docs.prodia.com/reference/listsamplers for StableDiffusion
https://docs.prodia.com/reference/listsdxlsamplers for StableDiffusionXL

        Returns:
             Python list containing string names of available samplers
        """
        return await self._get(f"/{self.model_architecture}/samplers")

    async def loras(self) -> list:
        """
        Actual list of available LoRa models, sources:
https://docs.prodia.com/reference/listloras for StableDiffusion
https://docs.prodia.com/reference/listsdxlloras for StableDiffusionXL

        Returns:
             Python list containing string names of available LoRa models
        """
        return await self._get(f"/{self.model_architecture}/loras")

    async def embeddings(self) -> list:
        """
        Actual list of available embedding models, sources:
https://docs.prodia.com/reference/listembeddings for StableDiffusion
https://docs.prodia.com/reference/listsdxlembeddings for StableDiffusionXL

        Returns:
             Python list containing string names of available embedding models
        """
        return await self._get(f"/{self.model_architecture}/embeddings")

