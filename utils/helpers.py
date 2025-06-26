from datetime import datetime
from pathlib import Path
from typing import Union
import os

def get_object_type_name(value):
    return type(value).__name__



def get_full_file_path(folder_name: str) -> str:
    """
    Method name: get_full_file_path
       Params: folder_name which is a string and -> str annotation indicates that this function returns a string.
       --> str is just for readers clarity. it is optional. you can still return a string. """
    print(get_full_file_path.__doc__)
    root = Path(__file__).resolve().parent      # same as dirname+abspath
    target = root.parents[1] / folder_name      # parents[0] is one up, parents[1] two up
    return str(target)



def read_file_from_path_and_get_file_content(json_folder_name, file_name, base_path):
    try:
        # Determine the directory into which we'll write
        # if base_path is provided then it take that, else base is set to absolute path where the current.py file exists
        if base_path:
            print('inside if base_path')
            dir_path = os.path.join(base_path, json_folder_name)
        else:
            dir_path = os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                json_folder_name
            )
        print("read dir path is : "+dir_path)
        # Create that directory (and any parents) if it doesn't exist
        os.makedirs(dir_path, exist_ok=True)

        # Build the final file path
        file_path = os.path.join(dir_path, file_name)
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


def write_to_file_from_path(json_folder_name, file_name, stringToPass,base_path):
    try:
            # Determine the directory into which we'll write
            # if base_path is provided then it take that, else base is set to absolute path where the current.py file exists
            if base_path:
                dir_path = os.path.join(base_path, json_folder_name)
            else:
                dir_path = os.path.join(
                    os.path.dirname(os.path.abspath(__file__)),
                    json_folder_name
                )
            print(dir_path)
            # Create that directory (and any parents) if it doesn't exist
            os.makedirs(dir_path, exist_ok=True)

            # Build the final file path
            file_path = os.path.join(dir_path, file_name)
            print("Writing to:", file_path)
            print(stringToPass)
            try:
            # Now write safely
                with open(file_path, "w", encoding="utf-8") as f:
                     f.write(stringToPass)
            except Exception as e:
                raise Exception(f"Error writing file: {e}")
    except Exception as e:
        raise  Exception(f"Unable to create file: {e}")


