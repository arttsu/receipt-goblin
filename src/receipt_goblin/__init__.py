import logging
import os

from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

import receipt_goblin.bot

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


def main() -> None:
    token = os.getenv("RECEIPT_GOBLIN_TOKEN")

    if not token:
        raise ValueError

    application = ApplicationBuilder().token(token).build()
    start_handler = CommandHandler("start", receipt_goblin.bot.start)
    fallback_handler = MessageHandler(filters.ALL, receipt_goblin.bot.fallback)
    application.add_handler(start_handler)
    application.add_handler(fallback_handler)
    application.run_polling()
