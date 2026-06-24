from dataclasses import asdict

import uvicorn
from environs import EnvValidationError
from fastapi import FastAPI

from app.config import load_config
from app.logging import write_log
from app.message import Message


app = FastAPI(
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
    lifespan=None,
)


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/ping")
def ping(message: Message) -> dict[str, str]:
    write_log("INFO", event="RECEIVED", **message.model_dump())
    return {"status": "ok"}


if __name__ == "__main__":
    try:
        app.state.config = load_config()
        write_log("INFO", event="STARTUP", **asdict(app.state.config))
    except EnvValidationError as error:
        write_log("ERROR", event="STARTUP", error=str(error))
        raise SystemExit(1) from None

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        access_log=False,
        log_level="warning",
        log_config=None,
    )
