from typing import List
from weighted_assignment import weighted_assignment
from Points_assignment import points_assignment

"""
This fuction takes a list of weighted_assignment objects and returns the grade from the 
the list of assignmets.
"""
def calc_weighted_grade(list_of_weighted_asms: List[weighted_assignment]):
    score = 0
    for asm in list_of_weighted_asms:
        score += asm.calc_asm()
    return score

"""
This function takes a list of points_assignment object and 
returns the grade from the list of assignment
"""

def calc_points_grade (list_of_points_asms: List[points_assignment]):
    score = 0
    tot_points_earned = 0
    tot_points_total = 0
    for asm in list_of_points_asms:
        tot_points_earned += asm.get_points_earned()
        tot_points_total += asm.get_points_total()
    
    score = (tot_points_earned / tot_points_total) * 100
    return score


print("Hello World")
print("Test")
print("By World")
