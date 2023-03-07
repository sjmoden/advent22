from aocd import get_data

from Day6.Componets.SignalReader import SignalReader

data = get_data(day=6, year=2022)
signal_reader = SignalReader(data)


def find_day6_part1_solution():
    return signal_reader.get_starting_position()


def find_day6_part2_solution():
    return signal_reader.get_start_of_message_marker()
