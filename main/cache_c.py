
import os

def clean_cache():
    for root, dirs, files in os.walk('../cache_cleaner'):
        for dir in dirs:
            if dir == '__pycache__':
                cache_dir = os.path.join(root, dir)
                for file in os.listdir(cache_dir):
                    file_path = os.path.join(cache_dir, file)
                    os.remove(file_path)
                os.rmdir(cache_dir)
