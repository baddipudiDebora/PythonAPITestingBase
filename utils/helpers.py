from typing import Union
import os

def get_object_type_name(value):
    return type(value).__name__



def get_full_file_path(folder_name: str) -> str:
    root_path = os.path.dirname(os.path.abspath(__file__))
    # Explicitly cast to str to satisfy strict type checkers
    relative_path = os.path.join("..", "..", folder_name)
    full_path = os.path.abspath(os.path.join(root_path, relative_path))
    return full_path


def read_file_from_path_and_get_file_content(json_folder_name, file_name, base_path=None):
    try:
        base = base_path or os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base, json_folder_name, file_name)
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        raise Exception(
            f"Error reading JSON sample from folder: {json_folder_name} with filename: {file_name}"
        ) from e

def store_json_sample_string(json_folder_name, file_name, base_path=None):
    from_file_path = read_file_from_path_and_get_file_content(json_folder_name, file_name, base_path)

    if not from_file_path:
        raise ValueError("JSON sample string must not be null or empty")

    return from_file_path