import asyncio
from contextlib import asynccontextmanager
from dataclasses import asdict
from typing import AsyncIterator

from environs import EnvValidationError
from fastapi import FastAPI

from app.config import load_config
from app.logging import write_log
from app.message import Message
from app.sender import sender_loop


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    try:
        app.state.config = load_config()
        write_log("INFO", event="STARTUP", **asdict(app.state.config))
    except EnvValidationError as error:
        write_log("ERROR", event="STARTUP", error=str(error))
        raise

    sender_task = asyncio.create_task(sender_loop(app.state.config))

    try:
        yield
    finally:
        sender_task.cancel()
        try:
            await sender_task
        except asyncio.CancelledError:
            pass
        write_log("INFO", event="SHUTDOWN", **asdict(app.state.config))


app = FastAPI(
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
    lifespan=lifespan,
)


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/ping")
def ping(message: Message) -> dict[str, str]:
    write_log("INFO", event="RECEIVED", **message.model_dump())
    return {"status": "ok"}
