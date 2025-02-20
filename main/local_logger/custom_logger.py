import os

from main.file_manager.manager_impl import ManagerImpl as Man

man = Man()


class CustomLogger:

    def files_properties(self, properties) -> bool:
        from main.local_logger.custom_exceptions.required_keys_exception import \
            RequiredKeysException

        """Stores file metadata into 'file_info.json'."""
        data_folder = r"data_storage"
        required_keys = {"file_path", "file_name", "file_size", "file_format"}
        if not required_keys.issubset(properties):
            try:
                raise RequiredKeysException(required_keys)
            except RequiredKeysException:
                return False

        data_path = os.path.join(data_folder, r"file_info.json")
        try:
            existing_data = Man.load_data_storage_file(man, data_path)
        except Exception as e:
            massage = {"massage": str(e)}
            self.error_handling(massage)
            return False

        file_path = properties.pop("file_path")

        if file_path in existing_data:
            existing_data[file_path].update(properties)
        else:
            existing_data[file_path] = properties

        Man.save_data_storage_file(man, data_path, existing_data)
        return True

    def search_results(self, processed_data: dict) -> dict:
        """Stores search results into 'processed_data.json'."""
        data_folder = r"data_storage"
        data_path = os.path.join(data_folder, "processed_data.json")
        existing_data = Man.load_data_storage_file(man, data_path)

        file_path = processed_data.pop("file_path")

        if file_path not in existing_data:
            existing_data[file_path] = {}

        if "search_request" in processed_data:
            search_key = processed_data["search_request"]
            if search_key not in existing_data[file_path]:
                existing_data[file_path][search_key] = []
            existing_data[file_path][search_key].extend(processed_data["search_result"])

        Man.save_data_storage_file(man, data_path, existing_data)
        return {"status": "success", "message": "Search results logged successfully"}

    def error_handling(self, message: dict) -> bool:
        """Logs errors into 'error_data.json'."""
        data_folder = r"data_storage"

        data_path = os.path.join(data_folder, "error_data.json")
        existing_data = Man.load_data_storage_file(man, data_path)

        if not isinstance(existing_data, dict):
            existing_data = {"errors": []}
        elif "errors" not in existing_data:
            existing_data["errors"] = []

        existing_data["errors"].append(message)

        Man.save_data_storage_file(man, data_path, existing_data)
        return True
