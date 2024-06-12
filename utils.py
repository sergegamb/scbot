import json

from request_model import Model


def get_some_requests():
    """ extract requests from the local data """
    with open("requests.json", "r") as f:
        raw_data = f.read()
    data = json.loads(raw_data)
    serialized_data = Model(**data)
    return serialized_data.requests


def get_request_by_callback_data(callback_data):
    request_id = callback_data.split("_")[-1]
    # TODO: handle StopIteration exception
    return next(request for request in get_some_requests() if request.id == request_id)
