import time

from main.local_logger.custom_logger import CustomLogger

logger = CustomLogger()


class SaveJsonException(Exception):
    """Custom exception for file properties validation errors."""

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
        dict_message = {
            "error": {
                "error_status": True,
                "error_type": "st_save_issue",
                "error_message": "can not save JSON",
                "error_description": message,
                "error_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            }
        }
        CustomLogger.error_handling(logger, dict_message)
