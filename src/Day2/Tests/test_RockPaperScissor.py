from Day2.Components.RockPaperScissorEnum import RockPaperScissor


def test_x_returns_rock():
    assert RockPaperScissor.parse('X') == RockPaperScissor.Rock


def test_a_returns_rock():
    assert RockPaperScissor.parse('A') == RockPaperScissor.Rock


def test_y_returns_paper():
    assert RockPaperScissor.parse('Y') == RockPaperScissor.Paper


def test_b_returns_paper():
    assert RockPaperScissor.parse('B') == RockPaperScissor.Paper


def test_z_returns_scissor():
    assert RockPaperScissor.parse('Z') == RockPaperScissor.Scissor


def test_c_returns_scissor():
    assert RockPaperScissor.parse('C') == RockPaperScissor.Scissor
