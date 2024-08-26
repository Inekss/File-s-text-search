import tkinter as tk
from tkinter import filedialog
import os


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
        print(f"File selected: {file_path}")
        try:
            file_name = os.path.basename(file_path)
            file_size = os.path.getsize(file_path)
            file_format = os.path.splitext(file_name)[1]
        except Exception as e:
            print(f"Problem with file properties: {e}")
        else:
            file_properties = [file_path, file_name, file_size, file_format]
            for prop in file_properties:
                print(prop)
    else:
        print("No file selected")


if __name__ == "__main__":
    file_picker()
