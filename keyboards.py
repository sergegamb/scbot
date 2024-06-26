from telegram import InlineKeyboardMarkup, InlineKeyboardButton

import buttons


def task_keyboard(task):
    column = [buttons.back_to("tasks"), buttons.delete_task(task.id)]
    return InlineKeyboardMarkup.from_column(column)


def make_list(objects, param, name):
    # TODO: rewrite so working not with dicts
    simplified_objects = []
    for obj in objects:
        simplified_objects.append(obj.representation())
    keyboard = []
    for obj in simplified_objects:
        button = InlineKeyboardButton(
            text=f"#{obj.get('id')} {obj.get(param)}",
            callback_data=f"{name}_{obj.get('id')}"
        )
        keyboard.append(button)
    return keyboard


def task_list_keyboard(tasks):
    keyboard = make_list(tasks, "title", "task")
    keyboard.append(buttons.add_task_button)
    keyboard.append(buttons.back_to("menu"))
    return InlineKeyboardMarkup.from_column(keyboard)

