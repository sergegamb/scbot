import json

from bs4 import BeautifulSoup

from request_model import Model
from task_model import Model as TaskModel
from sc.interfaces import TaskInterface


def read_requests_from_a_file(filename):
    with open(filename, "r") as f:
        raw_data = f.read()
    data = json.loads(raw_data)
    serialized_data = Model(**data)
    return serialized_data.requests


def read_tasks_from_json(filename):
    with open(filename, "r") as f:
        raw_data = f.read()
    data = json.loads(raw_data)
    serialized_data = TaskModel(**data)
    return serialized_data.tasks


def read_tasks_from_sc():
    return TaskInterface.list()


def emoji(status):
    if status.id == 1:  # Закрыта
        return "⏹"
    if status.id == 2:  # Открыта
        return "🆓"
    if status.id == 3:  # Запланирована
        return "⏸"
    if status.id == 4:  # Выполнена
        return "🆒"
    if status.id == 5:  # Назначена
        return "🆕"
    if status.id == 6:  # В работе
        return "🔥"
    if status.id == 301:  # Запрос разработчикам
        return "ℹ️"
    if status.id == 1201:  # На согласовании
        return "⏯"
    return "👍"


def extract_text(html):
    if html is None:
        return "Empty"
    html = html.replace("<br />", "\n")
    soup = BeautifulSoup(html)
    return soup.getText()
