import os


def get_abs_path(file_path: str, rel_path: str) -> str:
    script_dir = os.path.dirname(file_path)
    return os.path.join(script_dir, rel_path)