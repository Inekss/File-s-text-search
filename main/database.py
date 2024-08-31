import os
import json
import time


def data_storage_constructor():
    files = ["file_info.json", "processed_data.json", "error_data.json"]

    for file_name in files:
        data_path = rf".\main\data_storage\{file_name}.json"
        if not os.path.isfile(data_path):
            with open(data_path, "w") as json_file:
                json.dump({}, json_file)


def files_properties(properties: dict):
    if (
        properties.get("file_path")
        and properties.get("file_name")
        and properties.get("file_size")
        and properties.get("file_format")
    ):

        data_path = r".\main\data_storage\file_info.json"
        if not os.path.isfile(data_path):
            with open(data_path, "w") as json_file:
                json.dump({}, json_file)

        try:
            with open(data_path, "r") as json_file:
                existing_data = json.load(json_file)
        except json.JSONDecodeError:
            with open(data_path, "w") as json_file:
                json.dump({}, json_file)
            errors_report = {
                "error_status": True,
                "error_type": "corrupted_file",
                "error_message": data_path,
                "error_description": "Error: corrupted json file, all data deleted",
                "error_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            }
            return errors_report

        properties_path = properties.pop("file_path")

        if properties_path in existing_data:
            existing_data[properties_path].update(properties)
        else:
            existing_data[properties_path] = properties

        with open(data_path, "w") as json_file:
            json.dump(existing_data, json_file, indent=4)

    else:
        errors_report = {
            "error_status": True,
            "error_type": "incorrect_parameters",
            "error_message": "parameters",
            "error_description": "Error: files_properties requires 4 parameters, each has its own location",
            "error_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        }
        error_handling(errors_report)


def search_results(processed_data: dict):
    if processed_data.get("file_path") and (
        (
            processed_data.get("search_request")
            and processed_data.get("search_result")
            and processed_data.get("search_status")
        )
        or processed_data.get("global_result")
    ):
        data_path = r".\main\data_storage\processed_data.json"
        if not os.path.isfile(data_path):
            with open(data_path, "w") as json_file:
                json.dump({}, json_file)

        try:
            with open(data_path, "r") as json_file:
                existing_data = json.load(json_file)
        except json.JSONDecodeError:
            with open(data_path, "w") as json_file:
                json.dump({}, json_file)
            errors_report = {
                "error_status": True,
                "error_type": "corrupted_file",
                "error_message": data_path,
                "error_description": "Error: corrupted json file, all data deleted",
                "error_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            }
            return errors_report

        file_path = processed_data.pop("file_path")

        if "search_request" in processed_data:
            search_request_key = processed_data["search_request"]

            if file_path not in existing_data:
                existing_data[file_path] = {}

            if search_request_key in existing_data[file_path]:
                existing_data[file_path][search_request_key].update(processed_data)
            else:
                existing_data[file_path][search_request_key] = processed_data

        elif "global_result" in processed_data:
            if file_path not in existing_data:
                existing_data[file_path] = {}

            existing_data[file_path]["global_result"] = processed_data["global_result"]

        with open(data_path, "w") as json_file:
            json.dump(existing_data, json_file, indent=4)

    else:
        errors_report = {
            "error_status": True,
            "error_type": "incorrect_parameters",
            "error_message": "parameters",
            "error_description": "Error: search_results requires 3 or 2 parameters, each has its own location",
            "error_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        }
        error_handling(errors_report)


def error_handling(report: dict):
    if (
        report.get("error_status")
        and report.get("error_type")
        and report.get("error_message")
        and report.get("error_description")
        and report.get("error_time")
    ):
        data_path = r".\main\data_storage\error_data.json"
        if not os.path.isfile(data_path):
            with open(data_path, "w") as json_file:
                json.dump({}, json_file)

        try:
            with open(data_path, "r") as json_file:
                existing_data = json.load(json_file)
        except json.JSONDecodeError:
            with open(data_path, "w") as json_file:
                json.dump({}, json_file)
            errors_report = {
                "error_status": True,
                "error_type": "corrupted_file",
                "error_message": data_path,
                "error_description": "Error: corrupted json file, all data deleted",
                "error_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            }
            return errors_report

        error_type = report.pop("error_type")
        error_time = report.get("error_time")

        if error_type not in existing_data:
            existing_data[error_type] = {}

        if error_time in existing_data[error_type]:
            existing_data[error_type][error_time].update(report)
        else:
            existing_data[error_type][error_time] = report

        with open(data_path, "w") as json_file:
            json.dump(existing_data, json_file, indent=4)

    else:
        errors_report = {
            "error_status": True,
            "error_type": "incorrect_parameters",
            "error_message": "parameters",
            "error_description": "Error: error_handling requires 5 parameters, each has its own location",
            "error_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        }
        error_handling(errors_report)


# if __name__ == "__main__":
# print()
# processed_data = {
#     "file_path": "my",
#     "search_request": "ddd",
#     "search_result": "hh",
#     "search_status": "hh",
# }

# or

# processed_data = {
#     "file_path": "home",
#     "global_result": "hh",
# }
# search_results(processed_data)

# path = r".\main\data_storage\processed_data.json"
# properties = {
#     "file_path": path,
#     "file_name": "name",
#     "file_size": "size",
#     "file_format": "format",
# }
# files_properties(properties)

# datalist = {"some data": 1, "some other data": 2}

# testing error_handling function

# error_report = {
#    "error_status": True,
#    "error_type": "corrupted_file",
#    "error_message": datalist,
#    "error_description": "Error: corrupted json file, all data deleted",
#    "error_time": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
# }
# error_handling(error_report)
