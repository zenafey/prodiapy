from .utils import *
import aiohttp


class ProdiaResponse:
    def __init__(self, image: str, payload: dict, response: dict, elapsed):
        self.failed = False
        self.url = image
        self.payload = payload
        self.response = response
        self.elapsed = elapsed

    def seed(self):
        return get_seed(self.url)

    def pnginfo(self):
        return get_pnginfo(self.url)

    def load(self):
        response = requests.get(self.url)
        return BytesIO(response.content)

    async def aload(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as response:
                return BytesIO(await response.read())

class ProdiaFailed:
    def __init__(self):
        self.failed = True
        self.url = None
        self.payload = None
        self.response = None
        self.elapsed = None