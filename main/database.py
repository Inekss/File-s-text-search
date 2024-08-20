import os
import json


def storing(request: str, data: object):
    error = [["error_message", ""], ["error_status", False]]
    directory_path = r".\main\data_storage"
    files = ["file_info.json", "processed_data.json", "error_data.json"]
    create_new_file = {}
    if request not in files:
        error = [
            ["error_message", "Error: No such file in data storage"],
            ["error_status", True],
        ]
        return error

    # To create all data_storage file at once
    for file_name in files:
        if file_name not in os.listdir(directory_path):
            file_name = os.path.join(directory_path, file_name)
            with open(file_name, "w") as json_file:
                json.dump(create_new_file, json_file)

    directory_path = os.path.join(directory_path, request)
    try:
        with open(directory_path, "r") as json_file:
            existing_data = json.load(json_file)
    except json.JSONDecodeError:
        existing_data = {}
        error = [
            [
                "error_message",
                f"Error: corrupted json file, all data deleted from {directory_path}",
            ],
            ["error_status", True],
        ]
        return error

    try:
        existing_data.update(data)
    except Exception:
        error = [
            ["error_message", f"Error: problems with dara format"],
            ["error_status", True],
        ]
        return error

    with open(directory_path, "w") as json_file:
        json.dump(existing_data, json_file, indent=4)

    return error
    # if error_status is false there is no error
    # Here a need to think about error object name


if __name__ == "__main__":
    datalist = {"some data": 1, "some other data": 2}
    storing("processed_data.json", datalist)
