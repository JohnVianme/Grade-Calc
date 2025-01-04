from typing import List
from weighted_assignment import weighted_assignment

"""
This fuction takes a list of weighted_assignment objects and returns the grade from the 
the list of assignmets.
"""
def calc_weighted_grade(list_of_weighted_asms: List[weighted_assignment]):
    score = 0
    for asm in list_of_weighted_asms:
        score += asm.calc_asm()
    return score


print("Hello World")
print("Test")
print("By World")
