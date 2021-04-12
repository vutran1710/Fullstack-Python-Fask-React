import services.logic as Logic


def test_file_path_logic():
    path = Logic.make_file_path()
    assert ".txt" in path
    assert "data" in path

    file_name = Logic.get_file_name(path)
    print(path, file_name)
    assert file_name.startswith("data-")
