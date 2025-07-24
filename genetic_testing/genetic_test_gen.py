import pygad
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


API_URL = "http://localhost:5000/users"

def generate_test_case(solution):
    """Generate API request payload from solution"""
    return {"name": f"User{int(solution[0])}", "age": int(solution[1])}

def fitness_function(ga_instance, solution, solution_idx):
    """Evaluate the effectiveness of a test case"""
    test_payload = generate_test_case(solution)

    try:
        response = requests.post(API_URL, json=test_payload)
        if response.status_code == 201:
            return 1.0  # High fitness for successful user creation
        elif response.status_code == 400:
            return 0.5  # Medium fitness for invalid input
        else:
            return 0.2  # Low fitness for other failures
    except requests.exceptions.RequestException:
        return 0.0  # Very low fitness if request fails

ga_instance = pygad.GA(
    num_generations=50,
    num_parents_mating=5,
    fitness_func=fitness_function,
    sol_per_pop=10,
    num_genes=2,
    mutation_num_genes=1,
    mutation_type="random",
    mutation_by_replacement=True,
)

# Run Genetic Algorithm
logging.info("Starting Genetic Algorithm for API Test Case Generation...")
ga_instance.run()
logging.info("Genetic Algorithm execution completed.")

# ✅ Log the best test case
solution, solution_fitness, _ = ga_instance.best_solution()
logging.info(f"Best Test Case: {generate_test_case(solution)} with Fitness: {solution_fitness}")
