import logging
import os
import sys

from logging import config
from pathlib import Path

from rich.logging import RichHandler


ROOT_DIR = os.getcwd()

LOG_DIR = Path(ROOT_DIR, "logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)


logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "minimal": {"format": "%(message)s"},  # LogRecord attributes
        "detailed": {
            "format": "%(levelname)s %(asctime)s [%(name)s:%(filename)s:%(funcName)s:%(lineno)d]\n%(message)s\n"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "stream": sys.stdout,
            "formatter": "minimal",
            "level": logging.DEBUG,
        },
        "info": {
            "class": "logging.handlers.RotatingFileHandler",  # create new log file on every run
            "filename": Path(LOG_DIR, "info.log"),
            "maxBytes": 10485760,
            "backupCount": 10,
            "formatter": "detailed",
            "level": logging.INFO,
        },
        "error": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": Path(LOG_DIR, "error.log"),
            "maxBytes": 10485760,
            "backupCount": 10,
            "formatter": "detailed",
            "level": logging.ERROR,
        },
    },
    "root": {"handler": ["console", "info", "error"], "level": logging.INFO, "propagate": True},
}

config.dictConfig(logging_config)
logger = logging.getLogger()
logger.handlers.append(RichHandler(markup=True))
