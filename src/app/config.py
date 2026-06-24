from dataclasses import dataclass

from environs import Env


@dataclass(frozen=True)
class Config:
    service_id: str
    instance_id: str
    peers: list[str]
    interval: int
    timeout: int


def load_config() -> Config:
    env = Env()

    return Config(
        service_id=env.str("SERVICE_ID"),
        instance_id=env.str("INSTANCE_ID"),
        peers=env.json("PEERS"),
        interval=env.int("INTERVAL"),
        timeout=env.int("TIMEOUT"),
    )
