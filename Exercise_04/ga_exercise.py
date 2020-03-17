'''
Genetic algorithm summerized:
    Start with random generated population of valid candidate individuals.
    For generation in (0...N):
        1.  select 2 individuals (parents) randomly from population for reprodution
            based on fitness of each individual. The fitter an individual, the more
            likely it is selected for reproduction.
        2.  Produce a new individual (child) by combining random parts of the 2 selected
            individuals (crossover).
        3.  Mutate a random number of new individuals to allow exploration other possible individuals.
        4.  Include the new individuals into the current population.
    Best solution is fittest of population individuals.

    Example:
        A trivial problem is to determine the greatest 3-bit binary number.
        Representation: An individual is represented by a string. The 3 bits could be
        represented by string such as: (0, 0, 1) etc.
        Initial population: Some random set of individuals, for example:
        [(1, 0, 0), (0, 1, 0), (0, 1, 0), (0, 0, 0)].
        Fitness function: Determines fitness of each individual; returns the integer
        value of the 3-bit number, 0 to 7.
        Selection: Individuals of each generation are randomly selected using a fitness
        ratio, their percentage contribution to the total fitness of the population.

        For the first generation:
        Genes       Fitness     Fitness ratio
        (1, 0, 0)   4           50 %
        (0, 1, 0)   2           25 %
        (0, 1, 0)   2           25 %
        (0, 0, 0)   0            0 %

        Total fitness is 4 + 2 + 2 + 0 = 8. (1, 0, 0) selected with 0.5, (0, 1, 0) with 0.25,
        (0, 1, 0) with 0.25 and (0, 0, 0) with 0.0 probability.

        Randomly selected pairs using fitness ratio:
        [(1, 0, 0), (0, 1, 0)], [(1, 0, 0), (1, 0, 0)], [(0, 1, 0), (0, 1, 0)], [(0, 1, 0), (1, 0, 0)]

        Reproduce: combine selected individual pairs at some random point using crossover. The first
        individual is copied up to the crossover point, then the second individual is copied from there.
            [(1, 0, 0), (0, 1, 0)] combined at bit 1 producing (1, 1, 0)
            [(1, 0, 0), (1, 0, 0)] combined at bit 0 producing (1, 0, 0)
            [(0, 1, 0), (0, 1, 0)] combined at bit 2 producing (0, 1, 0)
            [(0, 1, 0), (1, 0, 0)] combined at bit 1 producing (0, 0, 0)

        Note that the higher order bits contribute more to our definition of fitness; combining a high
        and low fitness individual could produce a lower fitness result.

        Stagnation: it is important that less fit individuals occasionally are selected, though all
        individuals are selected at rate proportional to their fitness. This helps ensure populations
        do not stagnate by constantly selecting from the same parent individuals. For example, if only
        the most fit individual, (1, 0, 0), were selected the optimal individual of (1, 1, 1) would
        never be found.

        Mutation: because the least significant bit is 0 throughout the population, no individual
        with least significant bit 1 can ever be produced using crossover alone. Change a random element
        in an individual representation at some specified probability. For example:
            (0, 1, 0) mutated to (0, 1, 1)

        New population: [(1, 1, 0), (1, 0, 0), (0, 1, 1), (0, 0, 0)] has total fitness
        of 6 + 4 + 3 + 0 = 13

        Genes       Fitness     Fitness ratio
        (1, 1, 0)   6           46 %
        (1, 0, 0)   4           31 %
        (0, 1, 1)   3           23 %
        (0, 0, 0)   0            0 %

        Terminate generation or fit enough: Terminate if individual fit enough or number ofo
        generations reached.

Exercise:
    Complete the following functions:
        fitness_function
        random_selection
        reproduce
        mutate
    Results (is compatible with any number of bits, not just 3):
        Generation 0:
        (1, 0, 0) - fitness: 4
        (0, 0, 0) - fitness: 0
        (0, 1, 0) - fitness: 2
        (0, 1, 1) - fitness: 3
        Generation 1:
        (1, 0, 0) - fitness: 4
        (0, 1, 0) - fitness: 2
        (0, 0, 0) - fitness: 0
        (0, 1, 1) - fitness: 3
        Generation 2:
        (1, 0, 0) - fitness: 4
        (1, 1, 0) - fitness: 6
        (0, 1, 0) - fitness: 2
        (0, 0, 0) - fitness: 0
        (0, 1, 1) - fitness: 3
        Generation 3:
        (1, 0, 0) - fitness: 4
        (1, 1, 0) - fitness: 6
        (0, 1, 0) - fitness: 2
        (0, 0, 0) - fitness: 0
        (0, 1, 1) - fitness: 3
        Generation 4:
        (1, 0, 0) - fitness: 4
        (1, 1, 0) - fitness: 6
        (0, 1, 0) - fitness: 2
        (0, 0, 0) - fitness: 0
        (0, 1, 1) - fitness: 3
        Generation 5:
        (1, 0, 0) - fitness: 4
        (1, 1, 0) - fitness: 6
        (0, 1, 0) - fitness: 2
        (0, 0, 0) - fitness: 0
        (0, 1, 1) - fitness: 3
        Generation 6:
        (1, 0, 0) - fitness: 4
        (1, 1, 0) - fitness: 6
        (0, 1, 0) - fitness: 2
        (0, 0, 0) - fitness: 0
        (0, 1, 1) - fitness: 3
        Final generation 6:
        (1, 1, 0) - fitness: 6
        (0, 1, 0) - fitness: 2
        (0, 0, 0) - fitness: 0
        (1, 0, 0) - fitness: 4
        (1, 1, 1) - fitness: 7
        (0, 1, 1) - fitness: 3
        Fittest Individual: (1, 1, 1) fitness: 7

'''


