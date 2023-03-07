from Day1.Components.Elf import Elf


def parse_input_string(input_string):
    elves = []
    input_split = input_string.split('\n\n')
    for input_group in input_split:
        input_group_split = input_group.splitlines()
        input_group_split_int = list(map(int, input_group_split))
        elves.append(Elf(input_group_split_int))
    return elves
