from Day7.Components.Directory import Directory


def test_ls_results_are_correct():
    directory = Directory("\\", None)
    directory.input_ls_result("dir a")
    directory.input_ls_result("14848514 b.txt")
    directory.input_ls_result("8504156 c.dat")
    assert len(directory.sub_directories) == 1
    assert directory.sub_directories[0].name == "a"
    assert len(directory.files) == 2
    assert directory.files[0].name == "b.txt"
    assert directory.files[0].size == 14848514
    assert directory.files[1].name == "c.dat"
    assert directory.files[1].size == 8504156


def test_ls_result_for_directories_are_not_duplicated():
    directory = Directory("\\", None)
    directory.input_ls_result("dir a")
    directory.input_ls_result("dir a")
    assert len(directory.sub_directories) == 1


def test_ls_result_for_files_are_not_duplicated():
    directory = Directory("\\", None)
    directory.input_ls_result("14848514 b.txt")
    directory.input_ls_result("14848514 b.txt")
    assert len(directory.files) == 1


def test_cd():
    directory = Directory("\\", None)
    directory.input_ls_result("dir a")
    new_directory = directory.cd("a")
    assert new_directory.name == "a"


def test_cd_up_a_level():
    directory = Directory("\\", None)
    directory.input_ls_result("dir a")
    a_directory = directory.cd("a")
    prev_directory = a_directory.cd("..")
    assert prev_directory.name == "\\"


def test_directory_size_is_correct():
    directory = Directory("\\", None)
    directory.input_ls_result("dir a")
    directory.input_ls_result("1 b.txt")
    directory.input_ls_result("10 c.dat")
    a_directory = directory.cd("a")
    a_directory.input_ls_result("100 e.dat")
    assert directory.return_directory_size() == 111


def test_return_all_subdirectories():
    directory = Directory("\\", None)
    directory.input_ls_result("dir a")
    a_directory = directory.cd("a")
    a_directory.input_ls_result("dir b")
    assert len(directory.return_all_subdirectories()) == 2
    assert directory.return_all_subdirectories()[0].name == "a"
    assert directory.return_all_subdirectories()[1].name == "b"
