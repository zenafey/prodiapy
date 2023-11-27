

__all__ = [
    "AuthenticationError",
    "InvalidParameterError",
    "UnknownError",
    "FailedJobError"
]


class ProdiaError(Exception):
    pass


class AuthenticationError(ProdiaError):
    pass


class InvalidParameterError(ProdiaError):
    pass


class UnknownError(ProdiaError):
    pass


class FailedJobError(ProdiaError):
    pass
