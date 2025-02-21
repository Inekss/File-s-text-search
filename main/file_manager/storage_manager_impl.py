import json
import os

from main.file_manager.storage_manager import StorageFileManager
from main.local_logger.custom_exceptions.file_not_exist_exception import (
    FileNotExistException,
)
from main.local_logger.custom_exceptions.invalid_json_exception import (
    InvalidJsonException,
)
from main.local_logger.custom_exceptions.save_json_exception import SaveJsonException


class StorageManagerImpl(StorageFileManager):
    def data_storage_exists(self, file_path: str) -> bool:
        """Check if both the directory and file exist without creating them."""

        dir_path = os.path.dirname(file_path)
        try:
            if not os.path.exists(dir_path):
                raise FileNotExistException("File does not exist")

            if not os.path.isfile(file_path):
                raise FileNotExistException("File does not exist")
        except FileNotExistException:
            return False

        return True

    def load_data_storage_file(self, file_path: str) -> dict:
        """Load JSON data with error handling, ensuring storage is initialized first."""

        if self.data_storage_exists(file_path):
            try:
                with open(file_path, "r") as json_file:
                    content = json_file.read().strip()

                    if not content:
                        raise Exception

                    data = json.loads(content)
                    return data

            except Exception:
                print(f"⚠️ {file_path} contains invalid JSON. Resetting...")
                with open(file_path, "w") as json_file:
                    json.dump({}, json_file)
                raise InvalidJsonException(
                    f" {file_path} contains invalid JSON. Resetting..."
                )
        return {}

    def save_data_storage_file(self, file_path, data) -> bool:
        """Save JSON data and force flush to disk."""
        if self.data_storage_exists(file_path):
            try:
                with open(file_path, "w") as json_file:
                    json.dump(data, json_file, indent=4)
                    json_file.flush()
                    os.fsync(json_file.fileno())
                print(f"✅ Data written to {file_path}")
                return True
            except Exception as e:
                print(f"❌ Failed to write data to {file_path}: {e}")
                raise SaveJsonException(f"❌ Failed to write data to {file_path}: {e}")
        return False
