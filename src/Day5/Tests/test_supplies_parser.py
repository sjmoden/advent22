from Day5.Components.Supplies9001 import Supplies9001
from Day5.Components.Supplies9000 import Supplies9000
from Day5.Components.SuppliesParser import parse_supplies, parse_instructions
from Day5.Components.SuppliesTypeEnum import SuppliesType

test_input = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 14 from 14 to 24"""

line_input = test_input.splitlines()


def test_supplies_are_parsed_correctly():
    supplies = parse_supplies(line_input, SuppliesType.v9000)
    assert len(supplies.container_state) == 3
    assert len(supplies.container_state[0]) == 2
    assert len(supplies.container_state[1]) == 3
    assert len(supplies.container_state[2]) == 1
    assert supplies.container_state[0][-1] == "N"
    assert supplies.container_state[1][-1] == "D"
    assert supplies.container_state[2][-1] == "P"


def test_instructions_are_parsed_correctly():
    instructions = parse_instructions(line_input)
    assert len(instructions) == 4
    assert instructions[0].number_to_move == 1
    assert instructions[0].starting_position == 1
    assert instructions[0].target_position == 0
    assert instructions[1].number_to_move == 3
    assert instructions[1].starting_position == 0
    assert instructions[1].target_position == 2
    assert instructions[2].number_to_move == 2
    assert instructions[2].starting_position == 1
    assert instructions[2].target_position == 0
    assert instructions[3].number_to_move == 14
    assert instructions[3].starting_position == 13
    assert instructions[3].target_position == 23


def test_supplies_9000_is_returned():
    supplies = parse_supplies(line_input, SuppliesType.v9000)
    assert type(supplies) is Supplies9000


def test_supplies_9001_is_returned():
    supplies = parse_supplies(line_input, SuppliesType.v9001)
    assert type(supplies) is Supplies9001

