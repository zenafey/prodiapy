class ProdiaException(Exception):
    """Exception raised by Prodia"""

class ClientError(ProdiaException):
    """Exception raised by Client init"""

class InvalidParameter(ProdiaException):
    """Exception raised by invalid parameters"""

class UnknownError(ProdiaException):
    """Exception raised by unknown Prodia errors"""