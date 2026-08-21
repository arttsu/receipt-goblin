import logging

from telegram import Update
from telegram.ext import ContextTypes

from receipt_goblin.chat_update import ChatUpdate
from receipt_goblin.environment import Environment


class Bot:
    def __init__(self, env: Environment) -> None:
        self.logger = logging.getLogger(__name__)
        self.env = env

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        self.logger.info(f"START; {update}")  # TODO: -> debug

        chat_update = ChatUpdate.from_update(update, self.env)

        if chat_update.authorized:
            await context.bot.send_message(
                chat_id=chat_update.chat_id, text="FEED ME RECEIPTS!"
            )
        else:
            # TODO: Log warning
            await context.bot.send_message(
                chat_id=chat_update.chat_id, text="I DON'T KNOW YOU!"
            )

    async def fallback(
        self, update: Update, _context: ContextTypes.DEFAULT_TYPE
    ) -> None:
        self.logger.info(f"FALLBACK; {update}")  # TODO: -> debug
