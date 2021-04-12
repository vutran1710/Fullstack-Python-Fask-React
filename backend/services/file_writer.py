import os
from typing import Generator
from random import choice
from string import digits
from models import FileInfo
from .logic import get_file_name


class FileWriter:
    def __init__(self, max_size=1024):
        self.max_size = max_size

    def write(self, path: str, data_stream: Generator) -> FileInfo:
        info = FileInfo(path=path, size=0)

        with open(path, "w+") as f:
            while f.tell() < self.max_size:
                f.write(next(data_stream))
            info.size = f.tell()

        return info
