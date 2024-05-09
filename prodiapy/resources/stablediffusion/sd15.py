from __future__ import annotations

from typing import Union, Optional, Literal
from prodiapy.resources.stablediffusion.template import StableDiffusionGeneral, AsyncStableDiffusionGeneral
from prodiapy.resources.engine import SyncAPIClient, AsyncAPIClient
from prodiapy.resources.utils import form_body


class StableDiffusion(StableDiffusionGeneral):
    """class related to /sd endpoints, source: https://docs.prodia.com/reference/generate"""
    def __init__(self, client: SyncAPIClient) -> None:
        super().__init__(client, model_architecture="sd")

    def controlnet(
            self,
            image_url: Optional[str] = None,
            image_data: Optional[str] = None,
            model: Optional[str] = None,
            controlnet_model: Optional[str] = None,
            controlnet_module: Optional[str] = None,
            controlnet_mode: Optional[Union[int, Literal[0, 1, 2]]] = None,
            threshold_a: Optional[int] = None,
            threshold_b: Optional[int] = None,
            resize_mode: Optional[Union[int, Literal[0, 1, 2]]] = None,
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
        return self._post(
            f"/sd/controlnet",
            body=form_body(
                dict_parameters=dict_parameters,
                imageUrl=image_url,
                imageData=image_data,
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
                sampler=sampler,
                width=width,
                height=height,
                **kwargs
            )
        )


class AsyncStableDiffusion(AsyncStableDiffusionGeneral):
    """class related to /sd endpoints, source: https://docs.prodia.com/reference/generate"""
    def __init__(self, client: AsyncAPIClient) -> None:
        super().__init__(client, model_architecture="sd")

    async def controlnet(
            self,
            image_url: Optional[str] = None,
            image_data: Optional[str] = None,
            model: Optional[str] = None,
            controlnet_model: Optional[str] = None,
            controlnet_module: Optional[str] = None,
            controlnet_mode: Optional[Union[int, Literal[0, 1, 2]]] = None,
            threshold_a: Optional[int] = None,
            threshold_b: Optional[int] = None,
            resize_mode: Optional[Union[int, Literal[0, 1, 2]]] = None,
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
        return await self._post(
            f"/sd/controlnet",
            body=form_body(
                dict_parameters=dict_parameters,
                imageUrl=image_url,
                imageData=image_data,
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
                sampler=sampler,
                width=width,
                height=height,
                **kwargs
            )
        )

