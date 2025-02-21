import atexit

import job
from files_managers.storage_manager_impl import StorageManagerImpl as stManager

from main.analyzer.util import save_simple_search_results
from main.cleaner import clean_cache
from main.files_managers.picker.picker import file_picker
from main.files_managers.picker.util import (
    construct_files_properties as files_properties,
)

man = stManager()

commands_list = [
    "help",
    "-h",
    "quit",
    "-q",
    "show-history",
    "-sh",
    "show-error-history",
    "-seh",
    "add-file",
    "-a -f",
    "add-folder",
    "-a -d",
    "add-file-path",
    "-a -f -p",
    "add-folder-path",
    "-a -d -p",
    "clear-database",
    "-rm -c",
    "remove-file",
    "-rm -f",
    "remove-folder",
    "-rm -d",
    "search-req-all",
    "-s -all",
    "search-req-file",
    "-s -f",
    "search-req-folder",
    "-s -d",
    "search-req-group",
    "-s -list",
    "search-req-multiple",
    "-s -multi",
    "show-files",
    "-t -f",
    "show-data",
    "-t -d",
    "show-errors",
    "-t -e",
    "show-all",
    "-t -all",
    "pycache-clean",
    "-clean",
]


def client():
    command_history = []
    while True:
        print()
        console_user_command = input("Enter a command: ")
        command_history.append(console_user_command)
        result = {}
        success = False
        match console_user_command:
            case "help" | "-h":
                for command in commands_list:
                    print(command)
                continue
            case "quit" | "-q":
                print("Terminating app...")
                break
            case "show-history" | "-sh":
                print("Showing command history...")
                for i in command_history:
                    print(i)
                continue
            case "show-error-history" | "-seh":
                success = False
            case "add-file" | "-a -f":
                print("Adding file manually...")
                result = file_picker()
                success = files_properties(result)
            case "add-folder" | "-a -d":
                print("Adding folder manually...")
            case "add-file-path" | "-a -f -p":
                print("Adding file using its system path...")
            case "add-folder-path" | "-a -d -p":
                print("Adding folder using its system path...")
            case "clear-database" | "-rm -c":
                print("Clearing all databases...")
            case "remove-file" | "-rm -f":
                print("Removing file from database...")
            case "remove-folder" | "-rm -d":
                print("Removing folder from database...")
            case "search-req-all" | "-s -all":
                print("Making search request through all database...")
            case "search-req-file" | "-s -f":
                print("Searching in one chosen file...")
                path = input("Enter a path of file: ")
                request = input("Enter a search request: ")
                result = job.simple_search_client(request, path)
                success = save_simple_search_results(result)
            case "search-req-folder" | "-s -d":
                print("Making search request in one chosen folder...")
            case "search-req-group" | "-s -list":
                print("Setting search group...")
            case "search-req-multiple" | "-s -multi":
                print("Making multiple search requests...")
            case "show-files" | "-t -f":
                print("Reviewing file storage...")
                success = stManager.show_file_info_data_storage(man)
                result = {"success": success}
            case "show-data" | "-t -d":
                print("Reviewing processed data storage...")
                success = stManager.show_processed_data_storage(man)
                result = {"success": success}
            case "show-errors" | "-t -e":
                print("Reviewing error storage...")
                success = stManager.show_error_storage(man)
                result = {"success": success}
            case "show-all" | "-t -all":
                print("Reviewing all storages...")
                success = stManager.show_all_data_storage(man)
                result = {"success": success}
            case "pycache-clean" | "-clean":
                print("Cleaning cache...")
                atexit.register(clean_cache)
                continue
            case _:
                print("Unknown command. Type 'help' or '-h' for a list of commands.")
                continue

        if not result or not success:
            stManager.show_error_storage(man)
            continue

        print(result)


if __name__ == "__main__":
    print("To see all commands, type 'help'.")
    client()
