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


def calc_points_grade(list_of_points_asms: List[points_assignment]):
    score = 0
    tot_points_earned = 0
    tot_points_total = 0
    for asm in list_of_points_asms:
        tot_points_earned += asm.get_points_earned()
        tot_points_total += asm.get_points_total()

    score = (tot_points_earned / tot_points_total) * 100
    return score


def add_assignment_points(list_of_asm, name, points_earned, points_total):  # Man
    pass


def add_assignment_weighted(
    list_of_asm: List, name, weight, points_earned, points_total
):  # John
    an_asm = weighted_assignment(
        name, float(weight), float(points_earned), float(points_total)
    )
    list_of_asm.append(an_asm)
    return True


def remove_assignment(list_of_asm, name):  # Man
    pass


def display_assignment(asm_type, list_of_asm: List):  # John
    for asm in list_of_asm:
        print(asm.get_name())
        if asm_type == 'w':
            print(asm.get_weight())
            print(asm.get_points_earned())
            print(asm.points_possible())
            print(asm.calc_asm())
        else:
            print(asm.get_points_earned())
            print(asm.points_possible())
            print(asm.calc_asm())

def overall_grade_assignment(list_of_asm):  # Man
    pass


asm_type = input("W-Weighted\nP-Points\n")
list_of_asm = []

while True:
    command_ = input("Q-Quit\nD-Display\nO-Overall Grade\nA-Add assignment\nR-Remove\n")

    if command_ == "A":
        if asm_type == "W":
            name = input("Enter the Name: ")
            weight = input("Enter the Weight: ")
            points_earned = input("Enter the points earned: ")
            points_total = input("Enter the points out of: ")
            add_assignment_weighted(
                list_of_asm, name, weight, points_earned, points_total
            )
        elif asm_type == "P":
            add_assignment_points(list_of_asm)

        print("Add element")
    elif command_ == "R":
        print("Remove element")

    elif command_ == "D":
        print("Display")

    elif command_ == "O":
        print("Overall Grade")
    elif command_ == "Q":
        print("Exiting...")
        exit()
    else:
        command_ = input("Unknown command, try again\n")
