from Day5.Components.Supplies9001 import Supplies9001


def test_supplies_move_correctly():
    supplies = Supplies9001([["a", "b"], ["c"], ["d"]])
    supplies.rearrange_stack(2, 0, 1)
    assert len(supplies.container_state[0]) == 0
    assert len(supplies.container_state[1]) == 3
    assert len(supplies.container_state[2]) == 1
    assert supplies.container_state[1][0] == "c"
    assert supplies.container_state[1][1] == "a"
    assert supplies.container_state[1][2] == "b"
