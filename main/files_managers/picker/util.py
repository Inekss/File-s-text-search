import os

from main.files_managers.storage_manager_impl import StorageManagerImpl as Man
from main.local_logger.custom_exceptions.required_keys_exception import (
    RequiredKeysException,
)

man = Man()


def construct_files_properties(properties: dict) -> bool:
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
        existing_data = Man.load_data_from_storage(man, data_path)
    except Exception:
        return False

    file_path = properties.pop("file_path")

    if file_path in existing_data:
        existing_data[file_path].update(properties)
    else:
        existing_data[file_path] = properties

    try:
        success = Man.save_data_to_storage(man, data_path, existing_data)
    except Exception:
        return False
    return success


def get_file_properties(file_path: str, file_info: dict) -> dict:
    """
    Extracts and returns file properties.
    :param file_path: Path of the file.
    :param file_info: Dictionary containing file details.
    :return: Dictionary with file properties.
    """
    return {
        "file_path": file_path,
        "file_name": file_info["file_name"],
        "file_size": file_info["file_size"],
        "file_format": file_info["file_format"],
    }


def analyze_folder_files(properties: dict) -> bool:
    """
    Analyzes folder files and returns structured data.
    :param properties: Dictionary containing folder properties.
    :return: Dictionary with analyzed folder data.
    """
    if not properties.get("selected_files"):
        try:
            raise RequiredKeysException("selected_files")
        except RequiredKeysException:
            return False

    selected_files = properties["selected_files"]
    for file_path, file_info in selected_files.items():
        data = get_file_properties(file_path, file_info)
        success = construct_files_properties(data)
        if not success:
            return False

    return True
