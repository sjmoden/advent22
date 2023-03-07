from Day3.Components.RucksackParser import parse_line, get_intersect_single, get_intersect, \
    parse_line_into_groups_of_three, get_intersect_from_group_of_three
import pytest


def test_compartments_are_parsed_correctly():
    result = parse_line("abcdef")
    assert result.compartment1 == "abc"
    assert result.compartment2 == "def"


def test_return_intersect_single_correctly():
    with pytest.raises(Exception) as e:
        get_intersect_single("gbhI", "IGkb")
        assert e.message == "Too many values"


def test_return_intersect_single_correctly():
    result = get_intersect_single("gbh", "Gkb")
    assert result == "b"


def test_return_intersect_single_correctly_with_multiple_identical_values():
    result = get_intersect_single("gbhb", "Gkbb")
    assert result == "b"


def test_return_intersect_correctly():
    result = get_intersect("gbhi", "Gkbi")
    assert result == ["b", "i"]


def test_return_correct_group_of_threes():
    values = ["1", "2", "3", "4", "5", "6"]
    parsed_result = parse_line_into_groups_of_three(values)
    assert len(parsed_result) == 2
    assert parsed_result[0] == ["1", "2", "3"]
    assert parsed_result[1] == ["4", "5", "6"]


def test_return_intersect_from_group_of_three():
    values = ["abcd", "defg", "dhigk"]
    parsed_result = get_intersect_from_group_of_three(values)
    assert parsed_result == "d"
