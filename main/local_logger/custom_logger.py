import os

from main.local_logger.custom_exceptions.invalid_json_exception import InvalidJsonException
from main.local_logger.custom_exceptions.save_json_exception import SaveJsonException

from main.file_manager.storage_manager_impl import StorageManagerImpl as Man

man = Man()

class CustomLogger:

    def files_properties(self, properties) -> bool:
        from main.local_logger.custom_exceptions.required_keys_exception import RequiredKeysException
        """Stores file metadata into 'file_info.json'."""
        data_folder = r"data_storage"
        required_keys = {"file_path", "file_name", "file_size", "file_format"}
        if not required_keys.issubset(properties):
            try:
                raise RequiredKeysException("file_path, file_name, file_size, file_format")
            except RequiredKeysException:
                return False

        data_path = os.path.join(data_folder, r"file_info.json")

        try:
            existing_data = Man.load_data_storage_file(man, data_path)
        except Exception:
            raise InvalidJsonException(f" {data_path} contains invalid JSON. Resetting...")

        file_path = properties.pop("file_path")

        if file_path in existing_data:
            existing_data[file_path].update(properties)
        else:
            existing_data[file_path] = properties

        try:
            Man.save_data_storage_file(man, data_path, existing_data)
        except Exception:
            raise SaveJsonException(f"❌ Failed to write data to {file_path}: {e}")
        return True

    def search_results(self, processed_data: dict) -> dict:
        """Stores search results into 'processed_data.json'."""
        data_folder = r"data_storage"
        data_path = os.path.join(data_folder, "processed_data.json")
        try:
            existing_data = Man.load_data_storage_file(man, data_path)
        except Exception:
            raise InvalidJsonException(f" {data_path} contains invalid JSON. Resetting...")

        file_path = processed_data.pop("file_path")

        if file_path not in existing_data:
            existing_data[file_path] = {}

        if "search_request" in processed_data:
            search_key = processed_data["search_request"]
            if search_key not in existing_data[file_path]:
                existing_data[file_path][search_key] = []
            existing_data[file_path][search_key].extend(processed_data["search_result"])

        try:
            Man.save_data_storage_file(man, data_path, existing_data)
        except Exception:
            raise SaveJsonException(f"❌ Failed to write data to {file_path}: {e}")
        return {"status": "success", "message": "Search results logged successfully"}
