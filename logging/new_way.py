""" This is learning new way of logging module """
import atexit
import json
import logging.config
import logging.handlers
import pathlib

logger = logging.getLogger("my_app")


def setup_logging():
    # stderr-file.json
    # filtered-stdout-stderr.json
    # queued-json-stderr.json
    # queued-stderr-json-file.json
    # stderr-json-file.json
    # my_config.json

    config_file = pathlib.Path("logging_configs/my_config.json")
    with open(config_file, encoding="utf-8") as f_in:
        config = json.load(f_in)

    logging.config.dictConfig(config)
    queue_handler = logging.getHandlerByName("queue_handler")
    if queue_handler is not None:
        queue_handler.listener.start()
        atexit.register(queue_handler.listener.stop)


def main():
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
        logger.exception("exception message")


if __name__ == "__main__":
    main()