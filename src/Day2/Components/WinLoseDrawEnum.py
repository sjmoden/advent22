from enum import Enum


class WinLoseDraw(Enum):
    Win = 1,
    Lose = 2,
    Draw = 3

    @staticmethod
    def parse(value):
        match value:
            case "X":
                return WinLoseDraw.Lose
            case "Y":
                return WinLoseDraw.Draw
            case "Z":
                return WinLoseDraw.Win
