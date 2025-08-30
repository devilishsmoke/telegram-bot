from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# 🔑 Токен бота
TOKEN = "8412312571:AAFRTFSxKg9LlhOk4HadxMIZ85YTY7LegS4"

# 🔑 Хэндлер для обработки сообщений
async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return  # Игнорируем пустые сообщения и вложения

    text = update.message.text.lower()

    if "привет" in text:
        await update.message.reply_video(video=open("gprivet.mp4", "rb"))
    elif "люди" in text:
        await update.message.reply_video(video=open("lyudi.mp4", "rb"))
    # если нет ключевых слов — бот молчит

# 🚀 Запуск бота
def main():
    app = Application.builder().token(TOKEN).build()

    # Обработка только текстовых сообщений
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

    print("🤖 Бот запущен! Нажми Ctrl+C для остановки.")
    app.run_polling()

if __name__ == "__main__":
    main()
