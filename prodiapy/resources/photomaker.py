
from prodiapy.resources.engine import APIResource, SyncAPIClient, AsyncAPIClient
from typing import Union, Literal, Optional
from prodiapy.resources.utils import form_body


class PhotoMaker(APIResource):
    def __init__(self, client: SyncAPIClient) -> None:
        super().__init__(client)

    def photomaker(
            self,
            image_urls: Optional[list[str]] = None,
            image_data: Optional[list[str]] = None,
            prompt: Optional[str] = None,
            negative_prompt: Optional[str] = None,
            style_preset: Optional[str] = None,
            strength: Optional[int] = None,
            steps: Optional[int] = None,
            seed: Optional[int] = None,
            dict_parameters: Optional[dict] = None,
            **kwargs
    ) -> dict:
        """
        Generate images with character consistency, source: https://docs.prodia.com/reference/photomaker

        Returns:
            Python dictionary containing job id
        """
        return self._post(
            "/photomaker",
            body=form_body(
                dict_parameters=dict_parameters,
                imageUrls=image_urls,
                imageData=image_data,
                prompt=prompt,
                negative_prompt=negative_prompt,
                style_preset=style_preset,
                strength=strength,
                steps=steps,
                seed=seed,
                **kwargs
            )
        )


class AsyncPhotoMaker(APIResource):
    def __init__(self, client: AsyncAPIClient) -> None:
        super().__init__(client)

    async def photomaker(
            self,
            image_urls: Optional[list[str]] = None,
            image_data: Optional[list[str]] = None,
            prompt: Optional[str] = None,
            negative_prompt: Optional[str] = None,
            style_preset: Optional[str] = None,
            strength: Optional[int] = None,
            steps: Optional[int] = None,
            seed: Optional[int] = None,
            dict_parameters: Optional[dict] = None,
            **kwargs
    ) -> dict:
        """
        Generate images with character consistency, source: https://docs.prodia.com/reference/photomaker

        Returns:
            Python dictionary containing job id
        """
        return await self._post(
            "/upscale",
            body=form_body(
                dict_parameters=dict_parameters,
                imageUrls=image_urls,
                imageData=image_data,
                prompt=prompt,
                negative_prompt=negative_prompt,
                style_preset=style_preset,
                strength=strength,
                steps=steps,
                seed=seed,
                **kwargs
            )
        )

