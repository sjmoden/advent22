from Day7.Components.Directory import Directory


def parse_terminal(terminal_input):
    directory = Directory("\\", None)
    curr_directory = directory
    is_ls = False

    for line in terminal_input:
        if line == "$ cd /":
            continue
        if not line.startswith("$") and is_ls:
            curr_directory.input_ls_result(line)
        if line.startswith("$") and not line == "$ ls":
            is_ls = False
        if line.startswith("$ cd"):
            curr_directory = curr_directory.cd(line.replace("$ cd ", ""))
        if line == "$ ls":
            is_ls = True

    return directory
