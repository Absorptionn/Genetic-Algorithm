import string
import random
import time

class Phrase:

    def __init__(self, target, characters=None) -> None:
        self.target = target
        self.target_length = len(target)

        if characters == None:
            self.characters = [random.choice(string.printable) for i in range(self.target_length)]
        else:
            self.characters = characters
        self.fitness = self.calculate_fitness()

    def __str__(self) -> str:
        return self.phrase

    @property
    def phrase(self) -> str:
        return ''.join(self.characters)

    def calculate_fitness(self) -> int:
        fitness = 0
        for self_char, target_char in zip(self.phrase, self.target):
            if self_char == target_char:
                fitness += 1
        return fitness / self.target_length

    def crossover(self, partner) -> object:
        characters = []

        for self_char, parent_char in zip(self.phrase, partner.phrase):

            probability = random.random()

            if probability < 0.45:
                characters.append(self_char)
            elif probability < 0.90:
                characters.append(parent_char)
            else:
                characters.append(random.choice(string.printable))

        return Phrase(self.target, characters)


class Population:

    def __init__(self, target, max_population) -> None:
        self.target = target
        self.max_population = max_population
        self.population = [Phrase(self.target) for i in range(self.max_population)]
        self.generation = 1

    def target_found(self) -> bool:
        self.population = sorted(self.population, key=lambda x: x.fitness, reverse=True)
        if self.best.fitness >= 1:
            print(f"Generation: {self.generation} \tPhrase: {self.best.phrase} \tfitness: {self.best.fitness}")
            return True
        print(self.best.phrase)
        return False

    @property
    def best(self):
        return self.population[0]

    def new_generation(self):
        new_generation = []

        elites = (10 * self.max_population) // 100
        new_generation.extend(self.population[:elites])

        commons = (90 * self.max_population) // 100
        for i in range(commons):
            parent_a = random.choice(self.population[:50])
            parent_b = random.choice(self.population[:50])
            child = parent_a.crossover(parent_b)
            new_generation.append(child)
        
        self.population = new_generation
        self.generation += 1


def main():
    target = "To be or not to be."
    max_population = 1000
    population = Population(target, max_population)

    while True:
        if population.target_found():
            break

        population.new_generation()
        time.sleep(0.05)

if __name__ == "__main__":
    main()