import random


p_mutation = 0.4
num_of_generations = 10


def genetic_algorithm(population, fitness_fn, minimal_fitness):
    for generation in range(num_of_generations):
        print("Generation {}:".format(generation))
        print_population(population, fitness_fn)

        new_population = set()

        for i in range(len(population)):
            mother, father = random_selection(population, fitness_fn)
            child = reproduce(mother, father)

            if random.uniform(0, 1) < p_mutation:
                child = mutate(child)

            new_population.add(child)

        # Add new population to population, use union to disregard
        # duplicate individuals
        population = population.union(new_population)

        fittest_individual = get_fittest_individual(population, fitness_fn)

        if minimal_fitness <= fitness_fn(fittest_individual):
            break

    print("Final generation {}:".format(generation))
    print_population(population, fitness_fn)

    return fittest_individual


def print_population(population, fitness_fn):
    for individual in population:
        fitness = fitness_fn(individual)
        print("{} - fitness: {}".format(individual, fitness))


def reproduce(mother, father):
    '''
    Reproduce two individuals with single-point crossover
    Return the child individual
    '''

    number = random.randint(0, len(father) - 1)
    child = [0] * len(father)
    for i in range(0, number):
        child[i] = mother[i]
    for i in range(number, 0):
        child[i] = father[i]

    return tuple(child)


def mutate(individual):
    '''
    Mutate an individual by randomly assigning one of its bits
    Return the mutated individual
    '''
    if len(individual) > 0:
        number = random.randint(0, len(individual) - 1)
        mutation = [0] * len(individual)

        for i in range(0, len(individual)):
            if i != number:
                mutation[i] = individual[i]
            else:
                mutation[i] = random.randint(0, 1)

        return tuple(mutation)


def random_selection(population, fitness_fn):
    """
    Compute fitness of each in population according to fitness_fn and add up
    the total. Then choose 2 from sequence based on percentage contribution to
    total fitness of population
    Return selected variable which holds two individuals that were chosen as
    the mother and the father
    """

    # Python sets are randomly ordered. Since we traverse the set twice, we
    # want to do it in the same order. So let's convert it temporarily to a
    # list.
    ordered_population = list(population)
    fitness_population = []
    stagnate_value = random.randint(0, 100)
    total_fitness = 0

    for individual in ordered_population:
        total_fitness += fitness_fn(individual)

    for individual in ordered_population:
        fitness_population.append(fitness_fn(individual))

    father_index = fitness_population.index(max(fitness_population))
    mother_index = 0

    fitness_population.remove(max(fitness_population))
    if stagnate_value > p_mutation * 100:
        mother_index = fitness_population.index(max(fitness_population))
    else:
        while mother_index != father_index:
            mother_index = random.randint(0, len(ordered_population))

    return ordered_population[mother_index], ordered_population[father_index]


def fitness_function(individual):
    '''
    Computes the decimal value of the individual
    Return the fitness level of the individual

    Explanation:
    enumerate(list) returns a list of pairs (position, element):

    enumerate((4, 6, 2, 8)) -> [(0, 4), (1, 6), (2, 2), (3, 8)]

    enumerate(reversed((1, 1, 0))) -> [(0, 0), (1, 1), (2, 1)]
    '''
    fitness = 0
    reversed_individuals = individual[::-1]
    for i in range(0, len(reversed_individuals)):
        fitness += (2 ** i) * reversed_individuals[i]
    return fitness


def get_fittest_individual(iterable, func):
    return max(iterable, key=func)


def get_initial_population(n, count):
    '''
    Randomly generate count individuals of length n
    Note since its a set it disregards duplicate elements.
    '''
    return set([
        tuple(random.randint(0, 1) for _ in range(n))
        for _ in range(count)
    ])


def main():
    minimal_fitness = 7

    # Curly brackets also creates a set, if there isn't a colon to indicate a dictionary
    initial_population = {
        (0, 1, 1),
        (0, 0, 0),
        (0, 1, 0),
        (1, 0, 0),
    }
    fittest = genetic_algorithm(initial_population, fitness_function, minimal_fitness)
    print('Fittest Individual: ' + str(fittest) + " fitness: " + str(fitness_function(fittest)))


if __name__ == '__main__':
    pass
    main()
