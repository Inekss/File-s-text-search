class InvalidJsonException(Exception):
    """Custom exception for file properties validation errors."""

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
        dict_message = {
            "error": {
                "error_status": True,
                "error_type": "contains invalid JSON",
                "error_message": "broken JSON",
                "error_description": message,
                "error_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            }
        }
        error_handling(logger, dict_message)

    def error_handling(self, message: dict) -> bool:
        """Logs errors into 'error_data.json'."""
        data_folder = r"data_storage"

        data_path = os.path.join(data_folder, "error_data.json")
        try:
            existing_data = Man.load_data_storage_file(man, data_path)
        except Exception:
            return False  # have rights to have no handling

        if not isinstance(existing_data, dict):
            existing_data = {"errors": []}
        elif "errors" not in existing_data:
            existing_data["errors"] = []

        existing_data["errors"].append(message)
        try:
            Man.save_data_storage_file(man, data_path, existing_data)
        except Exception:
            return False  # have rights to have no handling
        return True
