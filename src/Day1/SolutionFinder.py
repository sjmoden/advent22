from aocd import get_data

from Day1.Components.ElvesParser import parse_input_string

input_url = "https://adventofcode.com/2022/day/1/input"

data = get_data(day=1, year=2022)
elves = parse_input_string(data)
elves_calories = [elf.get_calorie_sum() for elf in elves]
elves_calories.sort(reverse=True)


def find_day1_part1_solution():
    return elves_calories[0]


def find_day1_part2_solution():
    return elves_calories[0] + elves_calories[1] + elves_calories[2]
