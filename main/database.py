import os
import json


def storing(request: str, data: object):
    error_report = [["error_status", False], ["error_type", ""], ["error_message", ""]]
    files = ["file_info.json", "processed_data.json", "error_data.json"]
    if request not in files:
        error_report = [
            ["error_status", True],
            ["error_type", "incorrect_parameter_value"],
            ["error_message", "Error: No such file in data storage"],
        ]
        return error_report

    # To create all data_storage file at once
    directory_path = r".\main\data_storage"
    create_new_file = {}
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
        error_report = [
            ["error_status", True],
            ["error_type", "corrupted_file"],
            ["error_message", "Error: corrupted json file, all data deleted"],
        ]

    try:
        existing_data.update(data)
    except Exception:
        error_report = [
            ["error_status", True],
            ["error_type", "incorrect_data_format"],
            ["error_message", f"Error: problems with data format"],
        ]
        return error_report

    with open(directory_path, "w") as json_file:
        json.dump(existing_data, json_file, indent=4)

    return error_report


if __name__ == "__main__":
    datalist = {"some data": 1, "some other data": 2}
    storing("processed_data.json", datalist)
