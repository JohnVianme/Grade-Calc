"""
Class representing a weighted_assignment object that has a name, weight, points earned and 
total points. This clas can be used to creat an assignment that has a weight.
"""


class weighted_assignment:
    def __init__(self, name, weight, points_earned, total_points):
        self.name = name
        self.weight = weight
        self.points_earned = points_earned
        self.total_points = total_points

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

    def get_points_earned(self):
        return self.points_earned

    def get_total_points(self):
        return self.total_points

    def calc_grade(self):
        pass

    def calc_asm(self):
        pass


asm1 = weighted_assignment("HW 1", 10, 90, 100)
print(f"Name: {asm1.get_name()}")
print(f"Weight: {asm1.get_weight()}%")
print(f"Earned Points: {asm1.get_points_earned()}")
print(f"Total Points: {asm1.get_total_points()}")
