from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8002113464:AAHjClyZmVu6WOmn-sx-t4pDBCaLilWf-9k"

menu = ReplyKeyboardMarkup([
    ["💳 Оплата"],
    ["🎥 Курсы"],
    ["🔁 Возврат"],
    ["💆‍♀️ Массаж"],
    ["📩 Поддержка"]
], resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет 👋 Выберите раздел:", reply_markup=menu)

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Вы выбрали: " + update.message.text)

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

app.run_polling()
