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
        return self.points_earned / self.points_possible * 100
    
    def calc_weight_grade(self):
        return self.points_earned / self.points_possible * self.weight