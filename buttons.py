from telegram import InlineKeyboardButton

from utils import emoji


def back_to(destination):
    return InlineKeyboardButton(
        text=f"Back to {destination}",
        callback_data=destination,
    )


def delete_task(task_id):
    return InlineKeyboardButton(
        text="Delete task",
        callback_data=f"delete_task_{task_id}",
    )


def delete_request(request_id):
    return InlineKeyboardButton(
        text="Delete request",
        callback_data=f"delete_request_{request_id}",
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
        text=f"#{task.id} {task.title}",
        callback_data=callback_data
    )


add_task_button = InlineKeyboardButton(
    text="Add Task",
    callback_data="add_task"
)


requests_button = InlineKeyboardButton(
            text="Requests",
            callback_data="requests",
        )

tasks_button = InlineKeyboardButton(
            text="Tasks",
            callback_data="tasks"
        )
