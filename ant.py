import numpy as np
import random

# Generate coordinates for cities
num_cities = 10
coords = np.random.rand(num_cities, 2) * 100  # Random 2D positions of cities

# Distance matrix
dist_matrix = np.linalg.norm(coords[:, np.newaxis] - coords, axis=2)

# ACO parameters
num_ants = 20
num_iterations = 100
alpha = 1     # Influence of pheromone
beta = 5      # Influence of distance
evaporation = 0.5
Q = 100  # Total pheromone deposited

# Initialize pheromone matrix
pheromone = np.ones((num_cities, num_cities))

def route_length(route):
    return sum(dist_matrix[route[i % num_cities], route[(i + 1) % num_cities]] for i in range(num_cities))

def choose_next_city(current_city, visited, pheromone, dist):
    probabilities = []
    for j in range(num_cities):
        if j in visited:
            probabilities.append(0)
        else:
            tau = pheromone[current_city][j] ** alpha
            eta = (1.0 / dist[current_city][j]) ** beta
            probabilities.append(tau * eta)
    total = sum(probabilities)
    if total == 0:
        return random.choice([j for j in range(num_cities) if j not in visited])
    probabilities = [p / total for p in probabilities]
    return np.random.choice(range(num_cities), p=probabilities)

best_route = None
best_length = float('inf')

for iteration in range(num_iterations):
    all_routes = []
    all_lengths = []

    for _ in range(num_ants):
        route = []
        visited = set()
        current = random.randint(0, num_cities - 1)
        route.append(current)
        visited.add(current)

        while len(route) < num_cities:
            next_city = choose_next_city(current, visited, pheromone, dist_matrix)
            route.append(next_city)
            visited.add(next_city)
            current = next_city

        all_routes.append(route)
        length = route_length(route)
        all_lengths.append(length)

        if length < best_length:
            best_length = length
            best_route = route

    # Update pheromones
    pheromone *= (1 - evaporation)
    for route, length in zip(all_routes, all_lengths):
        for i in range(num_cities):
            a, b = route[i % num_cities], route[(i + 1) % num_cities]
            pheromone[a][b] += Q / length
            pheromone[b][a] += Q / length

print("Best route found:", best_route)
print("Best route length:", best_length)
