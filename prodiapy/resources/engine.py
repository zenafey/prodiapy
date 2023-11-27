import aiohttp
import requests
from prodiapy._exceptions import *
from prodiapy.resources import logger


class SyncAPIClient:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def _request(self, method, endpoint, body=None):
        r = requests.request(method, self.base_url+endpoint, json=body, headers=self.headers)
        match r.status_code:
            case 200:
                return r.json()
            case 401 | 402:
                logger.error("Caught error(Unauthorized)")
                raise AuthenticationError(f"Prodia API returned {r.status_code}. Details: {r.text}")
            case 400:
                logger.error("Caught error(Invalid Generation Parameters)")
                raise InvalidParameterError(f"Prodia API returned {r.status_code}. Details: {r.text}")
            case _:
                logger.error("Unknown request error")
                raise UnknownError(f"Prodia API returned {r.status_code}. Details: {r.text}")

    def _post(self, endpoint, body):
        return self._request("post", endpoint, body)

    def _get(self, endpoint):
        return self._request("get", endpoint)


class APIResource:

    def __init__(self, client) -> None:
        self._client = client
        self._get = client._get
        self._post = client._post


class AsyncAPIClient:
    base_url: str
    headers: dict

    def __init__(self, base_url: str, headers: dict):
        self.base_url = base_url
        self.headers = headers

    async def _request(self, method, endpoint, body=None):
        async with aiohttp.ClientSession() as s:
            async with s.request(method, self.base_url+endpoint, json=body, headers=self.headers) as r:
                match r.status:
                    case 200:
                        return await r.json()
                    case 401 | 402:
                        logger.error("Caught error(Unauthorized)")
                        raise AuthenticationError(f"Prodia API returned {r.status}. Details: {await r.text()}")
                    case 400:
                        logger.error("Caught error(Invalid Generation Parameters)")
                        raise InvalidParameterError(f"Prodia API returned {r.status}. Details: {await r.text()}")
                    case _:
                        logger.error("Unknown request error")
                        raise UnknownError(f"Prodia API returned {r.status}. Details: {await r.text()}")

    async def _post(self, endpoint, body):
        return await self._request("post", endpoint, body)

    async def _get(self, endpoint):
        return await self._request("get", endpoint)



