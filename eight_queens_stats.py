from eight_queens import *
import matplotlib.pyplot as plt
import numpy as np

g = 40   # number of generations
n = 30   # number of individuals
k = 15   # individuals in tournament
m = 0.5  # mutation chance
e = True # elitism

gs = np.arange(1, g+1, 1)
avg_fitness = []
min_fitness = []
max_fitness = []

def run_ga_plot(g, n, k, m, e):
    population = [get_random_individual() for i in range(n)]

    for _ in range(g):
        next_generation = [tournament(population)] if e else []
        while len(next_generation) < n:
            p1, p2 = selection(population, k)
            o1, o2 = crossover(p1,p2,random.randint(0,7))
            o1 = mutate(o1, m)
            o2 = mutate(o2, m)
            next_generation.extend([o1, o2])
        fs = [28 - evaluate(i) for i in next_generation]
        avg_fitness.append(np.average(fs))
        min_fitness.append(np.min(fs))
        max_fitness.append(np.max(fs))
        population = next_generation
    return tournament(population)

run_ga_plot(g,n,k,m,e)
plt.plot(gs, avg_fitness, 'r', gs, min_fitness, 'b', gs, max_fitness, 'g')
plt.show()