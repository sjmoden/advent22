from Day4.Components.WorkOrder import WorkOrder


def parse_line(value):
    value_split = value.split(',')
    return [WorkOrder(value_split[0]), WorkOrder(value_split[1])]