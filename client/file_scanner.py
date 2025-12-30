import os
from config import SUPPORTED_EXTENSIONS, MAX_FILE_SIZE
from exceptions import ValidationError

def scan_project(directory):
    files = {}
    for root, _, filenames in os.walk(directory):
        for name in filenames:
            if any(name.endswith(ext) for ext in SUPPORTED_EXTENSIONS):
                path = os.path.join(root, name)
                if os.path.getsize(path) > MAX_FILE_SIZE:
                    raise ValidationError(f"{name} too large")
                with open(path, "r") as f:
                    files[path] = f.read()
    if not files:
        raise ValidationError("No source files found")
    return files
