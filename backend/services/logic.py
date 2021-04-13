"""Stateless function helpers to support business logics
"""
from os import environ
from random import choice
from string import digits


def make_file_path() -> str:
    dir_path = environ.get("DATA_DIR", "static/")
    hash = "".join([choice(digits) for _ in range(4)])
    file_name = f"data-{hash}.txt"
    path = dir_path + file_name
    return path


def get_file_name(path: str) -> str:
    return path[7:]


def convert_file_size(size_str: str) -> int:
    """Allow custom size for file-writer's writing operation"""
    try:
        if "K" in size_str:
            val, unit = size_str.split("K")
            return int(val) * 1024

        if "M" in size_str:
            val, unit = size_str.split("M")
            return int(val) * 1024 * 1024

        return int(size_str)
    except Exception:
        return 0


def fix_file_name(file_name: str) -> str:
    if not file_name:
        return ""

    if ".txt" not in file_name:
        file_name += ".txt"

    return file_name
