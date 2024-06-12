from telegram.ext import (
        CommandHandler,
        MessageHandler,
        CallbackQueryHandler
        )

from actions import (
        start_message,
        help_message,
        request_view,
        request_list
        )


my_handlers = [
        CommandHandler("start", start_message),
        CommandHandler("help", help_message),
        MessageHandler(None, request_list),
        CallbackQueryHandler(request_view, "request_"),
        CallbackQueryHandler(request_list, "requests"),
        ]
