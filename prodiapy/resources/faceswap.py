
from prodiapy.resources.engine import APIResource, SyncAPIClient, AsyncAPIClient
from prodiapy.resources.utils import form_body
from typing import Optional


class FaceSwap(APIResource):
    def __init__(self, client: SyncAPIClient) -> None:
        super().__init__(client)

    def faceswap(
            self,
            source_url: Optional[str] = None,
            target_url: Optional[str] = None,
            dict_parameters: Optional[dict] = None,
            **kwargs
    ) -> dict:
        """
        Swap a face inside an image (source_url) with another (target_url)
source: https://docs.prodia.com/reference/faceswap


        Returns:
            Python dictionary, containing job id
        """
        return self._post(
            "/faceswap",
            body=form_body(
                dict_parameters=dict_parameters,
                sourceUrl=source_url,
                targetUrl=target_url,
                **kwargs
            )
        )


class AsyncFaceSwap(APIResource):
    def __init__(self, client: AsyncAPIClient) -> None:
        super().__init__(client)

    async def faceswap(
            self,
            source_url: Optional[str] = None,
            target_url: Optional[str] = None,
            dict_parameters: Optional[dict] = None,
            **kwargs
    ) -> dict:
        """
        Swap a face inside an image (source_url) with another (target_url)
source: https://docs.prodia.com/reference/faceswap


        Returns:
            Python dictionary, containing job id
        """
        return await self._post(
            "/faceswap",
            body=form_body(
                dict_parameters=dict_parameters,
                sourceUrl=source_url,
                targetUrl=target_url,
                **kwargs
            )
        )

