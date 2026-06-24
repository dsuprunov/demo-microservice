import asyncio
from urllib.request import Request, urlopen

from app.config import Config
from app.logging import write_log
from app.message import Message, generate_message


def deliver_message(peer: str, message: Message, timeout: int) -> None:
    try:
        request = Request(
            peer,
            data=message.model_dump_json().encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="GET",
        )

        with urlopen(request, timeout=timeout) as response:
            response.read()

        write_log("INFO", event="DELIVERED", peer=peer, **message.model_dump())
    except Exception as error:
        write_log("ERROR", event="FAILED", peer=peer, error=str(error), **message.model_dump())


async def sender_loop(config: Config) -> None:
    while True:
        for peer in config.peers:
            message = generate_message(config)
            await asyncio.to_thread(
                deliver_message,
                peer,
                message,
                config.timeout,
            )

        await asyncio.sleep(config.interval)
