from collections import namedtuple
from Day2.Components.RockPaperScissorEnum import RockPaperScissor
from Day2.Components.WinLoseDrawEnum import WinLoseDraw


def parse_line(value):
    value_split = value.split(' ')

    play = namedtuple("Point", ["opponents_play", "your_play"])
    return play(RockPaperScissor.parse(value_split[0]), RockPaperScissor.parse(value_split[1]))


def parse_line2(value):
    value_split = value.split(' ')

    play = namedtuple("Point", ["opponents_play", "required_result"])
    return play(RockPaperScissor.parse(value_split[0]), WinLoseDraw.parse(value_split[1]))


def parse_your_move(opponents_play, required_result):
    if required_result == WinLoseDraw.Draw:
        return opponents_play

    if (opponents_play == RockPaperScissor.Rock and required_result == WinLoseDraw.Win)\
            or (opponents_play == RockPaperScissor.Scissor and required_result == WinLoseDraw.Lose):
        return RockPaperScissor.Paper
    if (opponents_play == RockPaperScissor.Rock and required_result == WinLoseDraw.Lose) \
            or (opponents_play == RockPaperScissor.Paper and required_result == WinLoseDraw.Win):
        return RockPaperScissor.Scissor
    if (opponents_play == RockPaperScissor.Paper and required_result == WinLoseDraw.Lose)\
            or (opponents_play == RockPaperScissor.Scissor and required_result == WinLoseDraw.Win):
        return RockPaperScissor.Rock
