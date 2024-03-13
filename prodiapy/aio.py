
from prodiapy.resources.engine import AsyncAPIClient
from prodiapy import resources
from typing import Optional
from prodiapy._exceptions import *

import os


class Prodia(AsyncAPIClient):
    api_key: str
    sd: resources.AsyncStableDiffusion
    sdxl: resources.AsyncStableDiffusionXL
    general: resources.AsyncGeneral

    def __init__(
            self,
            api_key: Optional[str] = os.getenv("PRODIA_API_KEY"),
            base_url: str = os.getenv("PRODIA_API_BASE", "https://api.prodia.com/v1")
    ) -> None:
        """Construct a new async prodia client instance.

            This automatically infers the following arguments from their corresponding environment variables if they are not provided:
            - `api_key` from `PRODIA_API_KEY`
        """
        if api_key is None:
            raise AuthenticationError(
                "The api_key client option must be set either by passing api_key to the client or by setting the \
PRODIA_API_KEY environment variable"
            )
        self.api_key = api_key

        super().__init__(
            base_url=base_url,
            headers=self.auth_headers
        )

        self.sd = resources.AsyncStableDiffusion(self)
        self.sdxl = resources.AsyncStableDiffusionXL(self)

        general = resources.AsyncGeneral(self)

        self.faceswap = general.faceswap
        self.upscale = general.upscale
        self.create = general.create
        self.job = general.job
        self.constant = general.constants
        self.wait = general.wait

    @property
    def auth_headers(self) -> dict:
        api_key = self.api_key
        return {'X-Prodia-Key': api_key, 'Content-Type': 'application/json'}