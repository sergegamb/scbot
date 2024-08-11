from warnings import filterwarnings
from telegram.warnings import PTBUserWarning
from telegram.ext import (
        CommandHandler,
        MessageHandler,
        CallbackQueryHandler,
        ConversationHandler
        )

from request_actions import (
        start_message,
        help_message,
        request_view,
        request_list,
        menu_command,
        menu_callback,
        get_request_task_title,
        add_request_task,
        )
from task_actions import (
        task_view,
        task_list,
        delete_task,
        add_task,
        get_task_title,
        request_task_view
        )
my_handlers = [
        CommandHandler("start", start_message),
        CommandHandler("help", help_message),
        CommandHandler("menu", menu_command),
        CallbackQueryHandler(menu_callback, "menu"),
        CallbackQueryHandler(request_task_view, "request_task_"),
        CallbackQueryHandler(request_view, "request_"),
        CallbackQueryHandler(request_list, "requests"),
        CallbackQueryHandler(task_view, "task_"),
        CallbackQueryHandler(task_list, "tasks"),
        CallbackQueryHandler(delete_task, "delete_task_"),
        ConversationHandler(
                entry_points=[CallbackQueryHandler(add_task, "add_task")],
                states={0: [MessageHandler(None, get_task_title)]},
                fallbacks=[],
                per_message=False,
        ),
        ConversationHandler(
                entry_points=[CallbackQueryHandler(add_request_task, "add_request_task_")],
                states={0: [MessageHandler(None, get_request_task_title)]},
                fallbacks=[],
                per_message=False,
        )
        ]

filterwarnings(action="ignore", message=r"If.*", category=PTBUserWarning)
