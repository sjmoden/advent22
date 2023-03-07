from Day5.Components.Supplies import Supplies


class Supplies9000(Supplies):
    def rearrange_stack(self, number_to_move, starting_position, target_position):
        for _ in range(0, number_to_move):
            item_to_move = self.container_state[starting_position].pop()
            self.container_state[target_position].append(item_to_move)
