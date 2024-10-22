import logging

from telegram import Update
from telegram.ext import ContextTypes, CallbackQueryHandler

from sc.interfaces import RequestInterface, RequestTaskInterface
import messages
import keyboards


logger = logging.getLogger(__name__)

async def to_work_action(update: Update, context: ContextTypes.DEFAULT_TYPE):
    request_id = context.user_data["request_id"]
    logger.info(f"To work request {request_id}")
    RequestInterface.to_work(request_id)
    context.user_data["request_id"] = request_id
    request = RequestInterface.get(request_id)
    request_tasks = RequestTaskInterface.list(request.id)
    await update.callback_query.answer("Yo")
    message_text = messages.request_template(request)
    keyboard = keyboards.request_keyboard(request, request_tasks)
    await update.callback_query.edit_message_text(
        text=message_text,
        reply_markup=keyboard
    )


to_work_handler = CallbackQueryHandler(
    to_work_action, "to_work"
)