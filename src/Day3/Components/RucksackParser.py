from collections import namedtuple


def parse_line(value):
    len_value = len(value)
    value_mid_point = int(len_value / 2)

    rucksack = namedtuple("RuckSack", ["compartment1", "compartment2"])
    return rucksack(value[:value_mid_point], value[value_mid_point:len_value])


def parse_line_into_groups_of_three(values):
    loop_value = 1
    return_values = []
    return_value = []
    for value in values:
        return_value.append(value)

        if loop_value % 3 == 0:
            return_values.append(return_value)
            return_value = []

        loop_value += 1

    return return_values


def get_intersect_single(compartment1, compartment2):
    intersect = get_intersect(compartment1, compartment2)

    if 1 < len(intersect) != intersect.count(intersect[0]):
        raise Exception('Too many values')

    return intersect[0]


def get_intersect(compartment1, compartment2):
    intersect = [value for value in compartment1 if value in compartment2]
    return intersect


def get_intersect_from_group_of_three(value):
    intersect1 = get_intersect(value[0], value[1])
    intersect2 = get_intersect(intersect1, value[2])
    return intersect2[0]
