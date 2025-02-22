from abc import abstractmethod


class FileManager:

    @abstractmethod
    def file_exist(self, file_path: str) -> bool:
        pass

    @abstractmethod
    def simple_search_txt_log_json(
        self, search_term: str, path: str
    ) -> list[dict[str, dict[int, str]]]:
        pass

    @abstractmethod
    def simple_search_in_docx(
        self, search_term: str, path: str
    ) -> list[dict[str, dict[int, str]]]:
        pass

    def simple_search_pdf(
        self, search_term: str, path: str
    ) -> list[dict[str, dict[int, str]]]:
        pass
