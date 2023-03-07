from aocd import get_data
from Day2.Components.RockPaperScissorGame import get_score
from Day2.Components.StategyParser import parse_line, parse_line2, parse_your_move

data = get_data(day=2, year=2022)
data_lines = data.splitlines()


def get_score_from_input_line(value):
    parsed_values = parse_line(value)
    return get_score(parsed_values.opponents_play, parsed_values.your_play)


def find_day2_part1_solution():
    return sum([get_score_from_input_line(data_line) for data_line in data_lines])


def get_score_from_input_line2(value):
    parsed_value = parse_line2(value)
    parsed_your_move = parse_your_move(parsed_value.opponents_play, parsed_value.required_result)
    return get_score(parsed_value.opponents_play, parsed_your_move)


def find_day2_part2_solution():
    return sum([get_score_from_input_line2(data_line) for data_line in data_lines])
