from typing import List


class InvalidCommand(Exception):
    def __init__(self, command: List[str], cli: str) -> None:
        super().__init__(f"Invalid command: {command}\n\n{cli}")


class InvalidSourcePath(Exception):
    def __init__(self, path: str) -> None:
        super().__init__(f"Non-existent source path: {path}")
