from telegram import InlineKeyboardMarkup

import buttons
import utils


def task_keyboard(task):

    column = [buttons.delete_task(task.id), buttons.back_to("tasks")]
    if task.request:
        column.append(buttons.view_request(task.request.id))
    return InlineKeyboardMarkup.from_column(column)


def task_list_keyboard(tasks):
    keyboard = []
    for task in tasks:
        keyboard.append(buttons.task_button(task))
    keyboard.append(buttons.add_task_button)
    keyboard.append(buttons.back_to("menu"))
    return InlineKeyboardMarkup.from_column(keyboard)


def request_keyboard(request, tasks):
    column = []
    for task in tasks:
        column.append(buttons.task_button(task))
    column.append(buttons.add_request_task_button(request.id))
    column.append(
        buttons.back_to("requests")
    )
    return InlineKeyboardMarkup.from_column(column)


def request_list_keyboard(requests):
    keyboard = []
    for request in requests:
        keyboard.append(buttons.request_button(request))
    keyboard.append(buttons.back_to("menu"))
    return InlineKeyboardMarkup.from_column(keyboard)


menu_keyboard = InlineKeyboardMarkup.from_column(
        [buttons.requests_button,
         buttons.tasks_button]
    )
