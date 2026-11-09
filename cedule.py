import random
# Données du problème
capacites = [20, 15, 35, 40, 15, 15, 10]
demandes = [80, 90, 65, 70]

maintenance_possible = [
    ["1100", "0110", "0011"],          # unité 1
    ["1100", "0110", "0011"],          #  2
    ["1000", "0100", "0010", "0001"],  #  3
    ["1000", "0100", "0010", "0001"],  #  4
    ["1000", "0100", "0010", "0001"],  #  5
    ["1000", "0100", "0010", "0001"],  #  6
    ["1000", "0100", "0010", "0001"]   #  7
]

CAPACITE_TOTALE = sum(capacites)

# Création d'un chromosome


def creer_chromosome():
    chromosome = []

    for choix in maintenance_possible:
        chromosome.append(random.choice(choix))

    return chromosome

# Fonction objective (fitness)
def fitness(chromosome):

    reserves = []

    for intervalle in range(4):

        perte = 0

        for unite in range(len(chromosome)):
            if chromosome[unite][intervalle] == '1':
                perte += capacites[unite]

        reserve = CAPACITE_TOTALE - perte - demandes[intervalle]

        reserves.append(reserve)

    min_reserve = min(reserves)

    if min_reserve < 0:
        return 0

    return min_reserve

# Sélection par loterie

def selection_loterie(population):

    fitnesses = [fitness(ind) for ind in population]

    total = sum(fitnesses)

    if total == 0:
        return random.choice(population)

    r = random.uniform(0, total)

    cumul = 0

    for individu, fit in zip(population, fitnesses):

        cumul += fit

        if cumul >= r:
            return individu
# Croisement
def croisement(parent1, parent2):

    point = random.randint(1, len(parent1)-1)

    enfant1 = parent1[:point] + parent2[point:]
    enfant2 = parent2[:point] + parent1[point:]

    return enfant1, enfant2
# Mutation par inversion
def mutation_inversion(chromosome):

    mutant = chromosome.copy()

    gene = random.randint(0, len(mutant)-1)

    possibilites = maintenance_possible[gene]

    indice = possibilites.index(mutant[gene])

    nouvel_indice = (indice + 1) % len(possibilites)

    mutant[gene] = possibilites[nouvel_indice]

    return mutant

# AG principal

TAILLE_POPULATION = 50
GENERATIONS = 100
TAUX_CROISEMENT = 0.8
TAUX_MUTATION = 0.1

population = [creer_chromosome() for _ in range(TAILLE_POPULATION)]

for generation in range(GENERATIONS):

    nouvelle_population = []

    while len(nouvelle_population) < TAILLE_POPULATION:

        parent1 = selection_loterie(population)
        parent2 = selection_loterie(population)

        if random.random() < TAUX_CROISEMENT:
            enfant1, enfant2 = croisement(parent1, parent2)
        else:
            enfant1 = parent1.copy()
            enfant2 = parent2.copy()

        if random.random() < TAUX_MUTATION:
            enfant1 = mutation_inversion(enfant1)

        if random.random() < TAUX_MUTATION:
            enfant2 = mutation_inversion(enfant2)

        nouvelle_population.append(enfant1)

        if len(nouvelle_population) < TAILLE_POPULATION:
            nouvelle_population.append(enfant2)

    population = nouvelle_population
# Résultat final
meilleur = max(population, key=fitness)

print("===== Meilleure solution =====")

for i, gene in enumerate(meilleur):
    print(f"Unité {i+1} : {gene}")

print("\nFitness =", fitness(meilleur))

print("\nRéserves :")

for intervalle in range(4):

    perte = 0

    for unite in range(len(meilleur)):
        if meilleur[unite][intervalle] == '1':
            perte += capacites[unite]

    reserve = CAPACITE_TOTALE - perte - demandes[intervalle]

    print(f"Intervalle {intervalle+1} : {reserve} MW")
