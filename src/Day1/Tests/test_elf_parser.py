from Day1.Components.ElvesParser import parse_input_string

input_file = """12
13
14

15
16
17

18
"""


def test_correct_number_of_elves_are_passed():
    elves = parse_input_string(input_file)
    assert len(elves) == 3


def test_first_elf_has_correct_calories():
    elves = parse_input_string(input_file)
    assert elves[0].get_calories() == [12,13,14]