import pytest
from Day2.Components.RockPaperScissorEnum import RockPaperScissor
from Day2.Components.StategyParser import parse_line, parse_your_move
from Day2.Components.StategyParser import parse_line2
from Day2.Components.WinLoseDrawEnum import WinLoseDraw

testdata = [
    ("A Y", RockPaperScissor.Rock, RockPaperScissor.Paper),
    ("B X", RockPaperScissor.Paper, RockPaperScissor.Rock),
    ("C Z", RockPaperScissor.Scissor, RockPaperScissor.Scissor)
]


@pytest.mark.parametrize("value,expected_opponent_play,expected_your_play", testdata)
def test_return_correct_line_details(value, expected_opponent_play, expected_your_play):
    result = parse_line(value)
    assert result.opponents_play == expected_opponent_play
    assert result.your_play == expected_your_play


testdata2 = [
    ("A Y", RockPaperScissor.Rock, WinLoseDraw.Draw),
    ("B X", RockPaperScissor.Paper, WinLoseDraw.Lose),
    ("C Z", RockPaperScissor.Scissor, WinLoseDraw.Win)
]


@pytest.mark.parametrize("value,expected_opponent_play,expected_your_result", testdata2)
def test_return_correct_line_details2(value, expected_opponent_play, expected_your_result):
    result = parse_line2(value)
    assert result.opponents_play == expected_opponent_play
    assert result.required_result == expected_your_result


parse_your_move_data = [
    (RockPaperScissor.Rock, WinLoseDraw.Win, RockPaperScissor.Paper),
    (RockPaperScissor.Rock, WinLoseDraw.Lose, RockPaperScissor.Scissor),
    (RockPaperScissor.Rock, WinLoseDraw.Draw, RockPaperScissor.Rock),
    (RockPaperScissor.Paper, WinLoseDraw.Win, RockPaperScissor.Scissor),
    (RockPaperScissor.Paper, WinLoseDraw.Lose, RockPaperScissor.Rock),
    (RockPaperScissor.Paper, WinLoseDraw.Draw, RockPaperScissor.Paper),
    (RockPaperScissor.Scissor, WinLoseDraw.Win, RockPaperScissor.Rock),
    (RockPaperScissor.Scissor, WinLoseDraw.Lose, RockPaperScissor.Paper),
    (RockPaperScissor.Scissor, WinLoseDraw.Draw, RockPaperScissor.Scissor)
]


@pytest.mark.parametrize("opponent_play, required_result, expected_your_play", parse_your_move_data)
def test_return_correct_your_play(opponent_play, required_result, expected_your_play):
    result = parse_your_move(opponent_play, required_result)
    assert result == expected_your_play
