from telegram import Update, InlineKeyboardMarkup
from telegram.ext import ContextTypes, ConversationHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton

import logging



from request_actions import request_list

logger = logging.getLogger(__name__)
PICK = 0


async def filter_action(update: Update, _):
        logger.info("Choose filter view")
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
                                )
                        ]
                )
        )
        return PICK


async def pick_filter_action(update: Update, context: ContextTypes.DEFAULT_TYPE):
        chosen_filter = update.callback_query.data
        if chosen_filter.startswith("filter_all"):
                logger.info("Filter all was chosen")
                await update.callback_query.answer("All requests")
                context.user_data["filter"] = "all"
        elif chosen_filter.startswith("filter_my"):
                logger.info("Filter my was chosen")
                await update.callback_query.answer("Your requests")
                context.user_data["filter"] = "my"
        context.user_data["page"] = 0
        await request_list(update, context)
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

