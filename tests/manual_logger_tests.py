import os
import sys

import pytest

# Add project root to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main.local_logger.custom_logger import CustomLogger as Logger

# Ensure tests use the correct data storage directory
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA_STORAGE_PATH = os.path.join(PROJECT_ROOT, "main", "data_storage")


def test_logger():
    logger = Logger()

    file_properties = {
        "file_path": "test_file2.txt",
        "file_name": "test_file2",
        "file_size": "2KB",
        "file_format": ".txt",
    }

    result = logger.files_properties(file_properties)

    assert result


if __name__ == "__main__":
    pytest.main()
