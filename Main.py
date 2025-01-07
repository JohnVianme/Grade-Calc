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
        score += asm.calc_weight_grade()
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


def add_assignment_points(list_of_asm: List, name, points_earned, points_total):  # Man
    asm = points_assignment(name, points_earned, points_total)
    list_of_asm.append(asm)
    print("Added Successfully")
    return True


def add_assignment_weighted(
    list_of_asm: List, name, weight, points_earned, points_total
):  # John
    an_asm = weighted_assignment(
        name, float(weight), float(points_earned), float(points_total)
    )
    list_of_asm.append(an_asm)
    return True


def remove_assignment(list_of_asm: List, name):  # Man
    for asm in list_of_asm:
        if asm.get_name() == name:
            list_of_asm.remove(asm)
            return True
    print("Assignment not found.")
    return False


def display_assignment(asm_type, list_of_asm: List):  # John
    print("############################################")
    for asm in list_of_asm:
        print("Name: " + str(asm.get_name()) + "\n")
        if asm_type.lower() == "w":
            print("Weight: " + str(asm.get_weight()) + "\n")
            print("Points Earned: " + str(asm.get_points_earned()) + "\n")
            print("Points Possible: " + str(asm.get_points_possible()) + "\n")
            print("Asm Grade: " + str(asm.calc_asm()) + "%")
            print("Asm Weight Grade: " + str(asm.calc_weight_grade()))
        else:
            print("Points Earned: " + str(asm.get_points_earned()) + "\n")
            print("Points Possible: " + str(asm.get_points_total()) + "\n")
            print("Grade: " + str(asm.calc_grade()))
        print("----------------------------")
    if asm_type.lower() == "w":
        print("{Final Grade Overall: " + str(calc_weighted_grade(list_of_asm)) + " }")
    else:
        print("{Final Grade Overall: " + str(calc_points_grade(list_of_asm)) + " }")

    print("############################################")


def overall_grade_assignment(list_of_asm: List, asm_type):  # Man
    if asm_type == "W":
        print(f"{calc_weighted_grade(list_of_asm): .2f}%")
        return True
    elif asm_type == "P":
        print(f"{calc_points_grade(list_of_asm): .2f}%")
        return True
    else:
        return False


def check_input(value, error_message):
    while True:
        try:
            value = float(value)
            return value

        except ValueError:
            value = input("Invalid input. " + error_message + "\n")


asm_type = input("Select type of Assignmet:\nW-Weighted\nP-Points\n").upper()
list_of_asm = []

while True:  # Checks if assignment type is valid
    if asm_type == "P":
        break
    elif asm_type == "W":
        break
    else:
        print("Invalid assignment type, try again")
        asm_type = input("Select type of Assignmet:\nW-Weighted\nP-Points\n").upper()


while True:
    command_ = input(
        "Enter Command:\nQ-Quit\nD-Display\nO-Overall Grade\nA-Add assignment\nR-Remove\n"
    ).upper()

    if command_ == "A":
        if asm_type == "W":
            name = input("Enter the Name: ")

            weight = check_input(
                input("Enter the Weight: "), "Please enter a valid weight"
            )
            points_earned = check_input(
                input("Enter the points earned: "),
                "Please enter a valid point that was earned",
            )
            points_total = check_input(
                input("Enter the points possible: "), "Please enter a valid total point"
            )

            add_assignment_weighted(
                list_of_asm, name, weight, points_earned, points_total
            )
        elif asm_type == "P":
            name = input("What is the name of the assignment: ")
            points_earned = check_input(
                input("What is the points earned in this assignment: "),
                "Please enter a valid point that was earned",
            )
            points_total = check_input(
                input("What is the total points for this assignment: "),
                "Please enter a valid total point",
            )
            add_assignment_points(list_of_asm, name, points_earned, points_total)

    elif command_ == "R":

        name = input("Write the name of the assignment that you would like to remove: ")
        is_remove = remove_assignment(list_of_asm, name)
        if is_remove == True:
            print("Removed successfully")
        elif is_remove == False:
            print("Incorrect name, try again")
        # print("Remove element")

    elif command_ == "D":
        display_assignment(asm_type, list_of_asm)

    elif command_ == "O":
        print("Calculating overall grade...")
        overall_grade_assignment(list_of_asm, asm_type)
        print("Overall Grade")
    elif command_ == "Q":
        print("Exiting...")
        exit()
    else:
        print("Unknown command, try again\n")
