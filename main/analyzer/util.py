import os

from main.files_managers.storage_manager_impl import StorageManagerImpl as Man

man = Man()


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
