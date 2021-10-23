import random
import string 
import math

class Individual:
    mutation_rate = 0.01

    def __init__(self, target):
        self.target = target
        self.target_length = len(self.target)
        self.characters = [random.choice(string.printable) for i in range(self.target_length)]
        self.fitness = self.calculate_fitness()

    def calculate_fitness(self) -> int:
        fitness = 0
        for self_char, target_char in zip(self.target, self.characters):
            if self_char == target_char:
                fitness += 1
        fitness /= self.target_length
        fitness **= 2
        return fitness

    def mate(self, partner) -> object:
        child = Individual(self.target)
        characters = []

        mid_point = random.randint(0, self.target_length-1)
        characters.extend(self.characters[:mid_point])
        characters.extend(partner.characters[mid_point:])

        child.characters = characters
        fitness = child.calculate_fitness()
        child.fitness = fitness
        return child

    def mutate(self):
        for i in range(self.target_length):
            mutation_probability = random.random()
            if (mutation_probability < self.mutation_rate):
                self.characters[i] = random.choice(string.printable)


def main():
    target = "To be or not to be."
    max_population = 1000
    generation = 1

    population = []
    for i in range(max_population):
        population.append(Individual(target))
    
    while True:
        population = sorted(population, key=lambda x: x.fitness, reverse=True)

        if population[0].fitness >= 1:
            break
        print(f"Generation: {generation}\tPhrase: {''.join(population[0].characters)}\tFitness: {population[0].fitness * 100:0.2f}%")
        
        new_generation = []

        # Select Parent
        mating_pool = []
        max_fitness = 0
        for i in range(max_population):
            if population[i].fitness > max_fitness:
                max_fitness = population[i].fitness
        
        for i in range(max_population):
            fitness = (1 - 0) * (population[i].fitness - 0) / (max_fitness - 0) + 0
            n = math.floor(fitness * 100)
            for i in range(n):
                mating_pool.append(population[i])

        # Mate Parents
        for i in range(max_population):
            parent_a = mating_pool[random.randint(0, len(mating_pool)-1)]
            parent_b = mating_pool[random.randint(0, len(mating_pool)-1)]
            child = parent_a.mate(parent_b)
            child.mutate()
            new_generation.append(child)

        population = new_generation
        
        generation += 1
    
    print(f"Generation: {generation}\tPhrase: {''.join(population[0].characters)}\tFitness: {population[0].fitness * 100}%")



if __name__ == "__main__":
    main()