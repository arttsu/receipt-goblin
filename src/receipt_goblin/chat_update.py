from dataclasses import dataclass

from telegram import Update

from receipt_goblin.environment import Environment


@dataclass
class ChatUpdate:
    authorized: bool
    chat_id: int
    underlying: Update

    @classmethod
    def from_update(cls, update: Update, env: Environment) -> "ChatUpdate":
        if not (update.effective_chat and update.effective_user):
            raise ValueError

        authorized = update.effective_user.username == env.username

        return ChatUpdate(
            authorized=authorized, chat_id=update.effective_chat.id, underlying=update
        )
