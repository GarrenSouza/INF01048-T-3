import random

queensqty = 8

def evaluate(individual):

    attacks = 0

    for i in range(queensqty):
        for j in range(i+1, queensqty):
            if individual[i] == individual[j]:
                print('h')
                attacks += 1
            if individual[i] == individual[j] + (j - i):
                print('dd')
                attacks += 1
            if individual[i] == individual[j] - (j - i):
                print('d^')
                attacks += 1

    return attacks


def tournament(participants):
    min_attacks = 29
    best_p = None
    for p in participants:
        p_attacks = evaluate(p)
        if  p_attacks < min_attacks:
            min_attacks = p_attacks
            best_p = p
    return best_p


def crossover(parent1, parent2, index):
    return (parent1[:index]+parent2[index:],parent2[:index]+parent1[index:])


def mutate(individual, m):
    if(random.random() < m):
        individual[random.randint(0,7)] = random.randint(1,8)

    return individual


def get_random_individual():
    return [random.randint(1,8) for i in range(8)]


def selection(population, k):
    p1 = tournament(random.sample(population, k))
    v1 = population.index(p1)
    p2 = tournament(random.sample(population[:v1]+population[v1+1:], k))
    return (p1, p2)


def run_ga(g, n, k, m, e):
    population = [get_random_individual() for i in range(n)]

    for i in range(g):
        next_generation = [tournament(population)] if e else []
        while len(next_generation) < n:
            p1, p2 = selection(population, k)
            o1, o2 = crossover(p1,p2,random.randint(0,7))
            o1 = mutate(o1, m)
            o2 = mutate(o2, m)
            next_generation.extend([o1, o2])
        population = next_generation
    return tournament(population)

