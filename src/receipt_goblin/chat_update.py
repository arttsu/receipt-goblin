from dataclasses import dataclass

from telegram import PhotoSize, Update

from receipt_goblin.environment import Environment


@dataclass
class ChatUpdate:
    chat_id: int
    underlying: Update

    @classmethod
    def from_update(cls, update: Update, env: Environment) -> "ChatUpdate":
        if not (update.effective_chat and update.effective_user):
            raise ValueError

        return ChatUpdate(chat_id=update.effective_chat.id, underlying=update)


@dataclass
class PhotoUpdate(ChatUpdate):
    chat_id: int
    photo: PhotoSize
    underlying: Update

    @classmethod
    def from_update(cls, update: Update, env: Environment) -> "PhotoUpdate":
        chat_update = ChatUpdate.from_update(update, env)

        if not (update.message and update.message.photo):
            raise ValueError

        photo = max(update.message.photo, key=lambda p: p.height)

        return PhotoUpdate(
            chat_id=chat_update.chat_id,
            photo=photo,
            underlying=update,
        )
