from abc import abstractmethod


class FileManager:

    @abstractmethod
    def file_exist(self, file_path) -> bool:
        pass

    @abstractmethod
    def simple_search_txt_log_json(self, search_term: str, path: str) -> str:
        pass
