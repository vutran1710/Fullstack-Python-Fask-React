from services import FileWriter, DataGenerator
from services.logic import make_file_path
from models import FileInfo


def test_path():
    f = FileWriter()
    assert f.max_size == 1024
    f.max_size = 100
    assert f.max_size == 100


def test_write():
    f = FileWriter()
    dg = DataGenerator()

    def content_generator():
        while True:
            yield dg.random_str() + ", "

    stream_content = content_generator()
    path = make_file_path()
    file_info = f.write(path, stream_content)
    assert isinstance(file_info, FileInfo)
    assert int(file_info.size / 1024) == 1  # NOTE: 1kb
    print(file_info.name)
    print(file_info.path)

    f.max_size = 100
    path = make_file_path()
    file_info = f.write(path, stream_content)
    assert isinstance(file_info, FileInfo)
    assert int(file_info.size / 100) == 1  # NOTE: 100 bytes
    print(file_info.name)
    print(file_info.path)
