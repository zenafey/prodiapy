from prodiapy.resources.engine import SyncAPIClient, AsyncAPIClient
from prodiapy import resources
from prodiapy._exceptions import *
from typing_extensions import override

import os


class Prodia(SyncAPIClient):
    sd: resources.StableDiffusion
    sdxl: resources.StableDiffusionXL

    api_key: str

    def __init__(
            self,
            api_key: str | None = None,
            base_url: str | None = None
    ) -> None:
        """Construct a new prodia client instance.

            This automatically infers the following arguments from their corresponding environment variables if they are not provided:
            - `api_key` from `PRODIA_API_KEY`
        """
        if api_key is None:
            api_key = os.environ.get("PRODIA_API_KEY")
        if api_key is None:
            raise AuthenticationError(
                "The api_key client option must be set either by passing api_key to the client or by setting the \
                PRODIA_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = f"https://api.prodia.com/v1"

        super().__init__(
            base_url=base_url,
            headers=self.auth_headers
        )

        self.sd = resources.StableDiffusion(self)
        self.sdxl = resources.StableDiffusionXL(self)

        general = resources.General(self)
        upscale = resources.Upscale(self)
        faceswap = resources.FaceSwap(self)

        self.faceswap = faceswap.faceswap
        self.upscale = upscale.upscale
        self.create = general.create
        self.job = general.job
        self.constant = general.constant
        self.wait = general.wait


    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {'X-Prodia-Key': api_key, 'Content-Type': 'application/json'}


class AsyncProdia(AsyncAPIClient):
    sd: resources.AsyncStableDiffusion
    sdxl: resources.AsyncStableDiffusionXL

    api_key: str

    def __init__(
            self,
            api_key: str | None = None,
            base_url: str | None = None
    ) -> None:
        """Construct a new async prodia client instance.

            This automatically infers the following arguments from their corresponding environment variables if they are not provided:
            - `api_key` from `PRODIA_API_KEY`
        """
        if api_key is None:
            api_key = os.environ.get("PRODIA_API_KEY")
        if api_key is None:
            raise AuthenticationError(
                "The api_key client option must be set either by passing api_key to the client or by setting the \
                PRODIA_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = f"https://api.prodia.com/v1"

        super().__init__(
            base_url=base_url,
            headers=self.auth_headers
        )

        self.sd = resources.AsyncStableDiffusion(self)
        self.sdxl = resources.AsyncStableDiffusionXL(self)

        general = resources.AsyncGeneral(self)
        upscale = resources.AsyncUpscale(self)
        faceswap = resources.AsyncFaceSwap(self)

        self.faceswap = faceswap.faceswap
        self.upscale = upscale.upscale
        self.create = general.create
        self.job = general.job
        self.constant = general.constant
        self.wait = general.wait

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {'X-Prodia-Key': api_key, 'Content-Type': 'application/json'}