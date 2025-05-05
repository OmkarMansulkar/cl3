import numpy as np
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score

from deap import base, creator, tools, algorithms

# 1. Define the Problem
# Simulate structure damage dataset
X, y = make_classification(n_samples=100, n_features=5, n_classes=2, random_state=42)
INDIVIDUAL_SIZE = 5  # Number of features (weights)
POPULATION_SIZE = 50
P_CROSSOVER = 0.5
P_MUTATION = 0.2
NGEN = 50
HALL_OF_FAME_SIZE = 1

# 2. Set up DEAP Components
# Create a Fitness class (maximizing accuracy)
creator.create("FitnessMax", base.Fitness, weights=(1.0,))

# Create an Individual class (list of floats representing weights)
creator.create("Individual", list, fitness=creator.FitnessMax)

# Create a Toolbox for individual and population generation
toolbox = base.Toolbox()

# Define how to create a single gene (random float)
toolbox.register("attr_float", np.random.randn)

# Define how to create an individual (list of random floats)
toolbox.register("individual", tools.initRepeat, creator.Individual,
                 toolbox.attr_float, n=INDIVIDUAL_SIZE)

# Define how to create a population (list of individuals)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# 3. Define the Evaluation Function
def classify(individual, x):
    weights = np.array(individual)
    return int(np.dot(x, weights) > 0)

def evaluate(individual):
    weights = np.array(individual)
    predictions = [classify(individual, x) for x in X]
    accuracy = accuracy_score(y, predictions)
    return (accuracy,)  # Return a tuple as required by DEAP

toolbox.register("evaluate", evaluate)

# 4. Define Genetic Operators
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=0.1, indpb=P_MUTATION)
toolbox.register("select", tools.selTournament, tournsize=3)

# 5. Run the Genetic Algorithm
if __name__ == "__main__":
    # Create an initial population
    population = toolbox.population(n=POPULATION_SIZE)

    # Keep track of the best individual found
    hof = tools.HallOfFame(HALL_OF_FAME_SIZE)

    # Create a statistics object to record the evolution
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("min", np.min)
    stats.register("max", np.max)

    # Perform the evolutionary loop
    for gen in range(NGEN):
        # Select the next generation individuals
        offspring = algorithms.varAnd(population, toolbox, cxpb=P_CROSSOVER, mutpb=P_MUTATION)

        # Evaluate the new population
        fitnesses = toolbox.map(toolbox.evaluate, offspring)
        for ind, fit in zip(offspring, fitnesses):
            ind.fitness.values = fit

        # Update the hall of fame with the best individuals
        hof.update(offspring)

        # Select the individuals for the next generation
        population[:] = toolbox.select(offspring, k=len(population))

        # Record statistics
        record = stats.compile(population)
        print(f"Generation {gen+1}: Avg={record['avg']:.4f}, Min={record['min']:.4f}, Max={record['max']:.4f}, Best in Gen={hof[0].fitness.values[0]:.4f}")

    # Print the best individual found
    print("\nBest Individual (Weights):", hof[0])
    print("Best Accuracy:", hof[0].fitness.values[0])