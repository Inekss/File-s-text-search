import codecs
import os

import chardet
from docx import Document
import pdfplumber

from main.files_managers.file_manager import FileManager
from main.local_logger.custom_exceptions.file_not_exist_exception import (
    FileNotExistException,
)
from main.local_logger.custom_exceptions.unable_read_file_exception import (
    UnableReadFileException,
)


class FileManagerImpl(FileManager):
    def file_exist(self, file_path: str) -> bool:
        if not os.path.isfile(file_path):
            try:
                raise FileNotExistException("reader: No file in directory")
            except FileNotExistException:
                return False
        return True

    def simple_search_txt_log_json(
        self, search_term: str, path: str
    ) -> list[dict[str, dict[int, str]]]:
        def detect_encoding(encoding_path):
            try:
                with open(encoding_path, "rb") as f:
                    raw_data = f.read(5000)
                result = chardet.detect(raw_data)
                return result.get("encoding", "utf-8")
            except Exception:
                try:
                    raise UnableReadFileException(f"reader: corrupted file TO READ {e}")
                except UnableReadFileException:
                    return []

        encoding = detect_encoding(path)

        try:
            matches = []
            with codecs.open(path, "r", encoding=encoding, errors="ignore") as file:
                for i, line in enumerate(file, start=1):
                    if search_term.lower() in line.lower():
                        matches.append({"match": {i: line.strip()}})
            return matches
        except Exception as e:
            try:
                raise UnableReadFileException(f"reader: corrupted file TO READ {e}")
            except UnableReadFileException:
                return []

    def simple_search_in_docx(
        self, search_term: str, path: str
    ) -> list[dict[str, dict[int, str]]]:
        try:
            doc = Document(path)
            matches = []

            for i, para in enumerate(doc.paragraphs, start=1):
                if search_term.lower() in para.text.lower():
                    matches.append({"match": {i: para.text.strip()}})

            return matches

        except Exception as e:
            try:
                raise UnableReadFileException(f"reader: corrupted file TO READ {e}")
            except UnableReadFileException:
                return []

    def simple_search_pdf(
        self, search_term: str, path: str
    ) -> list[dict[str, dict[int, str]]]:
        try:
            matches = []

            with pdfplumber.open(path) as pdf:
                for page_num, page in enumerate(pdf.pages, start=1):
                    text = page.extract_text()
                    if text:
                        lines = text.split("\n")
                        for i, line in enumerate(lines, start=1):
                            if search_term.lower() in line.lower():
                                key = f"{i}.{page_num}"
                                matches.append({"match": {key: line.strip()}})

            return matches

        except Exception:
            return []
