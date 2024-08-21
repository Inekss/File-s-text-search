import os
import json
import time


def data_storage_constructor():
    files = ["file_info.json", "processed_data.json", "error_data.json"]

    # To create all data_storage file at once
    directory_path = r".\main\data_storage"
    for file_name in files:
        data_path = rf".\main\data_storage\{file_name}.json"
        if not os.path.isfile(data_path):
            with open(data_path, "w") as json_file:
                json.dump({}, json_file)


def files_properties(properties: list):
    if (
        properties[0][0] == "file_path"
        and properties[1][0] == "file_name"
        and properties[2][0] == "file_size"
        and properties[3][0] == "file_format"
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
            errors_report = [
                ["error_status", True],
                ["error_type", "corrupted_file"],
                ["error_message", data_path],
                ["error_description", "Error: corrupted json file, all data deleted"],
                ["error_time", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())],
            ]
            error_handling(errors_report)
            return

        properties_dict = dict(properties)
        properties_path = properties_dict.pop("file_path")
        if properties_path in existing_data:
            existing_data[properties_path].append(properties_dict)
        else:
            existing_data[properties_path] = [properties_dict]

        with open(data_path, "w") as json_file:
            json.dump(existing_data, json_file, indent=4)

    else:
        errors_report = [
            ["error_status", True],
            ["error_type", "incorrect_parameters"],
            ["error_message", "parameters"],
            [
                "error_description",
                "Error: files_properties has 4 parameters, each has own location",
            ],
            ["error_time", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())],
        ]
        error_handling(errors_report)


def search_results(processed_data: list):
    if processed_data[0][0] == "file_path" and (
        (
            processed_data[1][0] == "search_request"
            and processed_data[2][0] == "search_result"
            and processed_data[3][0] == "search_status"
        )
        or processed_data[1][0] == "global_result"
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
            errors_report = [
                ["error_status", True],
                ["error_type", "corrupted_file"],
                ["error_message", data_path],
                ["error_description", "Error: corrupted json file, all data deleted"],
                ["error_time", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())],
            ]
            error_handling(errors_report)
            return

        processed_data_dict = dict(processed_data)

        # Extract the file path and remove it from processed_data_dict
        file_path = processed_data_dict.pop("file_path")

        if processed_data[1][0] == "search_request":

            # Create the search request dictionary
            search_request_dict = {"request": processed_data_dict}

            # Check if the file_path already exists in existing_data
            if file_path in existing_data:
                existing_entry = existing_data[file_path]

                # If the existing entry is a single request, wrap it in a list
                if "reauest" in existing_entry:
                    if isinstance(existing_entry, dict):
                        existing_entry = [existing_entry]

                    # Check if the new search request matches any existing request
                    matching_request = next(
                        (
                            req
                            for req in existing_entry
                            if req["request"]["search_request"]
                            == search_request_dict["request"]["search_request"]
                        ),
                        None,
                    )

                    if matching_request:
                        # Update the matching request
                        matching_request["request"].update(
                            search_request_dict["request"]
                        )
                    else:
                        # Append the new search request to the list
                        existing_entry.append(search_request_dict)

                    # Update the entry in existing_data
                    existing_data[file_path] = existing_entry
                else:
                    # Initialize a new entry with the search request
                    existing_data[file_path].append(processed_data_dict)
            else:
                # Initialize a new entry with the search request
                existing_data[file_path].append(processed_data_dict)

        elif processed_data[1][0] == "global_result":

            if file_path in existing_data:

                global_result_updated = False

                # Iterate through the list to find and update the existing global_result

                for entry in existing_data[file_path]:

                    if "global_result" in entry:
                        # Update the global_result value with the new one

                        entry["global_result"] = processed_data_dict["global_result"]

                        global_result_updated = True

                        break

                if not global_result_updated:
                    # If no matching global_result was found, append the new one

                    existing_data[file_path].append(processed_data_dict)

            else:

                # Initialize a new entry with processed_data_dict if file_path does not exist

                existing_data[file_path] = [processed_data_dict]

        with open(data_path, "w") as json_file:
            json.dump(existing_data, json_file, indent=4)

    else:
        errors_report = [
            ["error_status", True],
            ["error_type", "incorrect_parameters"],
            ["error_message", "parameters"],
            [
                "error_description",
                "Error: search_results has 3 or 2 parameters, each has own location",
            ],
            ["error_time", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())],
        ]
        error_handling(errors_report)


def error_handling(report: list):
    if (
        report[0][1]
        and report[1][0] == "error_type"
        and report[2][0] == "error_message"
        and report[3][0] == "error_description"
        and report[4][0] == "error_time"
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
            errors_report = [
                ["error_status", True],
                ["error_type", "corrupted_file"],
                ["error_message", data_path],
                ["error_description", "Error: corrupted json file, all data deleted"],
                ["error_time", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())],
            ]
            error_handling(errors_report)
            return

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
                existing_data[error_type].append(report_dict)
        else:
            existing_data[error_type] = [report_dict]

        with open(data_path, "w") as json_file:
            json.dump(existing_data, json_file, indent=4)
    else:
        errors_report = [
            ["error_status", True],
            ["error_type", "incorrect_parameters"],
            ["error_message", "parameters"],
            [
                "error_description",
                "Error: error_handling has 5 parameters, each has own location",
            ],
            ["error_time", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())],
        ]
        error_handling(errors_report)


if __name__ == "__main__":
    print()
    # processed_data = [
    #     ["file_path", "home"],
    #     ["search_request", "hh"],
    #     ["search_result", "hh"],
    #     ["search_status", "hh"],
    # ]

    # or

    # processed_data = [
    #     ["file_path", "home"],
    #     ["global_result", "hh"],
    # ]
    # search_results(processed_data)

    # path = r".\main\data_storage\processed_data.json"
    # properties = [
    #     ["file_path", path],
    #     ["file_name", "name"],
    #     ["file_size", "size"],
    #     ["file_format", "format"],
    # ]
    # files_properties(properties)

    # datalist = {"some data": 1, "some other data": 2}
    # storing("processed_data.json", datalist)

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
