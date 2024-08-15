from telegram import InlineKeyboardMarkup

from sc.interfaces import RequestInterface
import buttons


def task_keyboard(task):
    keyboard = [buttons.delete_task(task.id),
                buttons.back_to("tasks")]
    return InlineKeyboardMarkup.from_column(keyboard)


def request_task_keyboard(task):
    request = RequestInterface.get(task.request.id)
    keyboard = [buttons.delete_request_task(task.request.id, task.id),
                buttons.request_button(request),
                buttons.open_request_task(task),
                buttons.back_to("menu")]
    return InlineKeyboardMarkup.from_column(keyboard)


def task_list_keyboard(tasks):
    keyboard = [buttons.task_button(task) for task in tasks]
    keyboard.append(buttons.add_task_button)
    keyboard.append(buttons.back_to("menu"))
    return InlineKeyboardMarkup.from_column(keyboard)


def request_keyboard(request, tasks):
    keyboard = [buttons.task_button(task) for task in tasks]
    keyboard.append(buttons.add_request_task_button(request.id))
    keyboard.append(buttons.back_to("requests"))
    return InlineKeyboardMarkup.from_column(keyboard)


def request_list_keyboard(requests):
    keyboard = [buttons.request_button(request) for request in requests]
    keyboard.append(buttons.back_to("menu"))
    return InlineKeyboardMarkup.from_column(keyboard)


menu_keyboard = InlineKeyboardMarkup.from_column(
        [buttons.requests_button,
         buttons.tasks_button]
    )
