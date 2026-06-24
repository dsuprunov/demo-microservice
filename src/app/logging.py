import json
import logging
import time

logging.Formatter.converter = time.gmtime
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)sZ %(levelname)-8s %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
    force=True,
)

logger = logging.getLogger("demo-microservice")


def write_log(level: str, **fields: object) -> None:
    logger.log(
        getattr(logging, level.upper(), logging.INFO),
        json.dumps(fields)
    )
