import os
from typing import Generator
from random import choice
from string import digits
from models import FileInfo


class FileWriter:
    def __init__(self, path=None, max_size=1024):
        """
        Max-size for a file to write to is 1Kb
        """
        self.set_path(path=path)
        self.max_size = max_size

    def set_path(self, path=None):
        if not path:
            prefix = "static/data-"
            suffix = "".join([choice(digits) for _ in range(4)])
            ext = ".txt"
            path = prefix + suffix + ext

        self.path = path

    def write(self, stream_generator: Generator, path=None) -> FileInfo:
        path = path or self.path
        info = FileInfo(name=path[8:], size=0)

        with open(path, "w+") as f:
            while f.tell() < self.max_size:
                f.write(next(stream_generator))
            info.size = f.tell()

        return info
