"""
Class representing a weighted_assignment object that has a name, weight, points earned and 
total points. This clas can be used to creat an assignment that has a weight.
"""


class weighted_assignment:
    def __init__(self, name, weight, points_earned, points_possible):
        self.name = name
        self.weight = weight
        self.points_earned = points_earned
        self.points_possible = points_possible

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

    def get_points_earned(self):
        return self.points_earned

    def get_points_possible(self):
        return self.points_possible

    def calc_asm(self):
        return self.points_earned / self.points_possible * self.weight

asm1 = weighted_assignment("HW 1", 10, 90, 100)
print(f"Name: {asm1.get_name()}")
print(f"Weight: {asm1.get_weight()}%")
print(f"Points Earned: {asm1.get_points_earned()}")
print(f"Points Possible: {asm1.get_points_possible()}")
print(f"Score: {asm1.calc_asm()}")