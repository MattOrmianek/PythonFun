""" This is learning new way of logging module """
import logging

logger = logging.getLogger("app")

def main() -> None:
    logging.basicConfig(level="DEBUG")
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")

    try:
        x = 1 / 0
    except ZeroDivisionError:
        logger.exception("This is an exception message")

if __name__ == "__main__":
    main()
