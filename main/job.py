import os
import codecs
import chardet
from docx import Document

import time


def search_in_txt_log_json(search_term, path):
    def detect_encoding(encoding_path):
        with open(encoding_path, "rb") as file:
            raw_data = file.read(10000)  # Read a small chunk of the file
        result = chardet.detect(raw_data)
        return result["encoding"]

    encoding = detect_encoding(path)

    if not encoding:
        errors_report = {
            "error_status": True,
            "error_type": "encoding_error",
            "error_message": path,
            "error_description": "Unable TO ENCODE",
            "error_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        }
        return errors_report

    try:
        with codecs.open(path, "r", encoding=encoding, errors="ignore") as file:
            content = file.read()

        lines = content.split("\n")
        matches = [
            f"{i + 1}: {line.strip()}"
            for i, line in enumerate(lines)
            if search_term.lower() in line.lower()
        ]

        if matches:
            return "\n".join(matches)
        else:
            return False

    except Exception as e:
        errors_report = {
            "error_status": True,
            "error_type": "corrupted_file",
            "error_message": path,
            "error_description": f"Error: corrupted file TO READ {e}",
            "error_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        }
        return errors_report


def search_in_docx(search_term, path):
    try:
        doc = Document(path)
        matches = []

        for i, para in enumerate(doc.paragraphs):
            if search_term.lower() in para.text.lower():
                matches.append(f"{i + 1}: {para.text.strip()}")

        if matches:
            return "\n".join(matches)
        else:
            return False

    except Exception as e:
        errors_report = {
            "error_status": True,
            "error_type": "corrupted_file",
            "error_message": path,
            "error_description": f"Error: corrupted file TO READ {e}",
            "error_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        }
        return errors_report


def reader(search_request, path):
    if not os.path.isfile(path):
        errors_report = {
            "error_status": True,
            "error_type": "file_not_found",
            "error_message": path,
            "error_description": "No file in directory",
            "error_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        }
        return errors_report

    match path.lower():
        case path if path.endswith(".docx"):
            output = search_in_docx(search_request, path)
        case path if path.endswith(".txt") or path.endswith(".log") or path.endswith(
            ".json"
        ):
            output = search_in_txt_log_json(search_request, path)
        case _:
            errors_report = {
                "error_status": True,
                "error_type": "file_format",
                "error_message": path,
                "error_description": "Unsupported file format",
                "error_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            }
            return errors_report

    if not output:
        no_result = {
            "file_path": path,
            "search_request": search_request,
            "search_result": None,
            "search_status": False,
        }
        return no_result
    else:
        result = {
            "file_path": path,
            "search_request": search_request,
            "search_result": output,
            "search_status": True,
        }
        return result


if __name__ == "__main__":
    file_path = r"D:/PyCharm 2024.1.4/File-s-text-search/requirements.txt"
    request = "ddddddsd"
    find = reader(request, file_path)
    print(find)
