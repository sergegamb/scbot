from telegram import Update, InlineKeyboardMarkup
from telegram.ext import ContextTypes, ConversationHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton

import logging

from paging import request_list_view
from sc.interfaces import RequestInterface
from tech import TECHNICIANS

logger = logging.getLogger(__name__)
PICK = 0


async def filter_action(update: Update, _):
    user = TECHNICIANS[update.callback_query.from_user.id]
    logger.info(f"Choose filter view: receive filters callback from {user}")
    await update.callback_query.answer("Which one?")
    await update.callback_query.edit_message_text(
        text="Choose a filter",
        reply_markup=InlineKeyboardMarkup.from_column(
            [
                InlineKeyboardButton(
                    text="All requests",
                    callback_data="filter_all"
                ),
                InlineKeyboardButton(
                    text="My requests",
                    callback_data="filter_my"
                ),
                InlineKeyboardButton(
                    text="All my groups",
                    callback_data="filter_all_my_groups"
                )
            ]
        )
    )
    return PICK


# TODO: use function request_by_filter
async def pick_filter_action(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chosen_filter = update.callback_query.data
    technician = TECHNICIANS[update.callback_query.from_user.id]
    logger.info(f"Filter {chosen_filter} was chosen by {technician}")
    if chosen_filter == "filter_all":
        await update.callback_query.answer("All requests")
        context.user_data["filter"] = "all"
        requests = RequestInterface.list_all(0)
    elif chosen_filter.startswith("filter_my"):
        await update.callback_query.answer("Your requests")
        context.user_data["filter"] = "my"
        requests = RequestInterface.list_technician(0, technician)
    else: # chosen_filter.startswith("filter_all_my_groups"):
        await update.callback_query.answer("All your groups")
        context.user_data["filter"] = "all_my_groups"
        requests = RequestInterface.list_technician_group(0, technician)
    context.user_data["page"] = 0
    logger.info(context.user_data)
    await request_list_view(update, context, requests)
    return ConversationHandler.END

filters_handler = ConversationHandler(
    entry_points=[
        CallbackQueryHandler(
            filter_action,
            "filters"
        )
    ],
    states={
        PICK: [
            CallbackQueryHandler(
                pick_filter_action
            )
        ]
    },
    fallbacks=[],
    per_message=False,
)

