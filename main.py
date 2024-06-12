import os
import logging

from telegram.ext import ApplicationBuilder

from handlers import my_handlers


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


async def error_handler(update, context):
    if update is None:
        return
    logging.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    TOKEN = os.getenv("BOTTOKEN")
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_error_handler(error_handler)
    application.add_handlers(my_handlers)
    application.run_polling()


if __name__ == "__main__":
    main()
