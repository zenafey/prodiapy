

class ProdiaResponse:
    """
    Prodia API result class

    Attributes:
        job_id: id of the job
        image_url: URL of generated image
        failed: is job failed or not(boolean)
        json: JSON response(dictionary)
    """
    def __init__(self, output: dict):
        self.job_id: str | None = output.get('job')
        self.image_url: str | None = output.get('imageUrl')
        self.failed: bool = output.get('failed', False)
        self.json: dict = output
