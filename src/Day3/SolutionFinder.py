from aocd import get_data

from Day3.Components.PriorityParser import parse_priority
from Day3.Components.RucksackParser import parse_line, get_intersect_single, parse_line_into_groups_of_three, \
    get_intersect_from_group_of_three

data = get_data(day=3, year=2022)
data_lines = data.splitlines()


def get_priority_from_input_line(value):
    rucksack = parse_line(value)
    intersect = get_intersect_single(rucksack.compartment1, rucksack.compartment2)
    return parse_priority(intersect)


def find_day3_part1_solution():
    return sum([get_priority_from_input_line(data_line) for data_line in data_lines])


def get_priority_from_input_line_group_of_three(value):
    intersect = get_intersect_from_group_of_three(value)
    return parse_priority(intersect)


def find_day3_part2_solution():
    group_of_threes = parse_line_into_groups_of_three(data_lines)
    return sum([get_priority_from_input_line_group_of_three(group_of_three) for group_of_three in group_of_threes])
