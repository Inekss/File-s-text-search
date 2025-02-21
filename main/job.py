import codecs
import time
from typing import Any

import chardet
from docx import Document

from main.files_managers.file_manager_impl import FileManagerImpl as FileManager
from main.local_logger.custom_exceptions.unsupported_format_exception import (
    UnsupportedFormatException,
)

fman = FileManager()


def search_in_docx(search_term, path: str) -> Any:
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


def simple_search_client(search_request, path: str) -> dict:
    if not FileManager.file_exist(fman, path):
        return {}

    match path.lower():
        case path if path.endswith(".docx"):
            output = search_in_docx(search_request, path)
        case path if path.endswith(".txt") or path.endswith(".log") or path.endswith(
            ".json"
        ):
            output = FileManager.simple_search_txt_log_json(fman, search_request, path)
        case _:
            try:
                raise UnsupportedFormatException(
                    "reader: Have no function to do search for that format"
                )
            except UnsupportedFormatException:
                return {}

    if not output:
        return {}
    else:
        return {
            "file_path": path,
            "search_request": search_request,
            "search_result": output,
            "search_status": True,
        }


if __name__ == "__main__":
    file_path = r"requirements.txt"
    request = "black"
    find = reader(request, file_path)
    print(find)
