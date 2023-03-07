from Day2.Components.WinLoseDrawEnum import WinLoseDraw


def test_x_returns_rock():
    assert WinLoseDraw.parse('X') == WinLoseDraw.Lose


def test_y_returns_paper():
    assert WinLoseDraw.parse('Y') == WinLoseDraw.Draw


def test_z_returns_scissor():
    assert WinLoseDraw.parse('Z') == WinLoseDraw.Win

