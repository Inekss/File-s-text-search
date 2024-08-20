import os
import json
import time


def storing(request: str, data: list):
    files = ["file_info.json", "processed_data.json", "error_data.json"]
    if request not in files:
        errors_report = [
            ["error_status", True],
            ["error_type", "incorrect_parameter_value"],
            ["error_message", request],
            ["error_description", "Error: No such file in data storage"],
            ["error_time", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())],
        ]
        error_handling(errors_report)
        return

    # To create all data_storage file at once
    directory_path = r".\main\data_storage"
    for file_name in files:
        file_path = rf".\main\data_storage\{file_name}.json"
        if not os.path.isfile(file_path):
            with open(file_path, "w") as json_file:
                json.dump({}, json_file)

    file_path = os.path.join(directory_path, request)
    try:
        with open(file_path, "r") as json_file:
            existing_data = json.load(json_file)
    except json.JSONDecodeError:
        existing_data = {}
        errors_report = [
            ["error_status", True],
            ["error_type", "corrupted_file"],
            ["error_message", file_path],
            ["error_description", "Error: corrupted json file, all data deleted"],
            ["error_time", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())],
        ]
        error_handling(errors_report)

    try:
        existing_data.update(data)
    except Exception:
        errors_report = [
            ["error_status", True],
            ["error_type", "incorrect_data_format"],
            ["error_message", "format"],
            [
                "error_description",
                f"Error: problems with data format - it is not a list",
            ],
            ["error_time", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())],
        ]
        error_handling(errors_report)
        return

    with open(file_path, "w") as json_file:
        json.dump(existing_data, json_file, indent=4)


def error_handling(report: list):
    if report[0][1]:
        file_path = r".\main\data_storage\error_data.json"
        if not os.path.isfile(file_path):
            with open(file_path, "w") as json_file:
                json.dump({}, json_file)

        with open(file_path, "r") as json_file:
            existing_data = json.load(json_file)

        report_dict = dict(report)
        error_type = report_dict.pop("error_type")
        error_time = report_dict.get("error_time")

        if error_type in existing_data:
            if error_time in [
                entry.get("error_time") for entry in existing_data[error_type]
            ]:
                for entry in existing_data[error_type]:
                    if entry.get("error_time") == error_time:
                        entry.update(report_dict)
                        break
                pass
            else:
                # Append the new report under the existing error type
                existing_data[error_type].append(report_dict)
        else:
            # Create a new list for this error type and add the report
            existing_data[error_type] = [report_dict]

        with open(file_path, "w") as json_file:
            json.dump(existing_data, json_file, indent=4)


if __name__ == "__main__":
    datalist = {"some data": 1, "some other data": 2}
    storing("processed_data.json", datalist)
    # testing error_handling function
    # error_report = [
    #    ["error_status", True],
    #    ["error_type", "corrupted_file"],
    #    ["error_message", datalist],
    #    ["error_description", "Error: corrupted json file, all data deleted"],
    #    ["error_time", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())],
    #    ["hello", "world"]
    # ]
    # error_handling(error_report)
