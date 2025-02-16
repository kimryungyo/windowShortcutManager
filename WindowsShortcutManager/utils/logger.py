from .singleton import singleton
import logging
import sys

DEFAULT_LOG_FORMAT = "[%(asctime)s] %(levelname)s: %(message)s"
DEFAULT_LOG_LEVEL = logging.DEBUG
DEFAULT_CONSOLE_LOG_LEVEL = logging.INFO
DEFAULT_FILE_LOG_LEVEL = logging.DEBUG

class Logger(logging.Logger):
    def __init__(
        self, name: str,
        log_file_path,
        log_format: str = DEFAULT_LOG_FORMAT,
        log_level: int = DEFAULT_LOG_LEVEL,
        console_log_level: int = DEFAULT_CONSOLE_LOG_LEVEL,
        file_log_level: int = DEFAULT_FILE_LOG_LEVEL,
    ):
        super().__init__(name, log_level)
        
        # 핸들러가 없는 경우에만 추가
        if not self.handlers:
            formatter = logging.Formatter(log_format)
            
            # 콘솔 핸들러 설정
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setLevel(console_log_level)
            console_handler.setFormatter(formatter)
            self.addHandler(console_handler)
            
            # 파일 핸들러 설정
            file_handler = logging.FileHandler(log_file_path)
            file_handler.setLevel(file_log_level)
            file_handler.setFormatter(formatter)
            self.addHandler(file_handler)

@singleton
class SingletonLogger(Logger):
    def __init__(
        self,
        log_file_path,
        log_format: str = DEFAULT_LOG_FORMAT,
        log_level: int = DEFAULT_LOG_LEVEL,
        console_log_level: int = DEFAULT_CONSOLE_LOG_LEVEL,
        file_log_level: int = DEFAULT_FILE_LOG_LEVEL,
    ):
        name = "SingletonLogger"
        super().__init__(name, log_file_path, log_format, log_level, console_log_level, file_log_level)