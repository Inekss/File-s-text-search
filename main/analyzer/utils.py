import os

from main.file_manager.storage_manager_impl import StorageManagerImpl as Man
from main.local_logger.custom_exceptions.required_keys_exception import (
    RequiredKeysException,
)

man = Man()


def files_properties(properties) -> bool:
    """Stores file metadata into 'file_info.json'."""
    data_folder = r"main/data_storage"
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
        return False

    file_path = properties.pop("file_path")

    if file_path in existing_data:
        existing_data[file_path].update(properties)
    else:
        existing_data[file_path] = properties

    try:
        success = Man.save_data_storage_file(man, data_path, existing_data)
    except Exception:
        return False
    return success


def search_results(processed_data: dict) -> dict:
    """Stores search results into 'processed_data.json'."""
    data_folder = r"data_storage"
    data_path = os.path.join(data_folder, "processed_data.json")
    try:
        existing_data = Man.load_data_storage_file(man, data_path)
    except Exception:
        return {}

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
        return {}
    return {"status": "success", "message": "Search results logged successfully"}
