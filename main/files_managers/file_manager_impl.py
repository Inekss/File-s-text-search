import codecs
import os

import chardet

from main.files_managers.file_manager import FileManager
from main.local_logger.custom_exceptions.file_not_exist_exception import (
    FileNotExistException,
)
from main.local_logger.custom_exceptions.unable_read_file_exception import (
    UnableReadFileException,
)


class FileManagerImpl(FileManager):
    def file_exist(self, file_path) -> bool:
        if not os.path.isfile(file_path):
            try:
                raise FileNotExistException("reader: No file in directory")
            except FileNotExistException:
                return False
        return True

    def simple_search_txt_log_json(self, search_term: str, path: str) -> str:
        def detect_encoding(encoding_path):
            with open(encoding_path, "rb") as f:
                raw_data = f.read(1000)
            result = chardet.detect(raw_data)
            return result["encoding"]

        encoding = detect_encoding(path)

        if not encoding:
            return ""

        try:
            matches = []
            with codecs.open(path, "r", encoding=encoding, errors="ignore") as file:
                for i, line in enumerate(file, start=1):
                    if search_term.lower() in line.lower():
                        matches.append(f"{i}: {line.strip()}")

            return "\n".join(matches) if matches else ""

        except Exception as e:
            try:
                raise UnableReadFileException(f"reader: corrupted file TO READ {e}")
            except UnableReadFileException:
                return ""
