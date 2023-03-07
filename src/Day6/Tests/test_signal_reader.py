import pytest
from Day6.Componets.SignalReader import SignalReader

testdata = [
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
    ("nppdvjthqldpwncqszvftbrmjlhg", 6),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11)
]


@pytest.mark.parametrize("stream_input,expected", testdata)
def test_return_correct_position(stream_input, expected):
    assert SignalReader(stream_input).get_starting_position() == expected


testdata_message_marker = [
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
    ("nppdvjthqldpwncqszvftbrmjlhg", 23),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26)
]


@pytest.mark.parametrize("stream_input,expected", testdata_message_marker)
def test_return_correct_position(stream_input, expected):
    assert SignalReader(stream_input).get_start_of_message_marker() == expected
