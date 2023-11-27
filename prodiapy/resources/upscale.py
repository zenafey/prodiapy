from prodiapy.resources.engine import APIResource
from typing import Union
from prodiapy.resources.constants import *
from prodiapy.resources.utils import form_body


class Upscale(APIResource):
    def __init__(self, client) -> None:
        super().__init__(client)

    def upscale(
            self,
            imageUrl: str | None = None,
            imageData=None,
            resize: Union[int, Literal[2, 4]] = 2,
            dict_parameters: dict | None = None
    ) -> dict:
        body = form_body(
                dict_parameters=dict_parameters,
                imageUrl=imageUrl,
                imageData=imageData,
                resize=resize
            )
        print(body)
        return self._post(
            "/upscale",
            body=form_body(
                dict_parameters=dict_parameters,
                imageUrl=imageUrl,
                imageData=imageData,
                resize=resize
            )
        )


class AsyncUpscale(APIResource):
    def __init__(self, client) -> None:
        super().__init__(client)

    async def upscale(
            self,
            imageUrl: str | None = None,
            imageData=None,
            resize: Union[int, Literal[2, 4], None] = None,
            dict_parameters: dict | None = None
    ) -> dict:
        return await self._post(
            "/upscale",
            body=form_body(
                dict_parameters=dict_parameters,
                imageUrl=imageUrl,
                imageData=imageData,
                resize=resize
            )
        )

