import random

from telegram import Update

import keyboards
import messages
import utils
from task_model_simplifyed import Task


async def task_view(update: Update, context):
    task = utils.get_task_by_callback_data(update.callback_query.data)
    await update.callback_query.answer("Yoy")
    message_text = f"#{task.id}\n{task.title}"
    keyboard = keyboards.task_keyboard(task)
    await update.callback_query.edit_message_text(
            text=message_text,
            reply_markup=keyboard
            )


async def task_list(update: Update, _):
    tasks = utils.get_some_tasks()  # TODO: get tasks from support center
    keyboard = keyboards.task_list_keyboard(tasks)
    await update.callback_query.edit_message_text(
            text=messages.task_message,
            reply_markup=keyboard
            )


async def delete_task(update: Update, context):
    task = utils.get_task_by_callback_data(update.callback_query.data)
    # TODO: make it a class method
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
    keyboard = keyboards.task_list_keyboard(tasks)
    await update.message.reply_text(
        text=messages.task_message,
        reply_markup=keyboard
    )
    return -1
    # return await task_list(update, context)


async def add_task(update: Update, context):
    await update.callback_query.edit_message_text(
        "Ok. You can write your task to me, i will track it for you"
    )
    return 0
