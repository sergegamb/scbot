import os
import logging

from telegram.ext import ApplicationBuilder

from handlers import my_handlers


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logging.getLogger("httpx").setLevel(logging.WARNING)


async def error_handler(update, context):
    if update is None:
        return
    logging.warning('Update caused error "%s"', context.error)


def main():
    app = ApplicationBuilder().token(os.getenv("BOTTOKEN")).build()
    app.add_error_handler(error_handler)
    app.add_handlers(my_handlers)
    app.run_polling()


if __name__ == "__main__":
    main()
