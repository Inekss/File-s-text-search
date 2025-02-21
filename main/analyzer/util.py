import os

from main.files_managers.storage_manager_impl import StorageManagerImpl as Man
from main.local_logger.custom_exceptions.invalid_input_exception import (
    InvalidInputException,
)

man = Man()


def save_simple_search_results(processed_data: dict) -> bool:
    """Stores search results into 'processed_data.json'."""
    if processed_data == {}:
        try:
            raise InvalidInputException(
                "simple_search_client return False while input validation"
            )
        except InvalidInputException:
            return False

    data_folder = r"data_storage"
    data_path = os.path.join(data_folder, "processed_data.json")
    try:
        existing_data = Man.load_data_from_storage_file(man, data_path)
    except Exception:
        return False

    file_path = processed_data.pop("file_path")

    if file_path not in existing_data:
        existing_data[file_path] = {}

    if "search_request" in processed_data:
        search_key = processed_data["search_request"]
        if search_key not in existing_data[file_path]:
            existing_data[file_path][search_key] = []
        existing_data[file_path][search_key].extend(processed_data["search_result"])

    try:
        Man.save_data_to_storage_file(man, data_path, existing_data)
    except Exception:
        return False
    return True
