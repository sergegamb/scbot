import random

from telegram import Update
from telegram import (
        InlineKeyboardButton,
        InlineKeyboardMarkup,
        )

import utils
from task_model_simplifyed import Task


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
    keyboard.append(utils.add_task_button)
    keyboard.append(utils.back_to_menu_button)
    await update.callback_query.edit_message_text(
            text="tasks",
            reply_markup=InlineKeyboardMarkup.from_column(keyboard)
            )


async def delete_task(update: Update, context):
    task = utils.get_task_by_callback_data(update.callback_query.data)
    utils.delete_task(task.id)
    return await task_list(update, context)


async def get_task_title(update: Update, context):
    task_title = update.message.text
    task_id = str(random.randint(100, 600))
    payload = {
        "title": task_title,
        "id": task_id
    }
    t = Task(**payload)
    utils.add_task(t)
    tasks = utils.get_some_tasks()  # TODO: DRY
    keyboard = utils.compose_keyboard(tasks, "title", "task")
    keyboard.append(utils.add_task_button)
    keyboard.append(utils.back_to_menu_button)
    await update.message.reply_text(
        text="tasks",
        reply_markup=InlineKeyboardMarkup.from_column(keyboard)
    )
    return -1
    # return await task_list(update, context)


async def add_task(update: Update, context):
    await update.callback_query.edit_message_text(
        "Ok. You can write your task to me, i will track it for you"
    )
    return 0
