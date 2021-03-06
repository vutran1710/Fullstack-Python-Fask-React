from os import environ
import services.logic as Logic


def test_file_path_logic():
    def verify_path():
        path = Logic.make_file_path()
        assert ".txt" in path
        assert "data" in path

        file_name = Logic.get_file_name(path)
        print(path, file_name)
        assert file_name.startswith("data-")

    environ["DATA_DIR"] = "asasdf/adfasdf234ad/adfsasdfd"
    verify_path()

    environ["DATA_DIR"] = "/static/data/"
    verify_path()

    del environ["DATA_DIR"]


def test_size_convert():
    size = Logic.convert_file_size("1K")
    assert size == 1024

    size = Logic.convert_file_size("2K")
    assert size == 1024 * 2

    size = Logic.convert_file_size("1M")
    assert size == 1024 * 1024

    size = Logic.convert_file_size("2M")
    assert size == 1024 * 1024 * 2
