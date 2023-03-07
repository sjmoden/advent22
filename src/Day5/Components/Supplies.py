class Supplies:
    def __init__(self, container_initial_state):
        self.container_state = container_initial_state

    def rearrange_stack(self, number_to_move, starting_position, target_position):
        for _ in range(0, number_to_move):
            item_to_move = self.container_state[starting_position].pop()
            self.container_state[target_position].append(item_to_move)

    def output_top_of_stack_code(self):
        output = ""
        for stack in self.container_state:
            output += stack[-1]
        return output
