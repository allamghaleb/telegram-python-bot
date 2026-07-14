import os
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "مرحبًا بك 👋\n"
        "أنا بوت Telegram بسيط مبني باستخدام Python.\n\n"
        "اكتب /help لمعرفة الأوامر المتاحة."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "الأوامر المتاحة:\n\n"
        "/start - تشغيل البوت\n"
        "/help - عرض المساعدة\n"
        "/about - معلومات عن المشروع\n\n"
        "أرسل أي رسالة وسأعيدها لك."
    )


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "هذا مشروع تعليمي بسيط لبناء Telegram Bot باستخدام Python.\n"
        "الهدف: تعلم البوتات، التعامل مع API، وتنظيم المشروع على GitHub."
    )


async def echo_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    await update.message.reply_text(f"أنت كتبت: {user_text}")


def main():
    if not BOT_TOKEN:
        raise ValueError(
            "BOT_TOKEN غير موجود. أنشئ ملف .env وضع التوكن داخله."
        )

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_message))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
