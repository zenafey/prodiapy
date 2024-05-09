
from prodiapy.resources.stablediffusion.template import StableDiffusionGeneral, AsyncStableDiffusionGeneral


class StableDiffusionXL(StableDiffusionGeneral):
    """
    class related to /sdxl endpoints, source: https://docs.prodia.com/reference/sdxl-generate
    """
    def __init__(self, client) -> None:
        super().__init__(client, model_architecture="sdxl")


class AsyncStableDiffusionXL(AsyncStableDiffusionGeneral):
    """
    class related to /sdxl endpoints, source: https://docs.prodia.com/reference/sdxl-generate
    """
    def __init__(self, client) -> None:
        super().__init__(client, model_architecture="sdxl")
