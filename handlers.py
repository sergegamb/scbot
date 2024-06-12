import json

from telegram.ext import CommandHandler, MessageHandler
from telegram import (
        InlineKeyboardButton,
        InlineKeyboardMarkup,
        )


from pydantic import BaseModel

from request_model import Model


my_handlers = []

async def start(update, context):
    await update.message.reply_text("hi. what can i do for you?")

start_handler = CommandHandler("start", start)

async def list_requests(update, context):
    # read from file
    with open("requests.json", "r") as f:
        data = f.read()
    # convert to dict
    json_data = json.loads(data)
    # convert to pydantic
    pydantic_data = Model(**json_data)
    # extract requests from response
    requests = pydantic_data.requests
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
                callback_data="request" + req.get("id")
                )
                ]
            )
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
            "requests",
            reply_markup=reply_markup
            )

message_handler = MessageHandler(None, list_requests)

my_handlers.append(start_handler)
my_handlers.append(message_handler)
