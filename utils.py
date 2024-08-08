import json

from request_model import Model
from task_model import Model as TaskModel
from sc.interfaces import TaskInterface


def read_requests_from_a_file(filename):
    with open(filename, "r") as f:
        raw_data = f.read()
    data = json.loads(raw_data)
    serialized_data = Model(**data)
    return serialized_data.requests


def get_request_by_callback_data(callback_data):
    request_id = callback_data.split("_")[-1]
    # TODO: handle StopIteration exception
    return next(request for request in get_some_requests() if request.id == request_id)


def read_tasks_from_json(filename):
    with open(filename, "r") as f:
        raw_data = f.read()
    data = json.loads(raw_data)
    serialized_data = TaskModel(**data)
    return serialized_data.tasks


def read_tasks_from_sc():
    return TaskInterface.list()


requests = read_requests_from_a_file("requests.json")


def get_some_requests():
    return requests


def delete_request(request_id):
    new_request = []
    global requests
    for req in requests:
        if req.id != request_id:
            new_request.append(req)
    requests = new_request


def emoji(status: dict):
    return "👍"
