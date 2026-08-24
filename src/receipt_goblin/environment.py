import os
from dataclasses import dataclass


@dataclass
class Environment:
    token: str
    corrections_path: str

    @classmethod
    def from_os_env(cls) -> "Environment":
        token = os.getenv("RECEIPT_GOBLIN_TOKEN")

        if not token:
            raise ValueError("'RECEIPT_GOBLIN_TOKEN' env variable is not set")

        corrections_path = os.getenv("RECEIPT_GOBLIN_CORRECTIONS_PATH")

        if not corrections_path:
            raise ValueError("'RECEIPT_GOBLIN_CORRECTIONS_PATH' env variable is not set")

        return Environment(token=token, corrections_path=corrections_path)
