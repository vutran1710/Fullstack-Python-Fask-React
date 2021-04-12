from services import FileWriter, DataGenerator
from models import FileInfo


def test_path():
    f = FileWriter()
    print(f.path)
    assert f.path
    assert ".txt" in f.path


def test_write():
    f = FileWriter()
    dg = DataGenerator()

    def content_generator():
        while True:
            yield dg.random_str() + ", "

    stream_content = content_generator()

    info = f.write(stream_content)
    assert isinstance(info, FileInfo)
    assert int(info.size / 1024) == 1  # NOTE: 1kb

    f = FileWriter(max_size=100)
    info = f.write(stream_content)
    assert isinstance(info, FileInfo)
    assert int(info.size / 100) == 1  # NOTE: 100 bytes
