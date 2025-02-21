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
        filetypes=(("Text files", "*.txt"), ("All files", "*.*")),
    )
    root.withdraw()  # Hide the root window again

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


if __name__ == "__main__":
    file_picker()
