from Day2.Components.RockPaperScissorEnum import RockPaperScissor


def get_score_from_your_play(your_play):
    match your_play:
        case RockPaperScissor.Rock:
            return 1
        case RockPaperScissor.Paper:
            return 2
        case RockPaperScissor.Scissor:
            return 3


def get_score(opponents_play, your_play):
    your_play_score = get_score_from_your_play(your_play)

    if opponents_play == your_play:
        return your_play_score + 3

    if (opponents_play == RockPaperScissor.Rock and your_play == RockPaperScissor.Paper) \
            or (opponents_play == RockPaperScissor.Paper and your_play == RockPaperScissor.Scissor)\
            or (opponents_play == RockPaperScissor.Scissor and your_play == RockPaperScissor.Rock):
        return your_play_score + 6

    return your_play_score
