"""Stateless function helpers to support business logics
"""
from random import choice
from string import digits


def make_file_path() -> str:
    prefix = "static/data-"
    suffix = "".join([choice(digits) for _ in range(4)])
    ext = ".txt"
    path = prefix + suffix + ext
    return path


def get_file_name(path: str) -> str:
    return path[7:]
