import logging
from pathlib import Path

from openai import OpenAI
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from receipt_goblin.chat_update import ChatUpdate, PhotoUpdate
from receipt_goblin.environment import Environment


class Bot:
    def __init__(self, env: Environment) -> None:
        self.logger = logging.getLogger(__name__)
        self.env = env
        self.openai = OpenAI()
        self.system_message = Path("resources/system_message.md").read_text()
        self.corrections = Path("resources/corrections.md").read_text()

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

    async def process_photo(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ) -> None:
        self.logger.info(f"PROCESS_PHOTO; {update}")  # TODO: -> debug

        photo_update = PhotoUpdate.from_update(update, self.env)

        if photo_update.authorized:
            file = await photo_update.photo.get_file()

            self.logger.info("Processing a receipt...")
            await context.bot.send_message(photo_update.chat_id, text="Processing...")

            response = self.openai.responses.create(
                model="gpt-5.6",
                input=[
                    {
                        "role": "developer",
                        "content": [
                            {"type": "input_text", "text": self.system_message}
                        ],
                    },
                    {
                        "role": "developer",
                        "content": [{"type": "input_text", "text": self.corrections}],
                    },
                    {
                        "role": "user",
                        "content": [
                            {"type": "input_image", "image_url": file.file_path}
                        ],
                    },
                ],
            )
            output = response.output_text
            await context.bot.send_message(
                photo_update.chat_id, text=output, parse_mode=ParseMode.MARKDOWN_V2
            )
        else:
            # TODO: Log warning
            await context.bot.send_message(
                chat_id=photo_update.chat_id, text="I DON'T KNOW YOU!"
            )

    async def fallback(
        self, update: Update, _context: ContextTypes.DEFAULT_TYPE
    ) -> None:
        self.logger.info(f"FALLBACK; {update}")  # TODO: -> debug
