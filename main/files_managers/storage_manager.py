from abc import abstractmethod


class StorageFileManager:

    @abstractmethod
    def data_storage_exists(self, file_path: str) -> bool:
        pass

    @abstractmethod
    def load_data_from_storage(self, file_path: str) -> dict:
        pass

    @abstractmethod
    def save_data_to_storage(self, file_path: str, data: dict) -> bool:
        pass

    @abstractmethod
    def remove_file_info(self, data: str) -> bool:
        pass

    def clear_st(self) -> bool:
        pass

    @abstractmethod
    def show_error_storage(self) -> bool:
        pass

    @abstractmethod
    def show_processed_data_storage(self) -> bool:
        pass

    @abstractmethod
    def show_file_info_data_storage(self) -> bool:
        pass

    @abstractmethod
    def show_all_data_storage(self) -> bool:
        pass

    def get_st_files_path(self) -> list:
        pass
