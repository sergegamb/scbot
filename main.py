import os
import logging
import warnings

from telegram.ext import ApplicationBuilder
from telegram.warnings import PTBUserWarning
from urllib3.exceptions import InsecureRequestWarning

warnings.filterwarnings(
    action="ignore",
    message=r".*CallbackQueryHandler",
    category=PTBUserWarning
)
warnings.filterwarnings(
    action="ignore",
    category=InsecureRequestWarning
)

from handlers import my_handlers
from filters import filters_handler
from paging import paging_handlers


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s'
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
    app.add_handler(filters_handler)
    app.add_handlers(paging_handlers)
    app.run_polling()


if __name__ == "__main__":
    main()
