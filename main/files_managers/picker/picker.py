import os
import tkinter as tk
from tkinter import filedialog

from main.local_logger.custom_exceptions.file_not_exist_exception import (
    FileNotExistException,
)
from main.local_logger.custom_exceptions.picker_file_corrupted_exception import (
    PickerFileCorruptedException,
)


def file_picker() -> dict:
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    root.deiconify()  # Make the root window appear
    root.lift()  # Bring it to the front
    root.focus_force()  # Force focus
    file_path = filedialog.askopenfilename(
        title="Select a File",
        filetypes=(("All files", "*.*"),),
    )
    root.withdraw()

    if file_path:
        try:
            file_name = os.path.basename(file_path)
            file_size = os.path.getsize(file_path)
            file_format = os.path.splitext(file_name)[1]
        except Exception:
            try:
                raise PickerFileCorruptedException(
                    "Issue appeared while trying to get file properties"
                )
            except PickerFileCorruptedException:
                return {}

        else:
            file_properties = {
                "file_path": file_path,
                "file_name": file_name,
                "file_size": file_size,
                "file_format": file_format,
            }
            return file_properties
    else:
        try:
            raise FileNotExistException("unable to choose a file using file picker")
        except FileNotExistException:
            return {}


def folder_picker() -> dict:
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    root.deiconify()  # Make the root window appear
    root.lift()  # Bring it to the front
    root.focus_force()  # Force focus

    folder_path = filedialog.askdirectory(title="Select a Folder")
    root.withdraw()

    if folder_path:
        try:
            folder_name = os.path.basename(folder_path)
            folder_size = 0
            valid_extensions = {".txt", ".log", ".pdf", ".docx", ".doc"}
            selected_files = {}

            for dp, dn, filenames in os.walk(folder_path):
                for f in filenames:
                    file_path = os.path.join(dp, f)
                    file_ext = os.path.splitext(f)[1].lower()

                    if file_ext in valid_extensions:
                        file_size = os.path.getsize(file_path)
                        folder_size += file_size
                        selected_files[file_path] = {
                            "file_name": f,
                            "file_size": file_size,
                            "file_format": file_ext,
                        }
        except Exception:
            try:
                raise FileNotExistException(
                    "unable to choose a file using folder picker"
                )
            except FileNotExistException:
                return {}

        return {
            "folder_path": folder_path,
            "folder_name": folder_name,
            "folder_size": folder_size,
            "selected_files": selected_files,
        }
    else:
        try:
            raise FileNotExistException("unable to choose a file using folder picker")
        except FileNotExistException:
            return {}


if __name__ == "__main__":
    result = file_picker()
    print(result)
