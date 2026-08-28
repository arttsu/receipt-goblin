import os
from dataclasses import dataclass


@dataclass
class Environment:
    token: str

    @classmethod
    def from_os_env(cls) -> "Environment":
        token = os.getenv("RECEIPT_GOBLIN_TOKEN")

        if not token:
            raise ValueError("'RECEIPT_GOBLIN_TOKEN' env variable is not set")

        return Environment(token=token)
