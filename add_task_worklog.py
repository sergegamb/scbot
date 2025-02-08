import logging
import time

from telegram import Update
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
    CallbackQueryHandler,
    MessageHandler,
    CommandHandler,
    filters
)

from sc.interfaces import GeneralTaskTimeEntryInterface
from messages import add_worklog_message
from tech import TECHNICIANS

GET = 0

logger = logging.getLogger(__name__)


async def add_worklog(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = TECHNICIANS[update.callback_query.from_user.id]
    logger.info(f"Receive {update.callback_query.data} from {user}")
    await update.callback_query.answer("Хорошо")
    await update.callback_query.edit_message_text(add_worklog_message)
    return GET


async def get_worklog_description(update: Update, context: ContextTypes.DEFAULT_TYPE):
    task_id = context.user_data["task_id"]
    owner = TECHNICIANS[update.message.from_user.id]
    logger.info(f"Receive task worklog {update.message.text} from {owner}")
    end_time = int(time.time()) * 1000
    hours = 1
    description = update.message.text
    if description[0] == '+':
        hours = 0
        while description[0] == '+':
            description = description[1:]
            hours += 1
    start_time = end_time - hours * 3600000
    answer = GeneralTaskTimeEntryInterface.add(task_id, owner, start_time, end_time, description)
    await update.message.reply_text(answer)
    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = TECHNICIANS[update.message.from_user.id]
    logger.info(f"User {user} canceled worklog add.")
    await update.message.reply_text(
        "Bye!"
    )
    return ConversationHandler.END


add_task_worklog_handler = ConversationHandler(
    entry_points=[CallbackQueryHandler(add_worklog, "add_task_worklog")],
    states={GET: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_worklog_description)]},
    fallbacks=[CommandHandler("cancel", cancel)],
    per_message=False,
)