from telegram import Update
from telegram.ext import ContextTypes

from paging import requests_by_filter, request_list_view
from sc.interfaces import RequestInterface, RequestTaskInterface
import keyboards
import messages
from tech import TECHNICIANS

import logging


logger = logging.getLogger(__name__)


async def request_view(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = TECHNICIANS.get(update.callback_query.from_user.id)
    logger.info(f"Receive {update.callback_query.data} from {user}")
    request_id = update.callback_query.data.split("_")[-1]
    context.user_data["request_id"] = request_id
    logger.info(context.user_data)
    request = RequestInterface.get(request_id)
    request_tasks = RequestTaskInterface.list(request.id)
    await update.callback_query.answer("Yo")
    message_text = messages.request_template(request)
    keyboard = keyboards.request_keyboard(request, request_tasks)
    await update.callback_query.edit_message_text(
            text=message_text,
            reply_markup=keyboard
            )


async def add_request_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = TECHNICIANS[update.callback_query.from_user.id]
    logger.info(f"Receive {update.callback_query.data} from {user}")
    logger.info(context.user_data)
    await update.callback_query.edit_message_text(
        messages.provide_task_title_message
    )
    return 0


async def get_request_task_title(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = TECHNICIANS[update.message.from_user.id]
    logger.info(f"Receive task - {update.message.text} from {user}")
    request_id = context.user_data.get('request_id')
    RequestTaskInterface.add(
        title=update.message.text,
        request_id=request_id,
    )
    # Request display
    request = RequestInterface.get(request_id)
    request_tasks = RequestTaskInterface.list(request.id)
    keyboard = keyboards.request_keyboard(request, request_tasks)
    await update.message.reply_text(
        text=messages.request_template(request),
        reply_markup=keyboard
    )
    return -1


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = TECHNICIANS[update.message.from_user.id]
    logger.info(f"User {user} canceled task add.")
    await update.message.reply_text(
        "Bye!"
    )
    #TODO: return request view
    return -1




async def request_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = TECHNICIANS.get(update.callback_query.from_user.id)
    logger.info(f"List requests: receive requests callback from {user}")
    logger.info(context.user_data)
    requests = requests_by_filter(update, context)
    await request_list_view(update, context, requests)


async def start_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = TECHNICIANS.get(update.message.from_user.id)
    logger.info(f"Receive /start command from {user}")
    if user is None:
        await update.message.reply_text(
            text=messages.unknown_user
        )
        return
    context.user_data["filter"] = "my"
    await update.message.reply_text(
        text=messages.menu,
        reply_markup=keyboards.menu_keyboard
    )

async def help_message(update, _):
    await update.message.reply_text(messages.help_message)

async def menu_command(update: Update, _):
    await update.message.reply_text(
        text=messages.menu,
        reply_markup=keyboards.menu_keyboard
    )

async def menu_callback(update: Update, _):
    user = TECHNICIANS.get(update.callback_query.from_user.id)
    logger.info(f"Receive menu callback from {user}")
    await update.callback_query.edit_message_text(
        text=messages.menu,
        reply_markup=keyboards.menu_keyboard
    )
