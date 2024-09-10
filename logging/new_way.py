""" This is learning new way of logging module """

import atexit
import json
import logging.config
import logging.handlers
from logging.handlers import QueueHandler, QueueListener
from queue import Queue
import pathlib

# Global logger instance
logger = logging.getLogger("my_app")


def setup_logging() -> None:
    """
    This is setup for logging module.
    List of config files:
    - stderr-file.json
    - filtered-stdout-stderr.json
    - queued-json-stderr.json
    - queued-stderr-json-file.json
    - stderr-json-file.json
    - my_config.json
    """

    # Load the logging configuration from JSON file
    config_file = pathlib.Path("logging_configs/my_config.json")
    with open(config_file, encoding="utf-8") as f_in:
        config = json.load(f_in)

    logging.config.dictConfig(config)

    # Retrieve the 'queue_handler' from the configured root logger
    root_logger = logging.getLogger()  # Use root logger to check for handlers
    queue_handler = None
    for handler in root_logger.handlers:
        if isinstance(handler, QueueHandler):
            queue_handler = handler
            break

    # If a QueueHandler is found, set up a listener and start it
    if queue_handler is not None:
        log_queue: Queue = Queue()
        listener = QueueListener(log_queue, *root_logger.handlers)
        listener.start()
        atexit.register(listener.stop)


def main() -> None:
    """This is main module with testing what logging logs will be."""
    setup_logging()
    logging.basicConfig(level="INFO")
    logger.debug("debug message", extra={"x": "hello"})
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")
    try:
        1 / 0
    except ZeroDivisionError:
        logger.error("ZeroDivisionError: You cannot divide by zero.")


if __name__ == "__main__":
    main()
