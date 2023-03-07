from Day5.Components.Supplies import Supplies


class Supplies9001(Supplies):
    def rearrange_stack(self, number_to_move, starting_position, target_position):
        items_to_move =[]
        for _ in range(0, number_to_move):
            item_to_move = self.container_state[starting_position].pop()
            items_to_move.append(item_to_move)
        items_to_move.reverse()
        for item_to_move in items_to_move:
            self.container_state[target_position].append(item_to_move)
