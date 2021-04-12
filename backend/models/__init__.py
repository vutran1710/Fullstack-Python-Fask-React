from pydantic import BaseModel


class FileInfo(BaseModel):
    name: str
    size: int
