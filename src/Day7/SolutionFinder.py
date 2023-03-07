from aocd import get_data

from Day7.Components.TerminalParse import parse_terminal

data = get_data(day=7, year=2022)
data_lines = data.splitlines()
directory = parse_terminal(data_lines)
all_sub_directory = directory.return_all_subdirectories()


def find_day7_part1_solution():
    return sum(x.return_directory_size() for x in all_sub_directory if x.return_directory_size() <= 100000)


def find_day7_part2_solution():
    size_of_filestream = 70000000
    required_space_for_update = 30000000
    space_used = directory.return_directory_size()
    space_left = size_of_filestream - space_used
    space_required = required_space_for_update - space_left
    all_sub_directory.sort(key=lambda x: x.return_directory_size())
    for x in all_sub_directory:
        if x.return_directory_size() >= space_required:
            return x.return_directory_size()
