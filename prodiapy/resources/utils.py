

def form_body(dict_parameters: dict | None = None, **kwargs):
    match dict_parameters:
        case None:
            body = {}
            for kwarg in kwargs:
                if kwargs.get(kwarg) is not None:
                    body[kwarg] = kwargs.get(kwarg)
        case _:
            body = dict_parameters

    return body

