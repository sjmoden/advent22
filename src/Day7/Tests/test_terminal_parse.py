from Day7.Components.TerminalParse import parse_terminal


def test_terminal_parse_correctly_creates_directory():
    terminal_input = """$ cd /
$ ls
dir a
1 b.txt
10 c.dat
dir d
$ cd a
$ ls
dir e
100 f
1000 g
10000 h.lst
$ cd e
$ ls
100000 i
$ cd ..
$ cd ..
$ cd d
$ ls
1000000 j
10000000 d.log
100000000 d.ext
1000000000 k"""
    directory = parse_terminal(terminal_input.splitlines())
    assert directory.return_directory_size() == 1111111111
