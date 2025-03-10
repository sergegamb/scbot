import logging

from telegram import Update, InlineKeyboardButton
from telegram.ext import CallbackQueryHandler, ContextTypes

from sc.interfaces import RequestInterface
import messages
import keyboards
from tech import TECHNICIANS


logger = logging.getLogger(__name__)

def requests_by_filter(update, context):
    if context.user_data.get("filter") is None:
        context.user_data["filter"] = "my"
    if context.user_data.get("page") is None:
        context.user_data["page"] = 0
    if context.user_data["filter"] == "all":
        requests = RequestInterface.list_all(context.user_data["page"])
    elif context.user_data["filter"] == "my":
        requests = RequestInterface.list_technician(
            context.user_data["page"],
            TECHNICIANS[update.callback_query.from_user.id]
        )
    else:  # groups
        requests = RequestInterface.list_technician_group(
            context.user_data["page"],
            TECHNICIANS[update.callback_query.from_user.id]
        )
    return requests

# DUPLICATE
async def request_list_view(update: Update, context: ContextTypes.DEFAULT_TYPE, requests):
    page = context.user_data["page"]
    await update.callback_query.answer(f"Requests page {page}")
    keyboard = keyboards.request_list_keyboard(requests, context.user_data.get("filter"))
    await update.callback_query.edit_message_text(
            text=messages.request_message,
            reply_markup=keyboard
            )


async def next_page_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = TECHNICIANS[update.callback_query.from_user.id]
    logger.info(f"Receive next_page callback query from {user}")
    try:
        context.user_data["page"] += 1
    except KeyError:
        context.user_data["page"] = 0
    logger.info(context.user_data)
    requests = requests_by_filter(update, context)
    await request_list_view(update, context, requests)


async def previous_page_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = TECHNICIANS[update.callback_query.from_user.id]
    logger.info(f"Receive prev_page callback query from {user}")
    try:
        context.user_data["page"] -= 1
        if context.user_data["page"] < 0:
            context.user_data["page"] = 0
            # TODO: Do not display Previous page button on the first page
    except KeyError:
        context.user_data["page"] = 0
    logger.info(context.user_data)
    requests = requests_by_filter(update, context)
    await request_list_view(update, context, requests)


next_page_handler = CallbackQueryHandler(next_page_callback, "next_page_requests")
previous_page_handler = CallbackQueryHandler(previous_page_callback, "previous_page_requests")


paging_handlers = [next_page_handler, previous_page_handler]