from abc import abstractmethod


class StorageFileManager:

    @abstractmethod
    def data_storage_exists(self, file_path) -> bool:
        pass

    @abstractmethod
    def load_data_storage_file(self, file_path: str) -> dict:
        pass

    @abstractmethod
    def save_data_storage_file(self, file_path: str, data: dict) -> bool:
        pass

    @abstractmethod
    def show_error_storage(self):
        pass

    @abstractmethod
    def show_processed_data_storage(self):
        pass

    @abstractmethod
    def show_file_info_data_storage(self):
        pass
