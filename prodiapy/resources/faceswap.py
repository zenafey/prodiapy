from prodiapy.resources.engine import APIResource
from prodiapy.resources.utils import form_body


class FaceSwap(APIResource):
    def __init__(self, client) -> None:
        super().__init__(client)

    def faceswap(
            self,
            sourceUrl: str | None = None,
            targetUrl: str | None = None,
            dict_parameters: dict | None = None
    ) -> dict:
        return self._post(
            "/faceswap",
            body=form_body(
                dict_parameters=dict_parameters,
                sourceUrl=sourceUrl,
                targetUrl=targetUrl
            )
        )


class AsyncFaceSwap(APIResource):
    def __init__(self, client) -> None:
        super().__init__(client)

    async def faceswap(
            self,
            sourceUrl: str | None = None,
            targetUrl: str | None = None,
            dict_parameters: dict | None = None
    ) -> dict:
        return await self._post(
            "/upscale",
            body=form_body(
                dict_parameters=dict_parameters,
                sourceUrl=sourceUrl,
                targetUrl=targetUrl
            )
        )

