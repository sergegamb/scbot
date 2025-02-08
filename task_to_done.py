import logging

from telegram import Update
from telegram.ext import ContextTypes, CallbackQueryHandler

from sc.interfaces import TaskInterface, RequestTaskInterface, RequestInterface
import messages
import keyboards
from tech import TECHNICIANS


logger = logging.getLogger(__name__)


async def task_to_done_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = TECHNICIANS.get(update.callback_query.from_user.id)
    logger.info(f"Receive {update.callback_query.data} callback from {user}")
    task_id = context.user_data["task_id"]
    logger.info(f"{task_id=}")
    TaskInterface.to_done(task_id)
    await update.callback_query.answer("Выполнена")
    task = TaskInterface.get(task_id)
    await update.callback_query.answer("Yoy")
    message_text = f"#{task.id}\n{task.title}"
    keyboard = keyboards.task_keyboard(task)
    await update.callback_query.edit_message_text(
        text=message_text,
        reply_markup=keyboard
    )


async def request_task_to_done_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = TECHNICIANS.get(update.callback_query.from_user.id)
    logger.info(f"Receive {update.callback_query.data} callback from {user}")
    task_id = context.user_data["task_id"]
    request_id = context.user_data["request_id"]
    logger.info(f"{task_id=}")
    RequestTaskInterface.to_done(request_id, task_id)
    await update.callback_query.answer("Выполнена")
    request = RequestInterface.get(request_id)
    request_tasks = RequestTaskInterface.list(request.id)
    message_text = messages.request_template(request)
    keyboard = keyboards.request_keyboard(request, request_tasks)
    await update.callback_query.edit_message_text(
        text=message_text,
        reply_markup=keyboard
    )


task_to_done_handler = CallbackQueryHandler(
    task_to_done_callback, "task_to_done"
)
request_task_to_done_handler = CallbackQueryHandler(
    request_task_to_done_callback, "request_task_to_done"
)