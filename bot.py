import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# получаем токен из переменных окружения
TOKEN = os.getenv("BOT_TOKEN")

# проверим токен
print(">>> TOKEN LOADED:", TOKEN[:10] if TOKEN else "NOT FOUND")

# хендлер сообщений
async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return
    text = update.message.text.lower()
    if "привет" in text:
        await update.message.reply_text("Привет 👋")
    elif "люди" in text:
        await update.message.reply_text("Видео будет тут 📹")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))
    print("🤖 Бот запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()
