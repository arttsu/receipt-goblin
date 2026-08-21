import os
from dataclasses import dataclass


@dataclass
class Environment:
    username: str
    token: str

    @classmethod
    def from_os_env(cls) -> "Environment":
        username = os.getenv("RECEIPT_GOBLIN_USERNAME")

        if not username:
            raise ValueError("'RECEIPT_GOBLIN_USERNAME' env variable is not set")

        token = os.getenv("RECEIPT_GOBLIN_TOKEN")

        if not token:
            raise ValueError("'RECEIPT_GOBLIN_TOKEN' env variable is not set")

        return Environment(username=username, token=token)
