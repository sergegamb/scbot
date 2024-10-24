import os

from telegram import InlineKeyboardButton

import messages
from utils import emoji


def back_to(destination):
    return InlineKeyboardButton(
        text=f"Back to {destination}",
        callback_data=destination,
    )


def delete_task(task_id):
    return InlineKeyboardButton(
        text=messages.delete_task,
        callback_data=f"delete_task_{task_id}",
    )


def delete_request_task(request_id, task_id):
    return InlineKeyboardButton(
        text=messages.delete_task,
        callback_data=f"delete_request_task_{request_id}_{task_id}"
    )


def request_button(request):
    # TODO: put button text template to another level
    return InlineKeyboardButton(
        text=f"#{request.id} {emoji(request.status)} {request.subject}",
        callback_data=f"request_{request.id}"
    )


def task_button(task):
    callback_data = f"task_{task.id}"
    if task.request is not None:  # request task
        callback_data = f"request_task_{task.id}_{task.request.id}"
    return InlineKeyboardButton(
        text=f"#{task.id} {emoji(task.status)} {task.title}",
        callback_data=callback_data
    )


add_task_button = InlineKeyboardButton(
    text="Add Task",
    callback_data="add_task"
)


requests_button = InlineKeyboardButton(
            text=messages.request_message,
            callback_data="requests_0",
        )

tasks_button = InlineKeyboardButton(
            text=messages.task_message,
            callback_data="tasks"
        )


def add_request_task_button(request_id):
    return InlineKeyboardButton(
        text=messages.add_task,
        callback_data=f"add_request_task_{request_id}"
    )


def open_request_task(task):
    domain = os.getenv("URL")[:-7]
    url = (
        f"{domain}/ui/tasks?mode=detail&from=showAllTasks&module=request"
        f"&taskId={task.id}&moduleId={task.request.id}"
    )
    return InlineKeyboardButton(
        text=messages.open_sc,
        url=url
    )

to_work_button = InlineKeyboardButton(
    text="В работу",
    callback_data="to_work"
)

to_hold_button = InlineKeyboardButton(
    text="Приостановить",
    callback_data="to_hold"
)

task_to_done = InlineKeyboardButton(
    text="Выполнена",
    callback_data="to_done"
)