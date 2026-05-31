import logging
import os

# Create logs directory
os.makedirs("logs", exist_ok=True)

# Create logger
logger = logging.getLogger("agent_logger")

logger.setLevel(logging.INFO)

# Prevent duplicate handlers
if not logger.handlers:

    file_handler = logging.FileHandler(
        "logs/agent.log",
        mode="a",
        encoding="utf-8"
    )

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)


def log_event(message):

    logger.info(message)

    for handler in logger.handlers:
        handler.flush()


def log_error(message):

    logger.error(message)

    for handler in logger.handlers:
        handler.flush()


# TEST EXECUTION
if __name__ == "__main__":

    print("LOGGER RUNNING")

    log_event("LOGGER TEST SUCCESS")

    print("LOG WRITTEN")