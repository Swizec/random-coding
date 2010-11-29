
TARGET = """Critticall is a new kind of a software tool, dedicated to hard problems solving. From discovering new unknown algorithms, answering some unsettled math questions, to creating school schedules. Critticall harnesses the power of the evolution to search for cunning solutions nobody has thought about them before. 

Sounds like some hardcore science fiction, but it's rather the radical incoming reality. Just try the ArtificialSort, invented using this tool, and you will be no less than impressed. If you don't like to be shocked, it's time to leave the site now. For the rest, we are having some amazing fun here. 

Critticall is an evolution process simulator, dedicated for code segments improvement. Be it a C dialect known as the "strict C", or a specially designed language for the school schedule description. 

The user submits some pieces of a valid code, along with the fitness function, and the Critticall will exercise some evolution upon it, to get more and more fitter piece of code. That may mean a faster program segment, a shorter program sequence doing the same job, or a better schedule solution. 

It's a plenty of real examples here. Already mentioned ArtificialSort which you can try if you are a C++ programmer. Since seeing is the most straight way to believing, we recommend you to do so. You have been almost thought at school, something like this isn't possible. What is another reason to try. 

To be a sceptic is the sole rational attitude to this kind of talk, you are reading just now. On the other hand we want exactly the rational people to engage in this, so we have provided a working examples, you may try free of any charge, whatsoever. 

With the remaining percent of brave, skilled and smart ... let we go forward with this! 

On the left side links of this page you will see the muscles of the Critticall software. The stuff hard to believe before checking it. 

On the right side is a link to a very practical application - School Schedule. Many programs tries to match humans in the scheduling art and no one can. Critticall however surpasses them all. No wonder, when it's able to crack the left side problems, is it? Follow the link to ALGiT on the right! 
"""
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz,\n'.\"! "
MUTATE_CHANCE = 0.005
BREED_CHANCE = 0.2
BREED_MAX_CHUNK = 50
START_POPULATION = 150
MAX_POPULATION = 800
BREED_RANGE = (20, 60)
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

if __name__ == "__main__":
    population = seed(START_POPULATION, len(TARGET))

    min = distance(population[0], TARGET)
    max = distance(population[-1:][0], TARGET)

    print "gen:", 0, "min:", min, "max:", max, "populus:", len(population)
    
    for i in xrange(1, MAX_EPOCHS):
        population = epoch(population)

        min = distance(population[0], TARGET)
        max = distance(population[-1:][0], TARGET)

        print "gen:", i, "min:", min, "max:", max, "populus:", len(population)
        #print population[0:2], population[-2:]
            
        if there_yet(population):
            print i, population[0]
            break

    print "end of world!"
    #print population
