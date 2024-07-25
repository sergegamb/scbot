from telegram import Update

import keyboards
import messages
from sc.interfaces import TaskInterface


async def task_view(update: Update, _):
    task_id = update.callback_query.data.split("_")[-1]
    task = TaskInterface.get(task_id)
    await update.callback_query.answer("Yoy")
    message_text = f"#{task.id}\n{task.title}"
    keyboard = keyboards.task_keyboard(task)
    await update.callback_query.edit_message_text(
            text=message_text,
            reply_markup=keyboard
            )


async def task_list(update: Update, _):
    tasks = TaskInterface.list()
    keyboard = keyboards.task_list_keyboard(tasks)
    await update.callback_query.edit_message_text(
            text=messages.task_message,
            reply_markup=keyboard
            )


async def delete_task(update: Update, _):
    task_id = update.callback_query.data.split("_")[-1]
    TaskInterface.delete(task_id)
    return await task_list(update, _)


async def get_task_title(update: Update, _):
    TaskInterface.add(title=update.message.text)
    tasks = TaskInterface.list()
    keyboard = keyboards.task_list_keyboard(tasks)
    await update.message.reply_text(
        text=messages.task_message,
        reply_markup=keyboard
    )
    return -1


async def add_task(update: Update, _):
    await update.callback_query.edit_message_text(
        "Ok. You can write your task to me, i will track it for you"
    )
    return 0
