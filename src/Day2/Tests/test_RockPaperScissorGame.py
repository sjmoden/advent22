from Day2.Components.RockPaperScissorEnum import RockPaperScissor
from Day2.Components.RockPaperScissorGame import get_score
import pytest

testdata = [
    (RockPaperScissor.Rock, RockPaperScissor.Rock, 4),
    (RockPaperScissor.Rock, RockPaperScissor.Paper, 8),
    (RockPaperScissor.Rock, RockPaperScissor.Scissor, 3),
    (RockPaperScissor.Paper, RockPaperScissor.Rock, 1),
    (RockPaperScissor.Paper, RockPaperScissor.Paper, 5),
    (RockPaperScissor.Paper, RockPaperScissor.Scissor, 9),
    (RockPaperScissor.Scissor, RockPaperScissor.Rock, 7),
    (RockPaperScissor.Scissor, RockPaperScissor.Paper, 2),
    (RockPaperScissor.Scissor, RockPaperScissor.Scissor, 6)
]


@pytest.mark.parametrize("a,b,expected", testdata)
def test_return_correct_score(a, b, expected):
    result = get_score(a, b)
    assert result == expected
