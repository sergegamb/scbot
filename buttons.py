from telegram import InlineKeyboardButton


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