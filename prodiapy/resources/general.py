

from prodiapy.resources.engine import APIResource, SyncAPIClient, AsyncAPIClient
from prodiapy.resources.facerestore import FaceRestore, AsyncFaceRestore
from prodiapy.resources.faceswap import FaceSwap, AsyncFaceSwap
from prodiapy.resources.upscale import Upscale, AsyncUpscale
from prodiapy.resources.photomaker import PhotoMaker, AsyncPhotoMaker
from prodiapy.resources.response import ProdiaResponse
from prodiapy.resources.utils import form_body
from prodiapy.resources import logger
from prodiapy._exceptions import *

import time
import asyncio
from typing import Optional


class General(APIResource):
    facerestore: FaceRestore.facerestore
    faceswap: FaceSwap.faceswap
    upscale: Upscale.upscale

    def __init__(self, client: SyncAPIClient) -> None:
        super().__init__(client)
        self.photomaker = PhotoMaker(client).photomaker
        self.facerestore = FaceRestore(client).facerestore
        self.faceswap = FaceSwap(client).faceswap
        self.upscale = Upscale(client).upscale

    def create(
            self,
            endpoint: str = "/sd/generate",
            dict_parameters: Optional[dict] = None,
            **params
    ) -> dict:
        """
        Universal method for any POST request to Prodia API
        Args:
            endpoint: endpoint in format "/{endpoint}"
            dict_parameters: request body in dictionary format, if passed **params are ignored
            **params: request body in kwargs format

        Returns:
            Python dictionary, containing job id
        """
        return self._post(
            endpoint,
            body=form_body(
                dict_parameters=dict_parameters,
                **params
            )
        )

    def constants(self, endpoint: str = "/sd/models") -> list:
        """
        Universal endpoint for any GET request to Prodia API(excepting /job/{job_id}, use job() method for this)
        Args:
            endpoint: listing endpoint in format "/{endpoint}"

        Returns:
            Actual list of available choices for chosen parameter
        """
        return self._get(endpoint)

    def job(self, job_id: str) -> dict:
        """
        Get job information, source: https://docs.prodia.com/reference/getjob

        Returns:
            Python dictionary, containing job information(status, result if succeeded generation)
        """
        return self._get(f"/job/{job_id}")

    def wait(
            self,
            job: dict,
            raise_on_fail: bool = True
    ) -> ProdiaResponse:
        """
        Wait until generation complete and get result or error if generation failed
        Args:
            job: Python dictionary you got from POST methods
            raise_on_fail: boolean

        Returns:
            ProdiaResponse object
        """
        job_result = job

        while job_result['status'] not in ['succeeded', 'failed']:
            time.sleep(0.25)
            job_result = self.job(job['job'])

        if job_result['status'] == 'failed':
            logger.failed(f"Job {job_result['job']} failed")
            if raise_on_fail:
                raise FailedJobError(f"Job {job_result['job']} failed")
            return ProdiaResponse({'job': job_result['job'], 'failed': True})

        logger.success(f"Got result: {job_result}")
        return ProdiaResponse(job_result)


class AsyncGeneral(APIResource):
    facerestore: AsyncFaceRestore.facerestore
    faceswap: AsyncFaceSwap.faceswap
    upscale: AsyncUpscale.upscale

    def __init__(self, client: AsyncAPIClient) -> None:
        super().__init__(client)
        self.photomaker = AsyncPhotoMaker(client).photomaker
        self.facerestore = AsyncFaceRestore(client).facerestore
        self.faceswap = AsyncFaceSwap(client).faceswap
        self.upscale = AsyncUpscale(client).upscale

    async def create(
            self,
            endpoint: str = "/sd/generate",
            dict_parameters: Optional[dict] = None,
            **params
    ) -> dict:
        """
        Universal method for any POST request to Prodia API
        Args:
            endpoint: endpoint in format "/{endpoint}"
            dict_parameters: request body in dictionary format, if passed **params are ignored
            **params: request body in kwargs format

        Returns:
            Python dictionary, containing job id
        """
        return await self._post(
            endpoint,
            body=form_body(
                dict_parameters=dict_parameters,
                **params
            )
        )

    async def constants(self, endpoint: str = "/sd/models") -> list:
        """
        Universal endpoint for any GET request to Prodia API(excepting /job/{job_id}, use job() method for this)
        Args:
            endpoint: listing endpoint in format "/{endpoint}"

        Returns:
            Actual list of available choices for chosen parameter
        """
        return await self._get(endpoint)

    async def job(self, job_id: str) -> dict:
        """
        Get information about a generation job, including status, source: https://docs.prodia.com/reference/getjob

        Returns:
            Python dictionary, containing job information(status, result if succeeded generation)
        """
        return await self._get(f"/job/{job_id}")

    async def wait(
            self,
            job: dict,
            raise_on_fail: bool = True
    ) -> ProdiaResponse:
        """
        Wait until generation complete and get result or error if generation failed
        Args:
            job: Python dictionary you got from POST methods
            raise_on_fail: boolean

        Returns:
            ProdiaResponse object
        """
        job_result = job

        while job_result['status'] not in ['succeeded', 'failed']:
            await asyncio.sleep(0.25)
            job_result = await self.job(job['job'])

        if job_result['status'] == 'failed':
            logger.failed(f"Job {job_result['job']} failed")
            if raise_on_fail:
                raise FailedJobError(f"Job {job_result['job']} failed")
            return ProdiaResponse({'job': job_result['job'], 'failed': True})

        logger.success(f"Got result: {job_result}")
        return ProdiaResponse(job_result)
