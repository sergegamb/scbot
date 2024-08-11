from telegram import Update

from sc.interfaces import RequestInterface, TaskInterface
import keyboards
import messages


async def request_view(update, _):
    request_id = update.callback_query.data.split("_")[-1]
    request = RequestInterface.get(request_id)
    request_tasks = TaskInterface.list_request_tasks(request.id)
    await update.callback_query.answer("Yo")
    message_text = messages.request_template(request)
    keyboard = keyboards.request_keyboard(request, request_tasks)
    await update.callback_query.edit_message_text(
            text=message_text,
            reply_markup=keyboard
            )


async def add_request_task(update: Update, context):
    request_id = update.callback_query.data.split("_")[-1]
    context.user_data["request_id"] = request_id
    await update.callback_query.edit_message_text(
        "Ok. You can write your task to me, i will track it for you"
    )
    return 0


async def get_request_task_title(update: Update, context):
    request_id = context.user_data.get('request_id')
    context.user_data.pop('request_id', None)
    TaskInterface.add_request_task(
        title=update.message.text,
        request_id=request_id,
    )
    request = RequestInterface.get(request_id)
    request_tasks = TaskInterface.list_request_tasks(request.id)
    keyboard = keyboards.request_keyboard(request, request_tasks)
    await update.message.reply_text(
        text=messages.request_template(request),
        reply_markup=keyboard
    )
    return -1


async def request_list(update, _):
    requests = RequestInterface.list()
    keyboard = keyboards.request_list_keyboard(requests)
    await update.callback_query.edit_message_text(
            text=messages.request_message,
            reply_markup=keyboard
            )


async def start_message(update, _):
    await update.message.reply_text("hi. what can i do for you?")

async def help_message(update, _):
    await update.message.reply_text("ok. here is help contact: @sgamb")

async def menu_command(update: Update, _):
    await update.message.reply_text(
        text="Menu",
        reply_markup=keyboards.menu_keyboard
    )

async def menu_callback(update: Update, _):
    await update.callback_query.edit_message_text(
        text="Menu",
        reply_markup=keyboards.menu_keyboard
    )
