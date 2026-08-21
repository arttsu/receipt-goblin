import logging

from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

from receipt_goblin.bot import Bot
from receipt_goblin.environment import Environment

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


def main() -> None:
    env = Environment.from_os_env()
    bot = Bot(env)
    application = ApplicationBuilder().token(env.token).build()
    start_handler = CommandHandler("start", bot.start)
    fallback_handler = MessageHandler(filters.ALL, bot.fallback)
    application.add_handler(start_handler)
    application.add_handler(fallback_handler)
    application.run_polling()
