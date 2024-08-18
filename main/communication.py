import tkinter as tk
from tkinter import filedialog
import os


def file_picker(user_command: str, call_picker: bool):
    if call_picker:
        # Open a file picker dialog and allow the user to select a file
        if user_command == "file":
            file_path = filedialog.askopenfilename(
                title="Select a File",
                filetypes=(("Text files", "*.txt"), ("All files", "*.*")),
            )

            # Process the selected file
            if file_path:
                print(f"File selected: {file_path}")
                try:
                    file_name = os.path.basename(file_path)
                    file_size = os.path.getsize(file_path)  # Size in bytes
                    file_format = os.path.splitext(file_name)[1]
                except Exception:
                    print(f"Problem with file properties...  {file_path}")
                else:
                    file_properties = [
                        file_path,
                        file_name,
                        file_size,
                        file_format,
                    ]
                    for i in range(len(file_properties)):
                        print(file_properties[i])
            else:
                print("No file selected")

        if user_command == "folder":
            folder_path = filedialog.askdirectory(title="Select a Folder")

            # Process the selected folder
            if folder_path:
                print(f"Folder selected: {folder_path}")
                # Add further processing of the folder here
            else:
                print("No folder selected")
    else:
        print("File picker was not called because the parameter was set to False.")


if __name__ == "__main__":
    command = "file"
    file_picker(command, call_picker=True)
