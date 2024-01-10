import aiohttp
import requests
from prodiapy.resources.utils import raise_exception


class SyncAPIClient:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def _request(self, method, endpoint, body=None):
        r = requests.request(method, self.base_url+endpoint, json=body, headers=self.headers)
        raise_exception(r.status_code, r.text)

        return r.json()

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
                raise_exception(r.status, await r.text())

                return await r.json()

    async def _post(self, endpoint, body):
        return await self._request("post", endpoint, body)

    async def _get(self, endpoint):
        return await self._request("get", endpoint)



