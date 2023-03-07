from collections import namedtuple
from Day5.Components.Supplies9000 import Supplies9000
from Day5.Components.Supplies9001 import Supplies9001
from Day5.Components.SuppliesTypeEnum import SuppliesType


def parse_supplies(supplies_input, supplies_type):
    starting_location = 0
    number_of_columns = 0

    for line in supplies_input:
        if line.startswith(" 1"):
            number_of_columns = int(max(line))
            break
        starting_location += 1

    supplies_stacks = [[] for x in range(number_of_columns)]

    for line_position in range(starting_location, 0, -1):
        line = supplies_input[line_position - 1]
        for column in range(0, number_of_columns):
            item_position = (column * 4) + 1
            supply_item = line[item_position:item_position + 1]
            if supply_item and supply_item.strip():
                supplies_stacks[column].append(supply_item)

    match supplies_type:
        case SuppliesType.v9000:
            return Supplies9000(supplies_stacks)
        case SuppliesType.v9001:
            return Supplies9001(supplies_stacks)


def parse_instructions(supplies_input):
    instruction = namedtuple("Instructions", ["number_to_move", "starting_position", "target_position"])
    instructions = []

    for line in supplies_input:
        if not line.startswith("move"):
            continue

        line_split = line.replace('move', '').replace('from', ',').replace('to', ',').split(',')
        instructions.append(instruction(int(line_split[0]), int(line_split[1])-1, int(line_split[2])-1))

    return instructions
