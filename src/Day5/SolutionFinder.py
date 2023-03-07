from aocd import get_data
from Day5.Components.SuppliesParser import parse_supplies, parse_instructions
from Day5.Components.SuppliesTypeEnum import SuppliesType

data = get_data(day=5, year=2022)
data_lines = data.splitlines()
instructions = parse_instructions(data_lines)


def get_solution(supplies_type):
    supplies = parse_supplies(data_lines,supplies_type)
    for instruction in instructions:
        supplies.rearrange_stack(instruction.number_to_move, instruction.starting_position, instruction.target_position)
    return supplies.output_top_of_stack_code()


def find_day5_part1_solution():
    return get_solution(SuppliesType.v9000)


def find_day5_part2_solution():
    return get_solution(SuppliesType.v9001)
