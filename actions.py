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
    # composed from text message ( title and discription )
    # and keyboard ( actions and go back )


async def request_list(update, context):
    requests = utils.get_some_requests()
    # prepare simplifyed data
    simplifyed_requests = []
    for req in requests:
        simplifyed_requests.append(req.representation())
    # prepare keyboard
    keyboard = []
    for req in simplifyed_requests:
        keyboard.append(
            [InlineKeyboardButton(
                text=req.get("id") + " " + req.get("subject"),
                callback_data="request_" + req.get("id")
                )
                ]
            )
    reply_markup = InlineKeyboardMarkup(keyboard)
    try:
        await update.message.reply_text(
                text="requests",
                reply_markup=reply_markup
                )
    except:
        await update.callback_query.edit_message_text(
                text="requests",
                reply_markup=reply_markup
                )

async def start_message(update, context):
    await update.message.reply_text("hi. what can i do for you?")

async def help_message(update, context):
    await update.message.reply_text("ok. here is help contact: @sgamb")
