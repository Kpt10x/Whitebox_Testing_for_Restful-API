import unittest
import sys
import os

# Add root to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from genetic_testing.genetic_test_gen import generate_test_case, fitness_function

class TestGeneticAlgorithm(unittest.TestCase):
    def test_generate_test_case(self):
        solution = [25.7, 40.9]
        test_case = generate_test_case(solution)
        self.assertEqual(set(test_case.keys()), {"name", "age"})

    def test_fitness_function_runs(self):
        # Try a dummy solution
        dummy_solution = [10, 30]
        score = fitness_function(None, dummy_solution, 0)
        self.assertIsInstance(score, float)

if __name__ == "__main__":
    unittest.main()
