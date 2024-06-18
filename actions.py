from telegram import Update
from telegram import (
        InlineKeyboardButton,
        InlineKeyboardMarkup,
        )

import utils


async def request_view(update, request):
    request = utils.get_request_by_callback_data(update.callback_query.data)
    await update.callback_query.answer("Yo")
    # TODO: ask jpt to convert it to human readable text
    message_text = (
            f"#{request.id} {request.subject}\n"
            f"\n{request.short_description}"
            )
    keyboard = InlineKeyboardButton(
            text="Go back to list view",
            callback_data="requests"
            )
    await update.callback_query.edit_message_text(
            text=message_text,
            reply_markup=InlineKeyboardMarkup.from_button(keyboard)
            )
    # telegram bot representation of Request
    # composed of text message ( title and discription )
    # and keyboard ( actions and go back )


async def request_list(update, context):
    requests = utils.get_some_requests()
    keyboard = utils.compose_keyboard(requests, "subject", "request")
    keyboard.append(
        InlineKeyboardButton(
            text="Go back",
            callback_data="menu",
        )
    )
    await update.callback_query.edit_message_text(
            text="requests",
            reply_markup=InlineKeyboardMarkup.from_column(keyboard)
            )

async def start_message(update, context):
    await update.message.reply_text("hi. what can i do for you?")

async def help_message(update, context):
    await update.message.reply_text("ok. here is help contact: @sgamb")

async def menu(update: Update, context):
    menu_keyboard = InlineKeyboardMarkup.from_column([
        InlineKeyboardButton(
            text="Requests",
            callback_data="requests",
        ),
        InlineKeyboardButton(
            text="Tasks",
            callback_data="tasks"
        )]
    )
    if update.message:
        await update.message.reply_text(
            text="Menu",
            reply_markup=menu_keyboard
        )
    else:
        await update.callback_query.edit_message_text(
            text="Menu",
            reply_markup=menu_keyboard
        )
