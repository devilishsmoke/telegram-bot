from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Пути к видео (файлы лежат рядом с bot.py)
VIDEO_HELLO = "gprivet.mp4"
VIDEO_PEOPLE = "lyudi.mp4"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "привет" in text:
        with open(VIDEO_HELLO, "rb") as video:
            await update.message.reply_video(video=video)
    elif "люди" in text:
        with open(VIDEO_PEOPLE, "rb") as video:
            await update.message.reply_video(video=video)

def main():
    import os
    TOKEN = os.getenv("BOT_TOKEN")  # токен из переменных окружения
    if not TOKEN:
        print(">>> TOKEN NOT FOUND")
        return

    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
