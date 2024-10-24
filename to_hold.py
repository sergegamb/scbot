import logging
import time

from telegram import Update
from telegram.ext import ContextTypes, CallbackQueryHandler

from sc.interfaces import RequestInterface, RequestTaskInterface
import messages
import keyboards


logger = logging.getLogger(__name__)


async def to_hold_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    request_id = context.user_data["request_id"]
    logger.info(f"To hold request {request_id}")
    RequestInterface.to_hold(request_id)
    context.user_data["request_id"] = request_id
    await update.callback_query.answer("Приостановлено")
    context.user_data["end_time"] = int(time.time())
    request = RequestInterface.get(request_id)
    request_tasks = RequestTaskInterface.list(request.id)
    message_text = messages.request_template(request)
    keyboard = keyboards.request_keyboard(request, request_tasks)
    await update.callback_query.edit_message_text(
        text=message_text,
        reply_markup=keyboard
    )


to_hold_handler = CallbackQueryHandler(
    to_hold_callback, "to_hold"
)