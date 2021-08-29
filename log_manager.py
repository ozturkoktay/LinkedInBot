import logging
from configuration import LOG_FORMAT
from logging.handlers import RotatingFileHandler
import uuid


class LogManager:

    def __init__(self, name: str, filename: str):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        fh = RotatingFileHandler(filename, maxBytes=5242880, backupCount=5000)
        fh.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)
        formatter = logging.Formatter(LOG_FORMAT,
                                      datefmt="%d/%m/%Y %I:%M:%S %p")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
        self.instance_id = str(uuid.uuid4())
        self.session_id = None

    def trace(self, message: str):
        if self.session_id is None:
            self.logger.debug(self.instance_id + "\t" + message)
        else:
            self.logger.debug(self.instance_id + "\t" + self.session_id +
                              "\t" + message)

    def info(self, message: str, display: bool = False):
        if self.session_id is None:
            self.logger.info(self.instance_id + "\t" + message)
        else:
            self.logger.info(self.instance_id + "\t" + self.session_id + "\t" +
                             message)

    def warn(self, message: str, display: bool = False):
        if self.session_id is None:
            self.logger.warning(self.instance_id + "\t" + message)
        else:
            self.logger.warning(self.instance_id + "\t" + self.session_id +
                                "\t" + message)

    def error(self, message: str, display: bool = True):
        if self.session_id is None:
            self.logger.error(self.instance_id + "\t" + message)
        else:
            self.logger.error(self.instance_id + "\t" + self.session_id +
                              "\t" + message)

    def exception(self, message: str, display: bool = True):
        if self.session_id is None:
            self.logger.exception(self.instance_id + "\t" + message)
        else:
            self.logger.exception(self.instance_id + "\t" + self.session_id +
                                  "\t" + message)
