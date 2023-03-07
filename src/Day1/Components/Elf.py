class Elf:
    def __init__(self, inputCalories):
        self.inputCalories = inputCalories

    def get_calories(self):
        return self.inputCalories;

    def get_calorie_sum(self):
        return sum(self.inputCalories)