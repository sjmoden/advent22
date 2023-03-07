from Day4.Components.WorkOrder import WorkOrder
import pytest


def test_work_order():
    work_order = WorkOrder("3-5")
    assert work_order.get_lower_value() == 3
    assert work_order.get_higher_value() == 5


def test_two_work_orders_that_overlap():
    work_order1 = WorkOrder("2-8")
    work_order2 = WorkOrder("3-5")
    assert work_order1.check_if_another_work_order_is_contained_in_this_work_order(work_order2)


def test_two_work_orders_that_dont_overlap():
    work_order1 = WorkOrder("2-8")
    work_order2 = WorkOrder("3-5")
    assert work_order2.check_if_another_work_order_is_contained_in_this_work_order(work_order1) == False


def test_two_work_orders_that_dont_overlap2():
    work_order1 = WorkOrder("70-73")
    work_order2 = WorkOrder("62-71")
    assert work_order1.check_if_another_work_order_is_contained_in_this_work_order(work_order2) == False


def test_two_work_orders_that_dont_overlap3():
    work_order1 = WorkOrder("70-73")
    work_order2 = WorkOrder("62-71")
    assert work_order2.check_if_another_work_order_is_contained_in_this_work_order(work_order1) == False


testdata = [
    ("2-4", "6-8", False),
    ("2-3", "4-5", False),
    ("5-7", "7-9", True),
    ("2-8", "3-7", True),
    ("6-6", "4-6", True)
]


@pytest.mark.parametrize("work_order1,work_order2,expected", testdata)
def test_return_correct_score(work_order1, work_order2, expected):

    assert WorkOrder(work_order1).check_if_another_work_order_contains_overlapping_work(WorkOrder(work_order2)) == expected
