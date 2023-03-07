import re


class SignalReader:
    def __init__(self, signal_input):
        self.signal_input = signal_input

    def generate_search_pattern(self, number_of_distinct, position):
        if position == number_of_distinct -1:
            return ""

        output = "(.)"
        for i in range(number_of_distinct - position - 1):
            output += "(?!"
            for dot_count in range(i):
                output += "."
            output += "\\"
            output += str(position + 1)
            output += r")"
        return output + self.generate_search_pattern(number_of_distinct, position+1)

    def get_starting_position(self):
        x = re.search(self.generate_search_pattern(4, 0), self.signal_input)
        return x.start() + 4

    def get_start_of_message_marker(self):
        x = re.search(self.generate_search_pattern(14, 0), self.signal_input)
        return x.start() + 14
