
from prodiapy.resources.engine import APIResource, SyncAPIClient, AsyncAPIClient
from prodiapy.resources.utils import form_body
from typing import Optional


class FaceRestore(APIResource):
    def __init__(self, client: SyncAPIClient) -> None:
        super().__init__(client)

    def facerestore(
            self,
            image_url: Optional[str] = None,
            image_data: Optional[str] = None,
            dict_parameters: Optional[dict] = None,
            **kwargs
    ) -> dict:
        """
        Restore and enhance the face inside an image, source: https://docs.prodia.com/reference/facerestore

        Returns:
            Python dictionary, containing job id
        """
        return self._post(
            "/facerestore",
            body=form_body(
                dict_parameters=dict_parameters,
                imageUrl=image_url,
                imageData=image_data,
                **kwargs
            )
        )


class AsyncFaceRestore(APIResource):
    def __init__(self, client: AsyncAPIClient) -> None:
        super().__init__(client)

    async def facerestore(
            self,
            image_url: Optional[str] = None,
            image_data: Optional[str] = None,
            dict_parameters: Optional[dict] = None,
            **kwargs
    ) -> dict:
        """
        Restore and enhance the face inside an image, source: https://docs.prodia.com/reference/facerestore

        Returns:
            Python dictionary, containing job id
        """
        return await self._post(
            "/facerestore",
            body=form_body(
                dict_parameters=dict_parameters,
                imageUrl=image_url,
                imageData=image_data,
                **kwargs
            )
        )

