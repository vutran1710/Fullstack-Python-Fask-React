from typing import Optional
from pydantic import BaseModel
from services.logic import get_file_name


class FileInfo(BaseModel):
    path: str
    size: int
    name: Optional[str]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = get_file_name(self.path)


class DataReport(BaseModel):
    strings: int = 0
    reals: int = 0
    integers: int = 0
    alpha_numerics: int = 0

    def update(self, _, data_type: str):
        type_map = {
            "str": "strings",
            "real": "reals",
            "int": "integers",
            "alpha_numeric": "alpha_numerics",
        }
        attr = type_map[data_type]
        current = getattr(self, attr)
        setattr(self, attr, current + 1)


class GenDataAPIResponse(BaseModel):
    file: str
    requested_size: int

    def __init__(self, /, path=None, size=None):
        name = get_file_name(path)
        super().__init__(file=name, requested_size=size)


class DataReportAPIResponse(DataReport):
    pass


class StatusAPIResponse(BaseModel):
    file: str
    status: str
