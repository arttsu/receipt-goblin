import logging

from telegram import Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f"START; {update}")

    if not update.effective_chat:
        raise ValueError

    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="FEED ME RECEIPTS!"
    )


async def fallback(update: Update, _context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info(f"FALLBACK; {update}")
