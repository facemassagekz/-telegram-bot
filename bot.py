import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Бот работает ✔")

app = app = Application.builder().token(TOKEN).build()
app.run_polling(drop_pending_updates=True)
app.add_handler(CommandHandler("start", start))

if __name__ == "__main__":
    app.run_polling(allowed_updates=Update.ALL_TYPES)
    
