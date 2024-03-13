

__all__ = [
    "AuthenticationError",
    "InvalidParameterError",
    "UnknownError",
    "FailedJobError",
    "exception_vocab"
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


exception_vocab = {
    401 | 401: AuthenticationError,
    400: InvalidParameterError
    }
