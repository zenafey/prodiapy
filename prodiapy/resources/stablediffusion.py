from prodiapy.resources.engine import APIResource
from typing import Union
from prodiapy.resources.constants import *
from prodiapy.resources.utils import form_body


class StableDiffusion(APIResource):
    def __init__(self, client) -> None:
        super().__init__(client)

    def generate(
            self,
            model: Union[str, sd_model_literal, None] = None,
            prompt: str | None = None,
            negative_prompt: str | None = None,
            style_preset: Union[str, style_preset_literal, None] = None,
            steps: int | None = None,
            cfg_scale: int | float | None = None,
            seed: int | None = None,
            upscale: bool | None = None,
            sampler: Union[str, sd_sampler_literal, None] = None,
            aspect_ratio: Union[str, Literal["square", "portrait", "landscape"], None] = None,
            width: int | None = None,
            height: int | None = None,
            dict_parameters: dict | None = None
    ) -> dict:
        return self._post(
            "/sd/generate",
            body=form_body(
                dict_parameters=dict_parameters,
                model=model,
                prompt=prompt,
                negative_prompt=negative_prompt,
                style_preset=style_preset,
                steps=steps,
                cfg_scale=cfg_scale,
                seed=seed,
                upscale=upscale,
                sampler=sampler,
                aspect_ratio=aspect_ratio,
                width=width,
                height=height
            )
        )

    def transform(
            self,
            imageUrl: str | None = None,
            imageData = None,
            model: Union[str, sd_model_literal, None] = None,
            prompt: str | None = None,
            denoising_strength: float | None = None,
            negative_prompt: str | None = None,
            style_preset: Union[str, style_preset_literal, None] = None,
            steps: int | None = None,
            cfg_scale: int | float | None = None,
            seed: int | None = None,
            upscale: bool | None = None,
            sampler: Union[str, sd_sampler_literal, None] = None,
            width: int | None = None,
            height: int | None = None,
            dict_parameters: dict | None = None
    ) -> dict:
        return self._post(
            "/sd/transform",
            body=form_body(
                dict_parameters=dict_parameters,
                imageUrl=imageUrl,
                imageData=imageData,
                model=model,
                prompt=prompt,
                denoising_strength=denoising_strength,
                negative_prompt=negative_prompt,
                style_preset=style_preset,
                steps=steps,
                cfg_scale=cfg_scale,
                seed=seed,
                upscale=upscale,
                sampler=sampler,
                width=width,
                height=height
            )
        )

    def inpainting(
            self,
            imageUrl: str | None = None,
            imageData = None,
            maskUrl: str | None = None,
            maskData=None,
            model: Union[str, sd_model_literal, None] = None,
            prompt: str | None = None,
            denoising_strength: float | None = None,
            negative_prompt: str | None = None,
            style_preset: Union[str, style_preset_literal, None] = None,
            steps: int | None = None,
            cfg_scale: int | float | None = None,
            seed: int | None = None,
            upscale: bool | None = None,
            mask_blur: int | None = None,
            inpainting_fill: Union[int, Literal[0, 1, 2, 3], None] = None,
            inpainting_mask_invert: Union[int, Literal[0, 1], None] = None,
            inpainting_full_res: bool | None = None,
            sampler: Union[str, sd_sampler_literal, None] = None,
            width: int | None = None,
            height: int | None = None,
            dict_parameters: dict | None = None
    ) -> dict:
        return self._post(
            "/sd/inpainting",
            body=form_body(
                dict_parameters=dict_parameters,
                imageUrl=imageUrl,
                imageData=imageData,
                maskUrl=maskUrl,
                maskData=maskData,
                model=model,
                prompt=prompt,
                denoising_strength=denoising_strength,
                negative_prompt=negative_prompt,
                style_preset=style_preset,
                steps=steps,
                cfg_scale=cfg_scale,
                seed=seed,
                upscale=upscale,
                mask_blur=mask_blur,
                inpainting_fill=inpainting_fill,
                inpainting_mask_invert=inpainting_mask_invert,
                inpainting_full_res=inpainting_full_res,
                sampler=sampler,
                width=width,
                height=height
            )
        )

    def controlnet(
            self,
            imageUrl: str | None = None,
            imageData = None,
            model: Union[str, sd_model_literal, None] = None,
            controlnet_model: str | None = None,
            controlnet_module: str | None = None,
            controlnet_mode: Union[int, Literal[0, 1 , 2], None] = None,
            threshold_a: int | None = None,
            threshold_b: int | None = None,
            resize_mode: Union[int, Literal[0, 1, 2], None] = None,
            prompt: str | None = None,
            negative_prompt: str | None = None,
            style_preset: Union[str, style_preset_literal, None] = None,
            steps: int | None = None,
            cfg_scale: int | float | None = None,
            seed: int | None = None,
            upscale: bool | None = None,
            sampler: Union[str, sd_sampler_literal, None] = None,
            width: int | None = None,
            height: int | None = None,
            dict_parameters: dict | None = None
    ) -> dict:
        return self._post(
            "/sd/controlnet",
            body=form_body(
                dict_parameters=dict_parameters,
                imageUrl=imageUrl,
                imageData=imageData,
                model=model,
                controlnet_model=controlnet_model,
                controlnet_module=controlnet_module,
                controlnet_mode=controlnet_mode,
                threshold_a=threshold_a,
                threshold_b=threshold_b,
                resize_mode=resize_mode,
                prompt=prompt,
                negative_prompt=negative_prompt,
                style_preset=style_preset,
                steps=steps,
                cfg_scale=cfg_scale,
                seed=seed,
                upscale=upscale,
                sampler=sampler,
                width=width,
                height=height
            )
        )

    def models(self) -> list:
        return self._get("/sd/models")

    def samplers(self) -> list:
        return self._get("/sd/samplers")

    def loras(self) -> list:
        return self._get("/sd/loras")

    def embeddings(self) -> list:
        return self._get("/sd/embeddings")


