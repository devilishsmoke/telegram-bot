import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# получаем токен из переменных окружения Railway
TOKEN = os.getenv("BOT_TOKEN")

# Хэндлер для обработки сообщений
async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return  # игнорируем пустые сообщения и вложения

    text = update.message.text.lower()

    if "привет" in text:
        await update.message.reply_video(video=open("gprivet.mp4", "rb"))
    elif "люди" in text:
        await update.message.reply_video(video=open("lyudi.mp4", "rb"))
    # если нет ключевых слов — бот молчит

# Запуск бота
def main():
    app = Application.builder().token(TOKEN).build()

    # обработка только текстовых сообщений
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

    print("✅ Бот запущен! Railway его держит в онлайне 🚀")
    app.run_polling()

if __name__ == "__main__":
    main()
