from prodiapy.util import request, arequest
from prodiapy.log_util import logs

class Engine:
    @classmethod
    def _post(cls, url, body, api_key):
        return request(method='post', url=url, api_key=api_key, body=body)

    @classmethod
    def _get(cls, url, api_key):
        return request(method='get', url=url, api_key=api_key)

    @classmethod
    async def _apost(cls, url, body, api_key):
        return await arequest(method='post', url=url, api_key=api_key, body=body)

    @classmethod
    async def _aget(cls, url, api_key):
        return await arequest(method='get', url=url, api_key=api_key)