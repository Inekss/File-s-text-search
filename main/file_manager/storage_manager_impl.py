import json
import os

from main.file_manager.storage_manager import StorageFileManager


class StorageManagerImpl(StorageFileManager):
    def data_storage_exists(self) -> bool:
        """Ensure all necessary JSON files exist without recreating them unnecessarily."""
        data_folder = "data_storage"
        files = ["file_info.json", "processed_data.json", "error_data.json"]

        if not os.path.exists(data_folder):
            os.makedirs(data_folder)

        for file_name in files:
            file_path = os.path.join(data_folder, file_name)

            if not os.path.isfile(file_path):
                try:
                    with open(file_path, "w") as json_file:
                        json_file.write("{}")
                    raise Exception
                except Exception:
                    raise
        return True

    def load_data_storage_file(self, file_path: str) -> dict:
        """Load JSON data with error handling, ensuring storage is initialized first."""

        if self.data_storage_exists():
            try:
                with open(file_path, "r") as json_file:
                    content = json_file.read().strip()

                    if not content:
                        raise Exception

                    data = json.loads(content)
                    print(f"📂 Loaded data from {file_path}: {data}")
                    return data

            except Exception:
                print(f"⚠️ {file_path} contains invalid JSON. Resetting...")
                with open(file_path, "w") as json_file:
                    json.dump({}, json_file)
                raise
        return {}

    def save_data_storage_file(self, file_path, data) -> bool:
        """Save JSON data and force flush to disk."""
        try:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)
                json_file.flush()
                os.fsync(json_file.fileno())
            print(f"✅ Data FORCEFULLY written to {file_path}")
            return True
        except Exception as e:
            print(f"❌ Failed to write data to {file_path}: {e}")
            raise
