from __future__ import annotations
from prodiapy.resources import logger
from prodiapy._exceptions import *


def form_body(dict_parameters: dict | None = None, **kwargs):
    if dict_parameters:
        body = dict_parameters
    else:
        body = {}
        for kwarg in kwargs:
            if kwargs.get(kwarg) is not None:
                body[kwarg] = kwargs.get(kwarg)

    return body


def raise_exception(status, message):
    message_body = f"Prodia API returned {status}. Details: {message}"
    if status == 200:
        pass
    elif status in [401, 402]:
        logger.error("Caught error(Unauthorized)")
        raise AuthenticationError(message_body)
    elif status == 400:
        logger.error("Caught error(Invalid Generation Parameters)")
        raise InvalidParameterError(message_body)
    else:
        logger.error("Unknown request error")
        raise UnknownError(message_body)


