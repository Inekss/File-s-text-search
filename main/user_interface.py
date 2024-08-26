from communication import file_picker


def user_interface():
    commands_list = [
        "help",
        "-h",
        "quit",
        "-q",
        "show-history",
        "-ch",
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
        "-t -i",
        "show-errors",
        "-t -e",
        "show-all",
        "-t -all",
    ]
    while True:
        console_user_command = input("Enter a command: ")
        match console_user_command:
            case "help" | "-h":
                for command in commands_list:
                    print(command)
            case "quit" | "-q":
                print("Terminating app...")
                break
            case "show-history" | "-ch":
                print("Showing command history...")
            case "add-file" | "-a -f":
                print("Adding file manually...")
                file_picker()
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
            case "search-req-folder" | "-s -d":
                print("Making search request in one chosen folder...")
            case "search-req-group" | "-s -list":
                print("Setting search group...")
            case "search-req-multiple" | "-s -multi":
                print("Making multiple search requests...")
            case "show-files" | "-t -f":
                print("Reviewing file database...")
            case "show-data" | "-t -i":
                print("Reviewing data database...")
            case "show-errors" | "-t -e":
                print("Reviewing error database...")
            case "show-all" | "-t -all":
                print("Reviewing all databases...")
            case _:
                print("Unknown command. Type 'help' or '-h' for a list of commands.")


if __name__ == "__main__":
    user_interface()
