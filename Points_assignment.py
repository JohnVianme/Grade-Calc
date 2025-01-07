"""
Class representing points_assignment object that has parameter name, points_earned, and points_total. This class can 
be used to create an assignment that is graded based off of a point system
"""



class points_assignment:
    def __init__(self, name, points_earned, points_total):
        self.name = name
        self.points_earned = points_earned
        self.points_total = points_total
    
    def get_name(self):
        return self.name
    
    def get_points_earned(self):
        return self.points_earned

    def get_points_total(self):
        return self.points_total
    
    def calc_grade(self):
        return (self.points_earned / self.points_total) * 100
    


asm2 = points_assignment("Final Exam", 140, 200)
'''
print(f"Name: {asm2.get_name()}")
print(f"Points earned: {asm2.get_points_earned()}")
print(f"Points total: {asm2.get_points_total()}")
print(f"Total grade: {asm2.calc_grade()}%")
'''





        


        