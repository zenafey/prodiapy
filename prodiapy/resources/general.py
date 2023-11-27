from prodiapy.resources.engine import APIResource
from prodiapy.resources.response import ProdiaResponse
from prodiapy.resources.logger import logger
from prodiapy.resources.utils import form_body
from prodiapy._exceptions import *

import time
import asyncio


class General(APIResource):
    def __init__(self, client) -> None:
        super().__init__(client)

    def create(
            self,
            endpoint: str = "/sd/generate",
            dict_parameters: dict | None = None,
            **params
    ) -> dict:
        return self._post(
            endpoint,
            body=form_body(
                dict_parameters=dict_parameters,
                **params
            )
        )

    def constant(
            self,
            endpoint: str = "/sd/models"
    ) -> list:
        return self._get(endpoint)

    def job(
            self,
            job_id: str
    ) -> dict:
        return self._get(f"/job/{job_id}")

    def wait(self, job: dict, raise_on_fail: bool = True):
        job_result = job

        while job_result['status'] not in ['succeeded', 'failed']:
            time.sleep(0.25)
            job_result = self.job(job['job'])

        if job_result['status'] == 'failed':
            logger.failed(f"Job {job_result['job']} failed")
            if raise_on_fail:
                raise FailedJobError("Job failed")
            return ProdiaResponse({'failed': True})

        logger.success(f"Got result: {job_result}")
        return ProdiaResponse(job_result)


class AsyncGeneral(APIResource):
    def __init__(self, client) -> None:
        super().__init__(client)

    async def create(
            self,
            endpoint: str = "/sd/generate",
            dict_parameters: dict | None = None,
            **params
    ) -> dict:
        return await self._post(
            endpoint,
            body=form_body(
                dict_parameters=dict_parameters,
                **params
            )
        )

    async def constant(
            self,
            endpoint: str = "/sd/models"
    ) -> list:
        return await self._get(endpoint)

    async def job(
            self,
            job_id: str
    ) -> dict:
        return await self._get(f"/job/{job_id}")

    async def wait(self, job: dict, raise_on_fail: bool = True):
        job_result = job

        while job_result['status'] not in ['succeeded', 'failed']:
            await asyncio.sleep(0.25)
            job_result = await self.job(job['job'])

        if job_result['status'] == 'failed':
            logger.failed(f"Job {job_result['job']} failed")
            if raise_on_fail:
                raise FailedJobError("Job failed")
            return ProdiaResponse({'failed': True})

        logger.success(f"Got result: {job_result}")
        return ProdiaResponse(job_result)