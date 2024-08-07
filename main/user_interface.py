from typing import List

def user_interface():
    console_user_command: str = None
    commands_list: List[str] = ["help", "quit"]
    while True:
        console_user_command = input("Enter a command: ")
        match console_user_command:
            case "help":
                for command in commands_list:
                    print(command)
            case "quit":
                break
            case "Add":
                print("Adding file")

if __name__ == "__main__":
    print("To see all commands, type 'help'.")
    user_interface()