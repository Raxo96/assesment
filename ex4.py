# 4. Design Pattern
#
# Apply Singleton design pattern to CustomLogger class.

import logging
import sys


class CustomLogger:
    def __init__(
            self,
            logger_name: str,
            log_level: int = logging.INFO,
            log_file: str = None
    ):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(log_level)
        self.logger.propagate = False

        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        if self.logger.hasHandlers():
            self.logger.handlers.clear()

        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)

        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def get_logger(self):
        return self.logger


if __name__ == "__main__":
    logger1 = CustomLogger("LoggerOne", logging.INFO)
    logger2 = CustomLogger("LoggerTwo", logging.DEBUG)

    assert id(logger1) == id(logger2), (
        "Logger instances should have the same IDs"
    )
