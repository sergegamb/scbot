import logging

from telegram import Update
from telegram.ext import ContextTypes

import keyboards
import messages
from sc.interfaces import TaskInterface, RequestTaskInterface, RequestInterface
from tech import TECHNICIANS


logger = logging.getLogger(__name__)


async def task_view(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = TECHNICIANS.get(update.callback_query.from_user.id)
    logger.info(f"Receive {update.callback_query.data} from {user}")
    task_id = update.callback_query.data.split("_")[-1]
    context.user_data["task_id"] = task_id
    task = TaskInterface.get(task_id)
    await update.callback_query.answer("Yoy")
    message_text = f"#{task.id}\n{task.title}"
    keyboard = keyboards.task_keyboard(task)
    await update.callback_query.edit_message_text(
            text=message_text,
            reply_markup=keyboard
            )


async def request_task_view(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = TECHNICIANS.get(update.callback_query.from_user.id)
    logger.info(f"Receive {update.callback_query.data} from {user}")
    callback_data = update.callback_query.data.split("_")
    task_id = callback_data[-2]
    request_id = callback_data[-1]
    context.user_data["task_id"] = task_id
    context.user_data["request_id"] = request_id
    task = RequestTaskInterface.get(request_id, task_id)
    await update.callback_query.answer("Yo yo")
    message_text = f"#{task.id}\n{task.title}"
    keyboard = keyboards.request_task_keyboard(task)
    await update.callback_query.edit_message_text(
        text=message_text,
        reply_markup=keyboard
    )


async def task_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = TECHNICIANS.get(update.callback_query.from_user.id)
    logger.info(f"Receive tasks callback from {user} or next/previous page")
    page = context.user_data.get("tasks_page", 1)
    tasks = TaskInterface.list(page)
    keyboard = keyboards.task_list_keyboard(tasks, page)
    await update.callback_query.edit_message_text(
            text=messages.task_message,
            reply_markup=keyboard
            )


async def task_page(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = TECHNICIANS.get(update.callback_query.from_user.id)
    logger.info(f"Receive {update.callback_query.data} callback from {user}")
    if context.user_data.get("tasks_page") is None:
        context.user_data["tasks_page"] = 1
    if update.callback_query.data == "previous_tasks_page":
        context.user_data["tasks_page"] -= 1
    else:
        context.user_data["tasks_page"] += 1
    await task_list(update, context)


async def delete_task(update: Update, _):
    user = TECHNICIANS.get(update.callback_query.from_user.id)
    logger.info(f"Receive {update.callback_query.data} callback from {user}")
    task_id = update.callback_query.data.split("_")[-1]
    TaskInterface.delete(task_id)
    return await task_list(update, _)


async def delete_request_task(update: Update, _):
    task_id = update.callback_query.data.split("_")[-1]
    request_id = update.callback_query.data.split("_")[-2]
    RequestTaskInterface.delete(request_id, task_id)
    request = RequestInterface.get(request_id)
    request_tasks = RequestTaskInterface.list(request.id)
    keyboard = keyboards.request_keyboard(request, request_tasks)
    await update.callback_query.edit_message_text(
        text=messages.request_template(request),
        reply_markup=keyboard
    )


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
        messages.provide_task_title_message
    )
    return 0
