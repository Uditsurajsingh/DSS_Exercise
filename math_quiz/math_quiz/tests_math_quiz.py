import unittest
from math_quiz import random_integer, operator, calculator

class TestMathGame(unittest.TestCase):

    def test_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_operator(self):
        # TODO
        # Test if operators are correct
        result = operator()
        expected_operators = {'+', '-', '*'}
        self.assertIn(result, expected_operators)
        pass

    def test_calculator(self):
        #Testing the calculator method
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (3, 5, '-', '3 - 5', -2),
                (5, 5, '*', '3 * 5', 25),
            ]

            for test_case in test_cases:
                num1, num2, operator, expected_problem, expected_answer = test_case
                # TODO
                problem, answer = calculator(num1, num2, operator)
                #self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)
                pass

if __name__ == "__main__":
    unittest.main()
