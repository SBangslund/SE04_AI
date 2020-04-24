'''
Homework:
    Modify your GA program given the following problem and code:
    Place n-queens on a chessboard in non-conflicting positions.

    Representation: A solution is represented by a list of integers, the rows
    of each queen. Each queen has its own column. (3, 4, 2, 6, 7, 8, 2) represents
    a queen in a3, one in b4, etc. Remember python list indices start from 0.

    Fitness function: Returns the integer value of the number of non-conflicting queen
    pairs; the maximum for n queens is n(n-1)/2.

    Fitness function (alternative): returns the integer value of the number of conflicting
    queen pairs. Minimize instead of maximizing.

    Selection: Roulette selection.

    Reproduce: Randomly select a crossover point to combine the two parents. Two new
    children are produced from the crossover. The effect is to maintain the fitness of each
    parent in the new population; keeping only one child occasionally losing fitness.


'''

import queens_fitness
import random

p_mutation = 0.2
num_of_generations = 75


def genetic_algorithm(population, fitness_fn, minimal_fitness):
    for generation in range(num_of_generations):
        print(generation)
        new_population = set()

        for i in range(len(population)):
            mother, father = random_selection(population, fitness_fn)
            child = reproduce(mother, father)

            if random.uniform(0, 1) < p_mutation:
                child = mutate(child)

            new_population.add(child)

        population = population.union(new_population)
        population = trim_population(population, fitness_fn)
        fittest_individual = get_fittest_individual(population, fitness_fn)

        if minimal_fitness <= fitness_fn(fittest_individual):
            break

    print("Final generation {}:".format(generation))
    print_population(population, fitness_fn)

    return fittest_individual


def trim_population(population, fitness_fn):
    new_population = set()
    for individual in population:
        if fitness_fn(individual) > -7:
            new_population.add(individual)
    return new_population


def print_population(population, fitness_fn):
    for individual in population:
        fitness = fitness_fn(individual)
        print("{} - fitness: {}".format(individual, fitness))


'''
Reproduce two individuals with single-point crossover
Return the child individual
'''


def reproduce(mother, father):
    number = random.randrange(1, len(father))
    child = [1] * len(father)
    for i in range(0, number + 1):
        child[i] = mother[i]
    for j in range(number, len(father)):
        child[j] = father[j]
    return tuple(child)


'''
Mutate an individual by randomly assigning one of its bits
Return the mutated individual
'''


def mutate(individual):
    if len(individual) > 0:
        number = random.randrange(len(individual))
        mutation = [1] * len(individual)

        for i in range(0, len(individual)):
            if i != number:
                mutation[i] = individual[i]
            else:
                mutation[i] = random.randrange(1, 9)

        return tuple(mutation)


"""
    Compute fitness of each in population according to fitness_fn and add up
    the total. Then choose 2 from sequence based on percentage contribution to
    total fitness of population
    Return selected variable which holds two individuals that were chosen as
    the mother and the father
"""


def random_selection(population, fitness_fn):
    ordered_population = list(population)
    fitness_population = []

    fitness_sum = 0

    for individual in ordered_population:
        fitness = fitness_fn(individual)
        fitness_sum += fitness
        fitness_population.append(fitness)

    selection = []

    for i in range(0, len(ordered_population)):
        probability = fitness_population[i] / fitness_sum
        if len(selection) >= 2:
            break
        if random.randint(0, 100) <= probability * 100 or random.randint(0, 100) > 80:
            selection.append(i)

    while len(selection) < 2:
        best = max(fitness_population)
        selection.append(fitness_population.index(best))
        fitness_population.remove(best)

    return ordered_population[0], ordered_population[1]


'''
Computes the decimal value of the individual
Return the fitness level of the individual
'''


def fitness_function(individual):
    fitness = 0
    reversed_individuals = individual[::-1]
    for i in range(0, len(reversed_individuals)):
        fitness += (2 ** i) * reversed_individuals[i]
    return fitness


def get_fittest_individual(iterable, func):
    return max(iterable, key=func)


def get_initial_population(n, count):
    return set([
        tuple(random.randint(0, 1) for _ in range(n))
        for _ in range(count)
    ])


def main():
    minimal_fitness = 0

    initial_population = {
        (1, 3, 7, 5, 2, 4, 6, 8),
        (5, 7, 3, 1, 8, 2, 4, 6)
    }
    fittest = genetic_algorithm(initial_population, queens_fitness.fitness_fn_negative, minimal_fitness)
    print('Fittest Individual: ' + str(fittest) + " fitness: " + str(queens_fitness.fitness_fn_negative(fittest)))


if __name__ == '__main__':
    pass
    main()
