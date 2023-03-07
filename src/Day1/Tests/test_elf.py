from Day1.Components.Elf import Elf


def test_returns_the_correct_sum():
    elf = Elf([123, 124, 124, 43, 54])
    assert elf.get_calorie_sum() == 468


def test_returns_zero_when_nothing_input():
    elf = Elf([])
    assert elf.get_calorie_sum() == 0


def test_returns_correct_calories():
    elf = Elf([123, 124, 124, 43, 54])
    assert elf.get_calories() == [123, 124, 124, 43, 54]
