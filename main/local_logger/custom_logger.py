import time

import os
import json

from main.local_logger.custom_exceptions.required_keys_exception import (
    RequiredKeysException,
)


class CustomLogger:
    def ensure_data_storage(self) -> bool:
        """Ensure all necessary JSON files exist without recreating them unnecessarily."""
        data_folder = "main/data_storage"
        files = ["file_info.json", "processed_data.json", "error_data.json"]

        all_exist = True
        for file_name in files:
            file_path = os.path.join(data_folder, file_name)  # Correctly joins paths

            if not os.path.isfile(file_path):  # Check if file exists
                all_exist = False
                with open(file_path, "w") as json_file:
                    json.dump({}, json_file)  # Create missing file
                print(f"⚠️ Created missing file: {file_path}")
            else:
                print(f"📂 Found existing file: {file_path}")

        return all_exist  # Return True if all files exist, False if any were created

    def load_json(self, file_path) -> dict:
        """Load JSON data with error handling, ensuring storage is initialized first."""

        # Ensure storage is set up before attempting to load
        self.ensure_data_storage()

        try:
            with open(file_path, "r") as json_file:
                content = json_file.read().strip()  # Remove whitespace

                if not content:  # If file is empty, reset it
                    print(f"⚠️ {file_path} is empty. Resetting...")
                    with open(file_path, "w") as json_file:
                        json.dump({}, json_file)
                    return {}

                data = json.loads(content)  # Load JSON data
                print(f"📂 Loaded data from {file_path}: {data}")
                return data

        except json.JSONDecodeError:
            print(f"⚠️ {file_path} contains invalid JSON. Resetting...")
            with open(file_path, "w") as json_file:
                json.dump({}, json_file)
            return {}

    def save_json(self, file_path, data):
        """Save JSON data and force flush to disk."""
        try:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)
                json_file.flush()  # Ensures data is written to disk
                os.fsync(json_file.fileno())  # Forces the OS to write changes
            print(f"✅ Data FORCEFULLY written to {file_path}")
        except Exception as e:
            print(f"❌ Failed to write data to {file_path}: {e}")

    def files_properties(self, properties) -> bool:
        """Stores file metadata into 'file_info.json'."""
        data_folder = r"main\data_storage"
        required_keys = {"file_path", "file_name", "file_size", "file_format"}
        if not required_keys.issubset(properties):
            try:
                raise RequiredKeysException(required_keys)
            except RequiredKeysException as e:
                return False

        data_path = os.path.join(data_folder, r"file_info.json")
        existing_data = self.load_json(data_path)

        file_path = properties.pop("file_path")

        if file_path in existing_data:
            existing_data[file_path].update(properties)
        else:
            existing_data[file_path] = properties

        self.save_json(data_path, existing_data)
        return True

    def search_results(self, processed_data: dict) -> dict:
        """Stores search results into 'processed_data.json'."""
        data_folder = r"main\data_storage"
        data_path = os.path.join(data_folder, "processed_data.json")
        existing_data = self.load_json(data_path)

        file_path = processed_data.pop("file_path")

        # Merge new search data with existing data for the same file_path and search request
        if file_path not in existing_data:
            existing_data[file_path] = {}

        if "search_request" in processed_data:
            search_key = processed_data["search_request"]
            if search_key not in existing_data[file_path]:
                existing_data[file_path][search_key] = []
            existing_data[file_path][search_key].extend(processed_data["search_result"])

        self.save_json(data_path, existing_data)
        return {"status": "success", "message": "Search results logged successfully"}

    def error_handling(self, message: dict) -> bool:
        """Logs errors into 'error_data.json'."""
        data_folder = r"main\data_storage"

        data_path = os.path.join(data_folder, "error_data.json")
        existing_data = self.load_json(data_path)

        if not isinstance(existing_data, dict):
            existing_data = {"errors": []}
        elif "errors" not in existing_data:
            existing_data["errors"] = []

        existing_data["errors"].append(message)

        self.save_json(data_path, existing_data)
        return True
