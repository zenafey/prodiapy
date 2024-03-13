

class ProdiaResponse:
    """
    Prodia API result class

    Attributes:
        job_id: id of the job
        image_url: URL of generated image
        failed: is job failed or not(boolean)
        json: JSON response(raw)
    """
    def __init__(self, output: dict):
        self.job_id = output.get('job')
        self.image_url = output.get('imageUrl')
        self.failed = output.get('failed', False)
        self.json = output
