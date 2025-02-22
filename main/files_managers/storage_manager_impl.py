import json
import os

from main.files_managers.storage_manager import StorageFileManager
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

    def load_data_from_storage(self, file_path: str) -> dict:
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

    def save_data_to_storage(self, file_path: str, data: dict) -> bool:
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

    def remove_file_info(self, data: str) -> bool:
        data_folder = r"data_storage"
        data_path = os.path.join(data_folder, "file_info.json")

        file_data = self.load_data_from_storage(data_path)

        if data in file_data:
            del file_data[data]
            with open(data_path, "w") as json_file:
                json.dump(file_data, json_file, indent=4)

            return True
        else:
            print(f"⚠ File path {data} not found in file_info.json.")
        return False

    def clear_st(self) -> bool:
        data_folder = r"data_storage"
        data_path = os.path.join(data_folder, "error_data.json")
        if not self.data_storage_exists(data_path):
            return False
        with open(data_path, "w") as json_file:
            json.dump({}, json_file)

        data_path = os.path.join(data_folder, "file_info.json")
        if not self.data_storage_exists(data_path):
            return False
        with open(data_path, "w") as json_file:
            json.dump({}, json_file)

        data_folder = r"data_storage"
        data_path = os.path.join(data_folder, "processed_data.json")
        if not self.data_storage_exists(data_path):
            return False
        with open(data_path, "w") as json_file:
            json.dump({}, json_file)

        return True

    def show_error_storage(self) -> bool:
        data_folder = "data_storage"
        data_path = os.path.join(data_folder, r"error_data.json")
        if not self.data_storage_exists(data_path):
            return False

        issues = self.load_data_from_storage(data_path)

        print("\033[94mErrors:\033[0m")  # Blue color for header
        for issue in issues.get("errors", []):
            error_details = issue.get("error", {})
            print(f"\033[91m{error_details}\033[0m")  # Red color for error
        return True

    def show_processed_data_storage(self) -> bool:
        data_folder = "data_storage"
        data_path = os.path.join(data_folder, r"processed_data.json")
        if not self.data_storage_exists(data_path):
            return False

        processed_data = self.load_data_from_storage(data_path)

        print("\033[94mProcessed Data:\033[0m")  # Blue header
        for file_path, matches in processed_data.items():
            print(f"\033[92mFile:\033[0m {file_path}")  # Green for file path
            for (
                search_term,
                occurrences,
            ) in matches.items():  # Iterate dynamically over search terms
                print(
                    f"  \033[93mSearch Term:\033[0m {search_term}"
                )  # Yellow for dynamic term
                for match in occurrences:
                    print(
                        f"    \033[96mMatch:\033[0m {match}"
                    )  # Cyan for match details
        return True

    def show_file_info_data_storage(self) -> bool:
        data_folder = "data_storage"
        data_path = os.path.join(data_folder, r"file_info.json")
        if not self.data_storage_exists(data_path):
            return False

        files = self.load_data_from_storage(data_path)

        print("\033[94mFile Structure:\033[0m")  # Blue color for header
        for file_path, file_details in files.items():
            print(f"\033[92mFile Path:\033[0m {file_path}")  # Green for path
            for key, value in file_details.items():
                print(f"  \033[96m{key}:\033[0m {value}")  # Cyan for key-value pairs
        return True

    def show_all_data_storage(self) -> bool:
        print()
        if not self.show_file_info_data_storage():
            return False
        print()
        if not self.show_processed_data_storage():
            return False
        print()
        if not self.show_error_storage():
            return False
        print()
        return True
