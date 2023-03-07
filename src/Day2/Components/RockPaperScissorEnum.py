from enum import Enum


class RockPaperScissor(Enum):
    Rock = 1
    Paper = 2
    Scissor = 3

    @staticmethod
    def parse(value):
        match value:
            case "A":
                return RockPaperScissor.Rock
            case "B":
                return RockPaperScissor.Paper
            case "C":
                return RockPaperScissor.Scissor
            case "X":
                return RockPaperScissor.Rock
            case "Y":
                return RockPaperScissor.Paper
            case "Z":
                return RockPaperScissor.Scissor
