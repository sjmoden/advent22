from Day4.Components.WorkOrderParser import parse_line


def test_parse_line_returns_correct_values():
    work_orders = parse_line("2-6,4-8")
    assert work_orders[0].command == "2-6"
    assert work_orders[1].command == "4-8"
