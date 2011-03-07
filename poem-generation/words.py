
import random, pickle
import constants, syllables
from cmath import sqrt

#SYLLABARY = syllables.syllabary()
# generated one, easier for development, less waiting :)
SYLLABARY = pickle.load(open('syllabary.pickle', 'r'))
MELODY = constants.MELODY
MELODY_RANKS = {'H': 5,
                'L': 4,
                'HM': 2.5,
                'HLHL': 2,
                'M': 2,
                'LMH': 1,
                'HML': 1.5,
                'HLL': 1}
MUTATE_CHANCE = 0.2
BREED_CHANCE = 0.5
BREED_MAX_CHUNK = 2
SEED_SIZE = 100
MAX_POPULATION = 1500
BREED_RANGE = (20, 40)
MAX_EPOCHS = 500

def seed(n):
    words = []

    def word():
        return [random.choice(SYLLABARY.keys()) for i in xrange(random.randint(1, 10))]

    for i in xrange(n):
        words.append(word())

    return words

def breed(a, b):
    if random.random()-0.5 < BREED_CHANCE:
        r = random.random()
        s = random.randint(0, len(a))
        e = s+random.randint(1, BREED_MAX_CHUNK)

        def replace():
            return a[0:s]+b[s:e]+a[e:]
        def prepend():
            return b[s:e]+a
        def append():
            return a+b[s:e]
        def insert():
            m = random.randint(0, len(a))
            return a[0:m]+b[s:e]+a[m:]

        if r < 0.25:
            c = replace()
        elif r < 0.50:
            c = prepend()
        elif r < 0.75:
            c = append()
        else:
            c = insert()
        return c
    else:
        return mutate(b)

def mutate(a):
    r = random.random()
    if r < 0.3:
        return [random.choice(SYLLABARY.keys()) if abs(random.random()-0.5) < MUTATE_CHANCE else k \
                    for k in a]
    elif r < 0.6:
        return filter(lambda e: e!=None, [None if abs(random.random()-0.5) < MUTATE_CHANCE else k \
                                              for k in a])
    else:
        return a+[random.choice(SYLLABARY.keys())] if random.random()-0.5 < MUTATE_CHANCE else a

def fitness(a, longest):
    def syllables():
        return reduce(lambda a,b: a*b, [SYLLABARY[s]['score'] for s in a])

    def shortnes():
        return abs(1/(sqrt(len(a))*5))

    def melody():
        def delta(a, b):
            la = len(a)
            lb = len(b)
            return (xrange(la) if la<lb else xrange(lb),
                    abs(la-lb)*3)
        def distance(a, b):
            (r, d) = delta(a, b)
            enum = {'H': 2, 'M': 1, 'L': 0}
            return d+sum([abs(enum[a[i]]-enum[b[i]]) for i in r])
        def max_dist(b):
            (r, d) = delta(a, b)
            return float(d+len(r)*2)
            
        return sum([(1-distance(map(lambda s: MELODY[SYLLABARY[s]['vowel']], a),
                                rank)/max_dist(rank))*MELODY_RANKS[rank] \
                    for rank in MELODY_RANKS.keys()])
    def phonology():
        return 1

    def complexity():
        # find nucleus of word
        # len deltas from nucleus
        # compare to ideal deltas
        # scoar
        nucleus = a[len(a)/2]
        deltas = [abs(len(s)-len(nucleus)) for s in a]
        try:
            return 1.0/sum(deltas)
        except ZeroDivisionError:
            return 1

    def redundancy():
        map = {}
        for s in a:
            try:
                map[s] += 1
            except KeyError:
                map[s] = 1
        if sum(map.values()) > len(map.keys()):
            return 0
        return 1

    if len(a) == 0:
        return 0
    
    return shortnes()*melody()*syllables()*phonology()*redundancy()*complexity()

def longest(population):
    return len(reduce(lambda a,b: a if len(a) > len(b) else b,
                      population))

def compete(population):
    max_len = longest(population)
    print max_len
    
    population.sort(key=lambda a: fitness(a, max_len),
                   reverse=True)
            
    return population

def cutoff(population):
    max = longest(population)
    return filter(lambda a: fitness(a, max) > 0, population[:MAX_POPULATION])


def epoch(population):
    population = compete(map(mutate, population))
    for i in xrange(BREED_RANGE[0]):
        for j in xrange(BREED_RANGE[1]):
            if i!=j:
                try:
                    population.append(breed(population[i], population[j]))
                except IndexError:
                    pass

    uniques = {}
    for s in population:
        uniques["".join(s)] = s

    return cutoff(compete([uniques[k] for k in uniques.keys()]))

def words(debug=False):
    print "Generating words"

    population = seed(SEED_SIZE)

    for i in xrange(MAX_EPOCHS):
        if debug:
            print i, "".join(population[0]), ",", "".join(population[-1:][0])
        population = epoch(population)
    return ["".join(w) for w in population]
    #return [":".join(["".join(w), str(fitness(w))]) for w in population]

if __name__=="__main__":
    print words(debug=True)
