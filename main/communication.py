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
        filetypes=(("Text files", "*.txt"), ("JSON files", "*.json"), ("LOG files", "*.log"), ("DOCX files", "*.docx"),
                   ("PDF files", "*.pdf"), ("XML files", "*.xml"), ("YML files", "*.yml"), ("All files", "*.*")),
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


def json_file_picker():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    root.deiconify()  # Make the root window appear
    root.lift()  # Bring it to the front
    root.focus_force()  # Force focus
    file_path = filedialog.askopenfilename(
        title="Select a JSON File",
        filetypes=(("JSON files", "*.json"), ("All files", "*.*")),
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

def log_file_picker():
    root = tk.Tk()
    root.withdraw()
    root.deiconify()
    root.lift()
    root.focus_force()
    file_path = filedialog.askopenfilename(
        title="Select a LOG File",
        filetypes=(("LOG files", "*.log"), ("All files", "*.*")),
    )
    root.withdraw()

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


def docx_file_picker():
    root = tk.Tk()
    root.withdraw()
    root.deiconify()
    root.lift()
    root.focus_force()
    file_path = filedialog.askopenfilename(
        title="Select a DOCX File",
        filetypes=(("DOCX files", "*.docx"), ("All files", "*.*")),
    )
    root.withdraw()

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


def pdf_file_picker():
    root = tk.Tk()
    root.withdraw()
    root.deiconify()
    root.lift()
    root.focus_force()
    file_path = filedialog.askopenfilename(
        title="Select a PDF File",
        filetypes=(("PDF files", "*.pdf"), ("All files", "*.*")),
    )
    root.withdraw()

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


def xml_file_picker():
    root = tk.Tk()
    root.withdraw()
    root.deiconify()
    root.lift()
    root.focus_force()
    file_path = filedialog.askopenfilename(
        title="Select an XML File",
        filetypes=(("XML files", "*.xml"), ("All files", "*.*")),
    )
    root.withdraw()

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


def yml_file_picker():
    root = tk.Tk()
    root.withdraw()
    root.deiconify()
    root.lift()
    root.focus_force()
    file_path = filedialog.askopenfilename(
        title="Select a YML File",
        filetypes=(("YML files", "*.yml"), ("All files", "*.*")),
    )
    root.withdraw()

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
    text_file_properties = file_picker()
    print(text_file_properties)

    json_file_properties = json_file_picker()
    print(json_file_properties)

    log_file_properties = log_file_picker()
    print(log_file_properties)

    docx_file_properties = docx_file_picker()
    print(docx_file_properties)

    pdf_file_properties = pdf_file_picker()
    print(pdf_file_properties)

    xml_file_properties = xml_file_picker()
    print(xml_file_properties)

    yml_file_properties = yml_file_picker()
    print(yml_file_properties)