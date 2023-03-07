from aocd import get_data

from Day4.Components.WorkOrderParser import parse_line

data = get_data(day=4, year=2022)
data_lines = data.splitlines()


def get_containing_work_order(value):
    work_orders = parse_line(value)
    return work_orders[0].check_if_another_work_order_is_contained_in_this_work_order(work_orders[1]) \
        or work_orders[1].check_if_another_work_order_is_contained_in_this_work_order(work_orders[0])


def find_day4_part1_solution():
    return len([data_line for data_line in data_lines if get_containing_work_order(data_line)])


def get_overlapping_work_order(value):
    work_orders = parse_line(value)
    return work_orders[0].check_if_another_work_order_contains_overlapping_work(work_orders[1])


def find_day4_part2_solution():
    return len([data_line for data_line in data_lines if get_overlapping_work_order(data_line)])
