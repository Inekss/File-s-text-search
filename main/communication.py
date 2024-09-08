import tkinter as tk
from tkinter import filedialog
import os
import time


def file_picker():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)

    file_types = (
        ("Text files", "*.txt"),
        ("JSON files", "*.json"),
        ("LOG files", "*.log"),
        ("DOCX files", "*.docx"),
        ("PDF files", "*.pdf"),
        ("XML files", "*.xml"),
        ("YML files", "*.yml"),
        ("All files", "*.*")
    )

    file_types = [ft for ft in file_types if ft[0] != "All files"] + [ft for ft in file_types if ft[0] == "All files"]

    file_path = filedialog.askopenfilename(
        title="Select a File",
        filetypes=file_types
    )

    root.destroy()  # Закрити вікно root

    if file_path:
        try:
            file_name = os.path.basename(file_path)
            file_size = os.path.getsize(file_path)
            file_format = os.path.splitext(file_name)[1]
            file_properties = {
                "file_path": file_path,
                "file_name": file_name,
                "file_size": file_size,
                "file_format": file_format,
            }
            return file_properties
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
        errors_report = {
            "error_status": True,
            "error_type": "file_picker",
            "error_message": "file not found",
            "error_description": "unable to choose a file using file picker",
            "error_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        }
        return errors_report


if __name__ == "__main__":
    result = file_picker()
    print(result)