from Day5.Components.Supplies import Supplies


def test_top_of_stack_code_is_correct():
    supplies = Supplies([["a", "b"], ["c"], ["d"]])
    assert supplies.output_top_of_stack_code() == "bcd"
