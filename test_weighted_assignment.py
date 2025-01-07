# Authors: 
from typing import List
import unittest
from weighted_assignment import weighted_assignment
import Main


class test_weighted_assignment(unittest.TestCase):
    def setUp(self):
        self.asm1 = weighted_assignment("HW 1", 10, 90, 100)
        self.asm2 = weighted_assignment("HW 2", 9, 80, 90)
        self.asm3 = weighted_assignment("HW 3", 8, 70, 80)
        self.asm4 = weighted_assignment("HW 4", 7, 60, 70)

        self.asms = []

        self.asms.append(self.asm1)
        self.asms.append(self.asm2)
        self.asms.append(self.asm3)
        self.asms.append(self.asm4)

        self.asm5 = weighted_assignment("HW 5", 10, 96.935, 100)
        self.asm6 = weighted_assignment("HW 6", 10, 57.79, 100)
        self.asm7 = weighted_assignment("HW 7", 10, 67.7777, 100)
        self.asm8 = weighted_assignment("HW 8", 10, 45.56, 100)

    def test_get_name(self):
        i = 1
        for asm in self.asms:
            self.assertEqual(asm.get_name(), "HW " + str(i))
            i += 1

    def test_weight(self):
        i = 0
        for asm in self.asms:
            self.assertEqual(asm.get_weight(), 10 - i)
            i += 1

    def test_earned(self):
        i = 0
        for asm in self.asms:
            self.assertEqual(asm.get_points_earned(), 90 - i)
            i += 10

    def test_total(self):
        i = 0
        for asm in self.asms:
            self.assertEqual(asm.get_points_possible(), 100 - i)
            i += 10

    def test_calc_asm(self):
        self.assertAlmostEqual(self.asm1.calc_asm(), (90 / 100) * 10, delta=1e-5)
        self.assertAlmostEqual(self.asm2.calc_asm(), (80 / 90) * 9, delta=1e-5)
        self.assertAlmostEqual(self.asm3.calc_asm(), (70 / 80) * 8, delta=1e-5)
        self.assertAlmostEqual(self.asm4.calc_asm(), (60 / 70) * 7, delta=1e-5)

    def test_calc_asm1(self):
        self.assertAlmostEqual(self.asm5.calc_asm(), (96.935 / 100) * 10, delta=1e-5)
        self.assertAlmostEqual(self.asm6.calc_asm(), (57.79 / 100) * 10, delta=1e-5)
        self.assertAlmostEqual(self.asm7.calc_asm(), (67.7777 / 100) * 10, delta=1e-5)
        self.assertAlmostEqual(self.asm8.calc_asm(), (45.56 / 100) * 10, delta=1e-5)

    def test_Main(self):
        expected = (90 / 100) * 10 + (80 / 90) * 9 + (70 / 80) * 8 + (60 / 70) * 7
        print(f"Expected: {expected}")
        print(f"Got: {Main.calc_weighted_grade(self.asms)}")
        self.assertAlmostEqual(
            Main.calc_weighted_grade(self.asms), expected, delta=1e-5
        )

if __name__ == "__main__":
    unittest.main()
