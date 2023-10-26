import aiohttp
import requests
from io import BytesIO
from prodiapy.exceptions import *
from prodiapy.log_util import *

def request(method, url, api_key=None, body=None):
    headers = {'X-Prodia-Key': api_key, 'Content-Type': 'application/json'}
    r = requests.request(method, url, json=body, headers=headers)
    if r.status_code in [401, 402]:
        error("Caught error(Unauthorized)")
        raise AuthorizationError(f"Prodia API returned {r.status_code}. Details: {r.text}")
    elif r.status_code == 400:
        error("Caught error(Invalid Generation Parameters)")
        raise InvalidParameter(f"Prodia API returned 400. Details: Invalid Generation Parameters")
    elif r.status_code not in [200, 400, 401, 402]:
        error("Unknown request error")
        raise UnknownError(f"Prodia API returned {r.status_code}. Details: {r.text}")

    resp = r.json()
    return resp

async def arequest(method, url, api_key=None, body=None):
    headers = {'X-Prodia-Key': api_key, 'Content-Type': 'application/json'}
    async with aiohttp.ClientSession() as s:
        async with s.request(method, url, json=body, headers=headers) as r:
            if r.status in [401, 402]:
                error("Caught error(Unauthorized)")
                raise AuthorizationError(f"Prodia API returned {r.status}. Details: {await r.text()}")
            elif r.status == 400:
                error("Caught error(Invalid Generation Parameters)")
                raise InvalidParameter(f"Prodia API returned 400. Details: Invalid Generation Parameters")
            elif r.status not in [200, 400, 401, 402]:
                error("Unknown request error")
                raise UnknownError(f"Prodia API returned {r.status}. Details: {await r.text()}")

            resp = await r.json()
            return resp


def load(url):
    logs(f"Loading image {url}...")
    return BytesIO(requests.get(url).content)

async def aload(url):
    logs(f"Loading image {url}...")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return BytesIO(await response.read())