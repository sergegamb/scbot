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
    keyboard = [InlineKeyboardButton(
            text="Delete",
            callback_data=f"delete_task_{task.id}"
    ), keyboard]
    await update.callback_query.edit_message_text(
            text=message_text,
            reply_markup=InlineKeyboardMarkup.from_column(keyboard)
            )


async def task_list(update: Update, context):
    tasks = utils.get_some_tasks()  # TODO: get tasks from support center
    keyboard = utils.compose_keyboard(tasks, "title", "task")
    keyboard.append(utils.back_to_menu_button)
    await update.callback_query.edit_message_text(
            text="tasks",
            reply_markup=InlineKeyboardMarkup.from_column(keyboard)
            )


async def delete_task(update: Update, context):
    task = utils.get_task_by_callback_data(update.callback_query.data)
    utils.delete_task(task.id)
    return await task_list(update, context)


async def add_task(update, context):
    pass