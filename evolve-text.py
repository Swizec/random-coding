
TARGET = """
Oft have we trod the vales of Castaly
And heard sweet notes of sylvan music blown
From antique reeds to common folk unknown:
And often launched our bark upon that sea
Which the nine Muses hold in empery,
And ploughed free furrows through the wave and foam,
Nor spread reluctant sail for more safe home
Till we had freighted well our argosy.

Of which despoiled treasures these remain,
Sordello's passion, and the honied line
Of young Endymion, lordly Tamburlaine
Driving his pampered jades, and more than these,
The seven-fold vision of the Florentine,
And grave-browed Milton's solemn harmonies.
"""
ALPHABET = ""    
MUTATE_CHANCE = 0.005
BREED_CHANCE = 0.3
BREED_MAX_CHUNK = len(TARGET)/4
START_POPULATION = 150
MAX_POPULATION = 1500
BREED_RANGE = (30, 70)
MAX_EPOCHS = 3000

import random

def seed(n, l):
    population = []
    
    def member():
        m = []
        for i in xrange(l):
            m.append(random.choice(ALPHABET))
        return "".join(m)
    
    for i in xrange(n):
        population.append(member())
    return population

def breed(a, b):
    if random.random()-0.5 < BREED_CHANCE:
        s = random.randint(0, len(a)-10)
        e = s+random.randint(1, BREED_MAX_CHUNK)
        c =  a[0:s]+b[s:e]+a[e:]
        return c
    else:
        return mutate(b)

def mutate(a):
    return "".join([random.choice(ALPHABET) if abs(random.random()-0.5) < MUTATE_CHANCE else k for k in a])

def distance(a, b):
    return sum([1 if a[i]!=b[i] else 0 for i in range(len(a))])

def compete(population):
    population.sort(key=lambda a: distance(a, TARGET))
    return population

def epoch(population):
    population = map(mutate, population)
    population = compete(population)
    for i in xrange(BREED_RANGE[0]):
        for j in xrange(BREED_RANGE[1]):
            if i!=j:
                population.append(breed(population[i], population[j]))
    population = compete(population)
    return population[:MAX_POPULATION]

def there_yet(population):
    for m in population:
        if distance(m, TARGET) == 0:
            return True
    return False

def construct_alphabet():
    fin = {}
    for c in TARGET:
        fin[c] = True
    return "".join(fin.keys())

if __name__ == "__main__":
    ALPHABET = construct_alphabet()
    population = seed(START_POPULATION, len(TARGET))

    print population[0]

    min = distance(population[0], TARGET)
    max = distance(population[-1:][0], TARGET)

    print "gen:", 0, "min:", min, "max:", max, "populus:", len(population)
    
    for i in xrange(1, MAX_EPOCHS):
        try:
            population = epoch(population)

            min = distance(population[0], TARGET)
            max = distance(population[-1:][0], TARGET)

            print "gen:", i, "min:", min, "max:", max, "populus:", len(population)
            
            if there_yet(population):
                print i, population[0]
                break
        except KeyboardInterrupt:
            print population[0]
            raise


    print "\nend of world!"
    #print population
