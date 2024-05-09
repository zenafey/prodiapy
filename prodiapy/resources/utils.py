
from typing import Optional
from prodiapy._exceptions import *


def form_body(dict_parameters: Optional[dict] = None, **kwargs) -> dict:
    return dict_parameters or {k: v for k, v in kwargs.items() if v is not None}


def raise_exception(status: int, message: str) -> None:
    message_body = f"Prodia API returned {status}. Details: {message}"
    exception = exception_vocab.get(status, UnknownError)
    if status != 200:
        raise exception(message_body)


