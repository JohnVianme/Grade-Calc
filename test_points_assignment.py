from Points_assignment import points_assignment
import Main
import unittest

"""
asm1 = points_assignment("Homework", 120, 130)
asm2 = points_assignment("Exam1", 100, 200)
asm3 = points_assignment("Exam2", 170, 200)
asm4 = points_assignment("Final Project", 220, 250)

asm_list = [asm1, asm2, asm3,asm4]

grade_overall = Main.calc_points_grade(asm_list)

print(f"{grade_overall: .2f}%")
"""




class test_points_assignment(unittest.TestCase):

    def setUp(self):
        self.asm1 = points_assignment("Homework", 120, 600)

        self.asm2 = points_assignment("Homework", 100, 100)

    
        self.asm3 = points_assignment("Homework", 65, 130)
        self.asm4 = points_assignment("Exam1", 100, 200)
        self.asm5 = points_assignment("Exam2", 100, 200)
        self.asm6 = points_assignment("Final Project", 100, 250)

        self.list_test = [self.asm3,self.asm4,self.asm5,self.asm6]
        self.grade_overall = Main.calc_points_grade(self.list_test)
        
    
        
    
    def test_name(self):
        self.assertEqual(self.asm1.get_name(), "Homework")

    
    def test_points_earned(self):
        self.assertEqual(self.asm1.get_points_earned(), 120)

    def test_points_total(self):
        self.assertEqual(self.asm1.get_points_total(), 600)

    def test_calc_grade(self):
        self.assertEqual(self.asm1.calc_grade(), 20)

    
    def test_calc_grade_2(self):
        self.assertAlmostEqual(self.asm2.calc_grade(), 100, places = 2)

    def test_overall_grade(self):
        self.assertAlmostEqual(self.grade_overall, 46.79, places = 2)

    
    
    

        



if __name__ == '__main__':
    unittest.main()