import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance
from random import random

def calculate_cost(solution, distances):
    cost = 0
    num_cities = len(solution)
    for i in range(num_cities):
        cost += distances[solution[i], solution[(i + 1) % num_cities]]
    return cost

def swap_two_cities(solution):
    new_solution = solution.copy()
    i, j = np.random.choice(len(solution), size=2, replace=False)
    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
    return new_solution

def acceptance_probability(cost, new_cost, temperature):
    if new_cost < cost:
        return 1
    else:
        return np.exp((cost - new_cost) / temperature)

def simulated_annealing(distances):
    num_cities = len(distances)
    solution = np.arange(num_cities)
    cost = calculate_cost(solution, distances)
    
    for temperature in np.logspace(0, 5, num=500000)[::-1]:
        new_solution = swap_two_cities(solution)
        new_cost = calculate_cost(new_solution, distances)
        
        if acceptance_probability(cost, new_cost, temperature) > random():
            solution = new_solution
            cost = new_cost
            
    return solution, cost

cities = np.random.rand(50, 2)
distances = distance.cdist(cities, cities, 'euclidean')
best_solution, best_cost = simulated_annealing(distances)
print("Best solution:", best_solution)
print("Best cost:", best_cost)

