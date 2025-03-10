import json

from json_log_formatter import JSONFormatter


class StructuredLogger:
    def __init__(self, logger) -> None:
        self.logger = logger
        self.binds = {}

    def bind(self, **kwargs):
        for key, value in kwargs.items():
            self.binds[key] = value

    def debug(self, message: str) -> None:
        self.logger.debug(message, extra=self.binds)

    def info(self, message: str) -> None:
        self.logger.info(message, extra=self.binds)

    def warn(self, message: str) -> None:
        self.logger.warn(message, extra=self.binds)

    def warning(self, message: str) -> None:
        self.logger.warning(message, extra=self.binds)

    def error(self, message: str) -> None:
        self.logger.error(message, extra=self.binds)


class CustomFormatter(JSONFormatter):
    def __init__(self, pretty_format_json: bool = False):
        super().__init__()
        self.pretty_format_json = pretty_format_json

    def json_record(self, message, extra, record):
        extra["message"] = message
        extra["level"] = record.levelname
        extra["timestamp"] = self.formatTime(record)
        return extra

    def format(self, record):
        if self.pretty_format_json:
            log_object = self.json_record(record.getMessage(), record.__dict__, record)
            return json.dumps(log_object, indent=4)
        return super().format(record)
