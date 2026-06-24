from collections.abc import Callable
from datetime import UTC, datetime
from itertools import count
from uuid import uuid4

from pydantic import BaseModel

from app.config import Config


class Message(BaseModel):
    message_id: str
    service_id: str
    instance_id: str
    timestamp: str
    payload: str


def create_message_generator() -> Callable[[Config], Message]:
    message_sequence = count(1)

    def generate_message(config: Config) -> Message:
        sequence_number = next(message_sequence)

        return Message(
            message_id=str(uuid4()),
            service_id=config.service_id,
            instance_id=config.instance_id,
            timestamp=datetime.now(UTC)
            .replace(microsecond=0)
            .isoformat()
            .replace("+00:00", "Z"),
            payload=f"msg-{sequence_number:06d}",
        )

    return generate_message


generate_message = create_message_generator()
