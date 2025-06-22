import os
import json

def load_payload(file_path, overrides=None):
    full_path = os.path.join(os.path.dirname(__file__), "..", file_path)
    print("The file path it is reading from is "+full_path)
    with open(full_path) as f:
        payload = json.load(f)
    if overrides:
        payload.update(overrides)
    return payload