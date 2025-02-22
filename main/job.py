from main.files_managers.file_manager_impl import FileManagerImpl as FileManager
from main.local_logger.custom_exceptions.invalid_input_exception import (
    InvalidInputException,
)
from main.local_logger.custom_exceptions.unsupported_format_exception import (
    UnsupportedFormatException,
)

fman = FileManager()


def simple_search_client(search_request: str, path: str) -> dict:
    if not FileManager.file_exist(fman, path) or path == "" or search_request == "":
        try:
            raise InvalidInputException(
                "simple_search_client return False while input validation"
            )
        except InvalidInputException:
            return {}

    match path.lower():
        case path if path.endswith(".docx") or path.endswith(".doc"):
            output = FileManager.simple_search_in_docx(fman, search_request, path)
        case path if path.endswith(".txt") or path.endswith(".log") or path.endswith(
            ".json"
        ):
            output = FileManager.simple_search_txt_log_json(fman, search_request, path)
        case path if path.endswith(".pdf"):
            output = FileManager.simple_search_pdf(fman, search_request, path)
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
