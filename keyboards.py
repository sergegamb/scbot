from telegram import InlineKeyboardMarkup

import buttons
import utils


def task_keyboard(task):
    column = [buttons.delete_task(task.id), buttons.back_to("tasks")]
    return InlineKeyboardMarkup.from_column(column)


def task_list_keyboard(tasks):
    keyboard = utils.make_list(tasks, "title", "task")
    keyboard.append(buttons.add_task_button)
    keyboard.append(buttons.back_to("menu"))
    return InlineKeyboardMarkup.from_column(keyboard)


def request_keyboard():
    keyboard = [buttons.back_to("requests")]
    return InlineKeyboardMarkup.from_column(keyboard)


def request_list_keyboard(requests):
    keyboard = utils.make_list(requests, "subject", "request")
    keyboard.append(buttons.back_to("menu"))
    return InlineKeyboardMarkup.from_column(keyboard)


menu_keyboard = InlineKeyboardMarkup.from_column(
        [buttons.requests_button,
         buttons.tasks_button]
    )
