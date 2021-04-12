from typing import Optional
from pydantic import BaseModel
from services.logic import get_file_name


class FileInfo(BaseModel):
    name: Optional[str]
    path: str
    size: int

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = get_file_name(self.path)
