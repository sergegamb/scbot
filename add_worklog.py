from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler, CallbackQueryHandler, MessageHandler

from sc.interfaces import BillingTimeEntryInterface

GET = 0

TECHNICIANS = {
    7602306060: "Сергей Гамбарян",
    33091521: "Илья Маракушев",
    122749292: "Павел Тетерин",
    119298025: "Василий Гусев",
    107551802: "Вадим Гусев",
    137511220: "Дмитрий Одинцов",
    5239813999: "Александр Михайлов"
}


async def add_worklog(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer("Хорошо")
    await update.callback_query.edit_message_text("Введите описание последнего ворклога")
    return GET


async def get_worklog_description(update: Update, context: ContextTypes.DEFAULT_TYPE):
    request_id = context.user_data["request_id"]
    owner = TECHNICIANS[update.message.from_user.id]
    start_time = context.user_data["start_time"]
    end_time = context.user_data["end_time"]
    description = update.message.text
    answer = BillingTimeEntryInterface.add(request_id, owner, start_time, end_time, description)
    await update.message.reply_text(answer)
    return ConversationHandler.END


add_worklog_handler = ConversationHandler(
    entry_points=[CallbackQueryHandler(add_worklog, "add_worklog")],
    states={GET: [MessageHandler(None, get_worklog_description)]},
    fallbacks=[],
    per_message=False,
)