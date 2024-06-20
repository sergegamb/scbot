from telegram.ext import (
        CommandHandler,
        MessageHandler,
        CallbackQueryHandler
        )

from actions import (
        start_message,
        help_message,
        request_view,
        request_list,
        menu
        )
from task_actions import (
        task_view,
        task_list,
        delete_task
        )

my_handlers = [
        CommandHandler("start", start_message),
        CommandHandler("help", help_message),
        CommandHandler("menu", menu),
        CallbackQueryHandler(menu, "menu"),
        CallbackQueryHandler(request_view, "request_"),
        CallbackQueryHandler(request_list, "requests"),
        CallbackQueryHandler(task_view, "task_"),
        CallbackQueryHandler(task_list, "tasks"),
        CallbackQueryHandler(delete_task, "delete_task_")
        ]

