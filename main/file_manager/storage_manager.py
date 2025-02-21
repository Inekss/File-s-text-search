from abc import abstractmethod


class StorageFileManager:

    @abstractmethod
    def data_storage_exists(self, file_path) -> bool:
        pass

    @abstractmethod
    def load_data_storage_file(self, file_path: str) -> dict:
        pass

    @abstractmethod
    def save_data_storage_file(self, file_path: str, data: dict):
        pass
