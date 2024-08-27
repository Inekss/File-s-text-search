import tkinter as tk
from tkinter import filedialog
import os
import time


def file_picker():
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
        except Exception as e:
            errors_report = {
                "error_status": True,
                "error_type": "corrupted_file",
                "error_message": file_path,
                "error_description": f"Error: corrupted file TO PEAK {e}",
                "error_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            }
            return errors_report
        else:
            file_properties = {
                "file_path": file_path,
                "file_name": file_name,
                "file_size": file_size,
                "file_format": file_format,
            }
            return file_properties
    else:
        errors_report = {
            "error_status": True,
            "error_type": "file_picker",
            "error_message": "file not found",
            "error_description": "unable to choose a file using file picker",
            "error_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        }
        return errors_report


if __name__ == "__main__":
    file_picker()
