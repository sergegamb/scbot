from telegram import Update, InlineKeyboardButton
from telegram.ext import CallbackQueryHandler, ContextTypes

from sc.interfaces import RequestInterface
import messages
import keyboards


next_page  = InlineKeyboardButton(
    text="Next page",
    callback_data="next_page"
    )
previous_page = InlineKeyboardButton(
    text="Previous page",
    callback_data="previous_page"
)

TECHNICIANS = {
    7602306060: "Сергей Гамбарян",
    33091521: "Илья Маракушев",
    122749292: "Павел Тетерин",
    119298025: "Василий Гусев",
    107551802: "Вадим Гусев",
    137511220: "Дмитрий Одинцов",
    5239813999: "Александр Михайлов"
}


# DUPLICATE
async def request_list_view(update: Update, context: ContextTypes.DEFAULT_TYPE):
    page = context.user_data["page"]
    requester_tg_id = update.callback_query.from_user.id
    technician_name = TECHNICIANS[requester_tg_id]
    await update.callback_query.answer(f"Requests page {page}")
    if context.user_data.get("filter") == "my":
        requests = RequestInterface.list(page, technician_name)
    else:
        requests = RequestInterface.list(page)
    keyboard = keyboards.request_list_keyboard(requests, context.user_data.get("filter"))
    await update.callback_query.edit_message_text(
            text=messages.request_message,
            reply_markup=keyboard
            )


async def next_page_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        context.user_data["page"] += 1
    except KeyError:
        context.user_data["page"] = 0
    await request_list_view(update, context)


async def previous_page_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        context.user_data["page"] -= 1
        if context.user_data["page"] < 0:
            context.user_data["page"] = 0
            # TODO: Do not display Previous page button on the first page
    except KeyError:
        context.user_data["page"] = 0
    await request_list_view(update, context)


next_page_handler = CallbackQueryHandler(next_page_callback, "next_page")
previous_page_handler = CallbackQueryHandler(previous_page_callback, "previous_page")


paging_handlers = [next_page_handler, previous_page_handler]