from telegram import Update
from telegram import (
        InlineKeyboardButton,
        InlineKeyboardMarkup,
        )

import utils


async def task_view(update: Update, context):
    task = utils.get_task_by_callback_data(update.callback_query.data)
    await update.callback_query.answer("Yoy")
    message_text = f"#{task.id}\n{task.title}"
    keyboard = InlineKeyboardButton(
            text="Go back to list view",
            callback_data="tasks"
            )
    await update.callback_query.edit_message_text(
            text=message_text,
            reply_markup=InlineKeyboardMarkup.from_button(keyboard)
            )


async def task_list(update: Update, context):
    tasks = utils.get_some_tasks()  # TODO: get tasks from support center
    # title is what we need
    message_text = "tasks"  # TODO: get message from file based on user language prefferences
    keyboard = utils.compose_keyboard(tasks, "title", "task")
    keyboard.append(
        InlineKeyboardButton(
            text="Go back",
            callback_data="menu"
        )
    )
    await update.callback_query.edit_message_text(
            text="tasks",
            reply_markup=InlineKeyboardMarkup.from_column(keyboard)
            )
