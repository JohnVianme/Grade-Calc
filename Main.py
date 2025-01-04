from weighted_assignment import weighted_assignment


def calc_weighted_grade(list_of_weighted_asms):
    score = 0
    for asm in list_of_weighted_asms:
        score = asm.calc_asm()
    return score


print("Hello World")
print("Test")
print("By World")
