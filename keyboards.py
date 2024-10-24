from telegram import InlineKeyboardMarkup, InlineKeyboardButton

from sc.interfaces import RequestInterface
import buttons
from sc.request_model import Request

next_page  = InlineKeyboardButton(
    text="Next page",
    callback_data="next_page"
    )
previous_page = InlineKeyboardButton(
    text="Previous page",
    callback_data="previous_page"
)

def task_keyboard(task):
    keyboard = [buttons.delete_task(task.id),
                buttons.task_to_done,
                buttons.back_to("tasks")]
    return InlineKeyboardMarkup.from_column(keyboard)


def request_task_keyboard(task):
    request = RequestInterface.get(task.request.id)
    keyboard = [buttons.delete_request_task(task.request.id, task.id),
                buttons.task_to_done,
                buttons.request_button(request),
                buttons.open_request_task(task),
                buttons.back_to("menu")]
    return InlineKeyboardMarkup.from_column(keyboard)


def task_list_keyboard(tasks):
    keyboard = [buttons.task_button(task) for task in tasks]
    keyboard.append(buttons.add_task_button)
    keyboard.append(buttons.back_to("menu"))
    return InlineKeyboardMarkup.from_column(keyboard)


def request_keyboard(request: Request, tasks):
    keyboard = [buttons.task_button(task) for task in tasks]
    keyboard.append(buttons.add_request_task_button(request.id))
    if request.status.name != "В работе":
        keyboard.append(buttons.to_work_button)
    if request.status.name != "Приостановлена":
        keyboard.append(buttons.to_hold_button)
    keyboard.append(buttons.back_to("requests"))
    return InlineKeyboardMarkup.from_column(keyboard)


def  request_list_keyboard(requests, filter_option):
    first_button = InlineKeyboardButton(
        text=f"Filter: {filter_option} requests",
        callback_data="filters"
    )
    keyboard = [[first_button]]
    for request in requests:
        keyboard.append([buttons.request_button(request)])
    keyboard.append([previous_page, buttons.back_to("menu"), next_page])
    return InlineKeyboardMarkup(keyboard)


menu_keyboard = InlineKeyboardMarkup.from_column(
        [buttons.requests_button,
         buttons.tasks_button]
    )