class AsyncStableDiffusion(APIResource):
    def __init__(self, client) -> None:
        super().__init__(client)

    async def generate(
            self,
            model: Union[str, sd_model_literal, None] = None,
            prompt: str | None = None,
            negative_prompt: str | None = None,
            style_preset: Union[str, style_preset_literal, None] = None,
            steps: int | None = None,
            cfg_scale: int | float | None = None,
            seed: int | None = None,
            upscale: bool | None = None,
            sampler: Union[str, sd_sampler_literal, None] = None,
            aspect_ratio: Union[str, Literal["square", "portrait", "landscape"], None] = None,
            width: int | None = None,
            height: int | None = None,
            dict_parameters: dict | None = None
    ) -> dict:
        return await self._post(
            "/sd/generate",
            body=form_body(
                dict_parameters=dict_parameters,
                model=model,
                prompt=prompt,
                negative_prompt=negative_prompt,
                style_preset=style_preset,
                steps=steps,
                cfg_scale=cfg_scale,
                seed=seed,
                upscale=upscale,
                sampler=sampler,
                aspect_ratio=aspect_ratio,
                width=width,
                height=height
            )
        )

    async def transform(
            self,
            imageUrl: str | None = None,
            imageData=None,
            model: Union[str, sd_model_literal, None] = None,
            prompt: str | None = None,
            denoising_strength: float | None = None,
            negative_prompt: str | None = None,
            style_preset: Union[str, style_preset_literal, None] = None,
            steps: int | None = None,
            cfg_scale: int | float | None = None,
            seed: int | None = None,
            upscale: bool | None = None,
            sampler: Union[str, sd_sampler_literal, None] = None,
            width: int | None = None,
            height: int | None = None,
            dict_parameters: dict | None = None
    ) -> dict:
        return await self._post(
            "/sd/transform",
            body=form_body(
                dict_parameters=dict_parameters,
                imageUrl=imageUrl,
                imageData=imageData,
                model=model,
                prompt=prompt,
                denoising_strength=denoising_strength,
                negative_prompt=negative_prompt,
                style_preset=style_preset,
                steps=steps,
                cfg_scale=cfg_scale,
                seed=seed,
                upscale=upscale,
                sampler=sampler,
                width=width,
                height=height
            )
        )

    async def inpainting(
            self,
            imageUrl: str | None = None,
            imageData=None,
            maskUrl: str | None = None,
            maskData=None,
            model: Union[str, sd_model_literal, None] = None,
            prompt: str | None = None,
            denoising_strength: float | None = None,
            negative_prompt: str | None = None,
            style_preset: Union[str, style_preset_literal, None] = None,
            steps: int | None = None,
            cfg_scale: int | float | None = None,
            seed: int | None = None,
            upscale: bool | None = None,
            mask_blur: int | None = None,
            inpainting_fill: Union[int, Literal[0, 1, 2, 3], None] = None,
            inpainting_mask_invert: Union[int, Literal[0, 1], None] = None,
            inpainting_full_res: bool | None = None,
            sampler: Union[str, sd_sampler_literal, None] = None,
            width: int | None = None,
            height: int | None = None,
            dict_parameters: dict | None = None
    ) -> dict:
        return await self._post(
            "/sd/inpainting",
            body=form_body(
                dict_parameters=dict_parameters,
                imageUrl=imageUrl,
                imageData=imageData,
                maskUrl=maskUrl,
                maskData=maskData,
                model=model,
                prompt=prompt,
                denoising_strength=denoising_strength,
                negative_prompt=negative_prompt,
                style_preset=style_preset,
                steps=steps,
                cfg_scale=cfg_scale,
                seed=seed,
                upscale=upscale,
                mask_blur=mask_blur,
                inpainting_fill=inpainting_fill,
                inpainting_mask_invert=inpainting_mask_invert,
                inpainting_full_res=inpainting_full_res,
                sampler=sampler,
                width=width,
                height=height
            )
        )

    async def controlnet(
            self,
            imageUrl: str | None = None,
            imageData=None,
            model: Union[str, sd_model_literal, None] = None,
            controlnet_model: str | None = None,
            controlnet_module: str | None = None,
            controlnet_mode: Union[int, Literal[0, 1, 2], None] = None,
            threshold_a: int | None = None,
            threshold_b: int | None = None,
            resize_mode: Union[int, Literal[0, 1, 2], None] = None,
            prompt: str | None = None,
            negative_prompt: str | None = None,
            style_preset: Union[str, style_preset_literal, None] = None,
            steps: int | None = None,
            cfg_scale: int | float | None = None,
            seed: int | None = None,
            upscale: bool | None = None,
            sampler: Union[str, sd_sampler_literal, None] = None,
            width: int | None = None,
            height: int | None = None,
            dict_parameters: dict | None = None
    ) -> dict:
        return await self._post(
            "/sd/controlnet",
            body=form_body(
                dict_parameters=dict_parameters,
                imageUrl=imageUrl,
                imageData=imageData,
                model=model,
                controlnet_model=controlnet_model,
                controlnet_module=controlnet_module,
                controlnet_mode=controlnet_mode,
                threshold_a=threshold_a,
                threshold_b=threshold_b,
                resize_mode=resize_mode,
                prompt=prompt,
                negative_prompt=negative_prompt,
                style_preset=style_preset,
                steps=steps,
                cfg_scale=cfg_scale,
                seed=seed,
                upscale=upscale,
                sampler=sampler,
                width=width,
                height=height
            )
        )

    async def models(self) -> list:
        return await self._get("/sd/models")

    async def samplers(self) -> list:
        return await self._get("/sd/samplers")

    async def loras(self) -> list:
        return await self._get("/sd/loras")

    async def embeddings(self) -> list:
        return await self._get("/sd/embeddings")

