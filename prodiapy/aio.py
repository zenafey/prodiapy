from typing import Optional
import os

from prodiapy.resources.engine import AsyncAPIClient
from prodiapy.resources import constants
from prodiapy import resources
from prodiapy._exceptions import AuthenticationError


class Prodia(AsyncAPIClient):
    """Asynchronous Prodia Client"""
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
            raise AuthenticationError(constants.AUTHENTICATION_ERROR)
        self.api_key = api_key

        super().__init__(
            base_url=base_url,
            headers=self.auth_headers
        )

        self.sd = resources.AsyncStableDiffusion(self)
        self.sdxl = resources.AsyncStableDiffusionXL(self)

        general = resources.AsyncGeneral(self)

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
