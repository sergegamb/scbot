import os
import logging
import warnings

from bs4 import GuessedAtParserWarning
from telegram.ext import ApplicationBuilder
from urllib3.exceptions import InsecureRequestWarning
from dotenv import load_dotenv

load_dotenv()

from add_worklog import add_worklog_handler
from task_to_done import task_to_done_handler
from to_hold import to_hold_handler
from to_work import to_work_handler


warnings.filterwarnings(
    action="ignore",
    category=InsecureRequestWarning
)
warnings.filterwarnings(
    action="ignore",
    category=GuessedAtParserWarning
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
    app.add_handler(to_work_handler)
    app.add_handler(to_hold_handler)
    app.add_handler(task_to_done_handler)
    app.add_handler(add_worklog_handler)
    app.run_polling()


if __name__ == "__main__":
    main()
