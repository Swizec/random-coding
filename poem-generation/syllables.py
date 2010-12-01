
import random
import constants

ALPHABET = constants.ENGLISH_ALPHABET
MUTATE_CHANCE = 0.2
BREED_CHANCE = 0.5
BREED_MAX_CHUNK = 3
SEED_SIZE = 50
MAX_POPULATION = 500
BREED_RANGE = (10, 40)
SYLLABLE = {'max': {"C": 3, "V": 1},
            'min': {"C": 0, "V": 1}}
PLEASANT = constants.ENGLISH_PLEASANTNESS
MAX_EPOCHS = 100

def seed(n):
    words = []

    def word():
        return [random.choice(ALPHABET.keys()) for i in xrange(random.randint(1, 10))]

    for i in xrange(n):
        words.append(word())

    return words

def breed(a, b):
    if random.random()-0.5 < BREED_CHANCE:
        s = random.randint(0, len(a))
        e = s+random.randint(1, BREED_MAX_CHUNK)
        c =  a[0:s]+b[s:e]+a[e:]
        return c
    else:
        return mutate(b)

def mutate(a):
    return [random.choice(ALPHABET.keys()) if abs(random.random()-0.5) < MUTATE_CHANCE else k \
                for k in a]

def fitness(a):
    types = [ALPHABET[k].split('-')[0] for k in a]
    C = sum([1 if t=='C' else 0 for t in types])
    V = sum([1 if t=='V' else 0 for t in types])

    def out_of_bounds():
       return C < SYLLABLE['min']['C'] or V < SYLLABLE['min']['V'] or \
              C > SYLLABLE['max']['C'] or V > SYLLABLE['max']['V']

    if out_of_bounds():
        return 0

    def shortness():
        return (SYLLABLE['max']['C']+SYLLABLE['max']['V'])-len(a)

    def pleasantness():
        s = 0
        for k in a:
            try:
                k = PLEASANT[k.split('-')[1]]
            except IndexError:
                k = ''
            s += PLEASANT[k]
        return s

    def complexity():
        # essentally distance of consonants from vowels
        def distance(types):
            s = 0
            c = 0
            d = 1
            for t in types:
                if t == 'C':
                    c += d
                    d += 1
                elif t == 'V':
                    s += c
                    c = 0
                    d = 1
            return s+c
        def max_distance():
            return (len(types)-1)*4

        return max_distance()-(distance(types)+distance(reversed(types)))
                

    return shortness()+pleasantness()+complexity()
    
def compete(syllables):
    syllables.sort(key=lambda a: fitness(a),
                   reverse=True)
            
    return syllables

def cutoff(syllables):
    cut = MAX_POPULATION
    for i in reversed(xrange(0, len(syllables))):
        if fitness(syllables[i]) > 0:
            cut = min([len(syllables)-i, MAX_POPULATION])
            break
    return syllables[:cut]
    

def epoch(syllables):
    syllables = compete(map(mutate, syllables))
    for i in xrange(BREED_RANGE[0]):
        for j in xrange(BREED_RANGE[1]):
            if i!=j:
                syllables.append(breed(syllables[i], syllables[j]))

    uniques = {}
    for s in syllables:
        uniques["".join(s)] = s

    syllables = compete([uniques[k] for k in uniques.keys()])
    return cutoff(syllables)
    


if __name__ == "__main__":
    syllables = seed(SEED_SIZE)
    
    for i in xrange(MAX_EPOCHS):
        print "".join(syllables[0]), ",", "".join(syllables[-1:][0])
        syllables = epoch(syllables)

    print ["".join(a) for a in syllables]
