
from prodiapy.resources.engine import SyncAPIClient
from prodiapy.resources import constants
from prodiapy import resources
from typing import Optional
from prodiapy._exceptions import *

import os


class Prodia(SyncAPIClient):
    """Prodia Client"""
    api_key: str
    sd: resources.StableDiffusion
    sdxl: resources.StableDiffusionXL
    general: resources.General

    def __init__(
            self,
            api_key: Optional[str] = os.getenv("PRODIA_API_KEY"),
            base_url: str = os.getenv("PRODIA_API_BASE", "https://api.prodia.com/v1")
    ):
        """Construct a new prodia client instance.

            This automatically infers the following arguments from their corresponding environment variables if they are not provided:
            - `api_key` from `PRODIA_API_KEY`
        """
        if api_key is None:
            raise AuthenticationError(constants.AUTHENTICATION_ERROR)
        self.api_key = api_key

        super().__init__(
            base_url=base_url,
            headers=self.auth_headers
        )

        self.sd = resources.StableDiffusion(self)
        self.sdxl = resources.StableDiffusionXL(self)

        general = resources.General(self)

        self.photomaker = general.photomaker
        self.faceswap = general.faceswap
        self.upscale = general.upscale
        self.create = general.create
        self.job = general.job
        self.constants = general.constants
        self.wait = general.wait

    @property
    def auth_headers(self) -> dict:
        api_key = self.api_key
        return {'X-Prodia-Key': api_key, 'Content-Type': 'application/json'}


