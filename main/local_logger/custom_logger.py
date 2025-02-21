import json
import os


class CustomLogger:
    def error_storage_exists(self) -> bool:
        """Ensure the JSON file exists without recreating it unnecessarily."""
        data_folder = r"data_storage"
        file_path = os.path.join(data_folder, r"error_data.json")

        if not os.path.isfile(file_path):
            try:
                with open(file_path, "w") as json_file:
                    json.dump({}, json_file)
                return False
            except Exception as e:
                return False

        return True

    def load_error_storage(self, file_path) -> dict:
        """Load JSON data without error handling, ensuring storage is initialized first."""

        if self.error_storage_exists():
            try:
                with open(file_path, "r") as json_file:
                    content = json_file.read().strip()

                    if not content:
                        raise Exception

                    data = json.loads(content)
                    return data

            except Exception:
                with open(file_path, "w") as json_file:
                    json.dump({}, json_file)
                # Have rights to be not caught
        return {}

    def save_error_storage(self, file_path, data) -> bool:
        """Save JSON data and force flush to disk."""
        if self.error_storage_exists():
            try:
                with open(file_path, "w") as json_file:
                    json.dump(data, json_file, indent=4)
                    json_file.flush()
                    os.fsync(json_file.fileno())
                return True
            except Exception:
                return False
                # Have rights to be not caught
        return False

    def error_handling(self, message: dict) -> bool:
        """Logs errors into 'error_data.json'."""
        data_folder = r"data_storage"

        data_path = os.path.join(data_folder, "error_data.json")
        try:
            existing_data = self.load_error_storage(data_path)
        except Exception:
            return False  # have rights to have no handling

        if not isinstance(existing_data, dict):
            existing_data = {"errors": []}
        elif "errors" not in existing_data:
            existing_data["errors"] = []

        existing_data["errors"].append(message)
        try:
            self.save_error_storage(data_path, existing_data)
        except Exception:
            return False  # have rights to have no handling
        return True
