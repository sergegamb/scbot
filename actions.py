from telegram import Update

import keyboards
import utils


async def request_view(update, request):
    request = utils.get_request_by_callback_data(update.callback_query.data)
    await update.callback_query.answer("Yo")
    # TODO: ask jpt to convert it to human readable text
    message_text = (
            f"#{request.id} {request.subject}\n"
            f"\n{request.short_description}"
            )
    keyboard = keyboards.request_keyboard()
    await update.callback_query.edit_message_text(
            text=message_text,
            reply_markup=keyboard
            )


async def request_list(update, _):
    requests = utils.get_some_requests()
    keyboard = keyboards.request_list_keyboard(requests)
    await update.callback_query.edit_message_text(
            text="requests",
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
