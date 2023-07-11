from .utils import *


class ProdiaResponse:
    def __init__(self, image: list, payload: dict, response: dict):
        self.url = image
        self.payload = payload
        self.response = response

    def seed(self):
        return get_seed(self.url)

    def pnginfo(self):
        return get_pnginfo(self.url)
