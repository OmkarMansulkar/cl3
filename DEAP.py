import random
from deap import base, creator, tools, algorithms

creator.create("FitMin", base.Fitness, weights=(-1.0,))
creator.create("Ind", list, fitness=creator.FitMin)

toolbox = base.Toolbox()
toolbox.register("attr", random.uniform, -10, 10)
toolbox.register("individual", tools.initRepeat, creator.Ind, toolbox.attr, 1)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", lambda ind: (ind[0]**2,))
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=2, indpb=1.0)
toolbox.register("select", tools.selTournament, tournsize=3)

pop = toolbox.population(n=10)
algorithms.eaSimple(pop, toolbox, 0.5, 0.2, 20, verbose=False)

best = tools.selBest(pop, 1)[0]
print("Best:", best[0], "Fitness:", best.fitness.values[0])
