import os


def parent_dirs_exist(path: str) -> bool:
    return os.path.exists(os.path.dirname(path))


def create_parent_dirs(path: str) -> None:
    os.makedirs(os.path.dirname(path))
