
import random
import constants, syllables

#SYLLABARY = syllables.syllabary()
# generated one, easier for development, less waiting :)
MAX_SYLLABLES = 5
SYLLABARY = {'zhso': {'score': 0.75, 'vowel': 'o'}, 'zhja': {'score': 0.75, 'vowel': 'a'}, 'zhsu': {'score': 0.75, 'vowel': 'u'}, 'oa': {'score': 0.75, 'vowel': 'oa'}, 'wea': {'score': 1.3333333333333335, 'vowel': 'ea'}, 'le': {'score': 1.3333333333333335, 'vowel': 'e'}, 'shzhoa': {'score': 0.75, 'vowel': 'oa'}, 'la': {'score': 1.3333333333333335, 'vowel': 'a'}, 'shjoa': {'score': 0.75, 'vowel': 'oa'}, 'lo': {'score': 1.3333333333333335, 'vowel': 'o'}, 'yoah': {'score': 0.91666666666666674, 'vowel': 'oa'}, 'cla': {'score': 0.75, 'vowel': 'a'}, 'li': {'score': 1.3333333333333335, 'vowel': 'i'}, 'chpi': {'score': 0.75, 'vowel': 'i'}, 'ti': {'score': 1.3333333333333335, 'vowel': 'i'}, 'woazh': {'score': 0.91666666666666674, 'vowel': 'oa'}, 'ta': {'score': 1.3333333333333335, 'vowel': 'a'}, 'oapsh': {'score': 0.75, 'vowel': 'oa'}, 'ya': {'score': 1.3333333333333335, 'vowel': 'a'}, 'quwe': {'score': 0.75, 'vowel': 'e'}, 'chya': {'score': 0.75, 'vowel': 'a'}, 'ye': {'score': 1.3333333333333335, 'vowel': 'e'}, 'poash': {'score': 0.91666666666666674, 'vowel': 'oa'}, 'yu': {'score': 1.3333333333333335, 'vowel': 'u'}, 'shu': {'score': 1.3333333333333335, 'vowel': 'u'}, 'wso': {'score': 0.75, 'vowel': 'o'}, 'sha': {'score': 1.3333333333333335, 'vowel': 'a'}, 'pba': {'score': 0.75, 'vowel': 'a'}, 'she': {'score': 1.3333333333333335, 'vowel': 'e'}, 'shi': {'score': 1.3333333333333335, 'vowel': 'i'}, 'sho': {'score': 1.3333333333333335, 'vowel': 'o'}, 'shea': {'score': 1.3333333333333335, 'vowel': 'ea'}, 'oash': {'score': 1.3333333333333335, 'vowel': 'oa'}, 'jchi': {'score': 0.75, 'vowel': 'i'}, 'quoapc': {'score': 0.33333333333333337, 'vowel': 'oa'}, 'oashw': {'score': 0.75, 'vowel': 'oa'}, 'sea': {'score': 1.3333333333333335, 'vowel': 'ea'}, 'chea': {'score': 1.3333333333333335, 'vowel': 'ea'}, 'quoac': {'score': 0.91666666666666674, 'vowel': 'oa'}, 'oashy': {'score': 0.75, 'vowel': 'oa'}, 'qukou': {'score': 0.75, 'vowel': 'ou'}, 'chna': {'score': 0.75, 'vowel': 'a'}, 'wou': {'score': 1.3333333333333335, 'vowel': 'ou'}, 'cno': {'score': 0.75, 'vowel': 'o'}, 'woa': {'score': 1.3333333333333335, 'vowel': 'oa'}, 'pea': {'score': 1.3333333333333335, 'vowel': 'ea'}, 'sma': {'score': 0.75, 'vowel': 'a'}, 'we': {'score': 1.3333333333333335, 'vowel': 'e'}, 'quu': {'score': 1.3333333333333335, 'vowel': 'u'}, 'ba': {'score': 1.3333333333333335, 'vowel': 'a'}, 'wa': {'score': 1.3333333333333335, 'vowel': 'a'}, 'wo': {'score': 1.3333333333333335, 'vowel': 'o'}, 'yshoa': {'score': 0.75, 'vowel': 'oa'}, 'bo': {'score': 1.3333333333333335, 'vowel': 'o'}, 'wi': {'score': 1.3333333333333335, 'vowel': 'i'}, 'qua': {'score': 1.3333333333333335, 'vowel': 'a'}, 'bu': {'score': 1.3333333333333335, 'vowel': 'u'}, 'wu': {'score': 1.3333333333333335, 'vowel': 'u'}, 'jo': {'score': 1.3333333333333335, 'vowel': 'o'}, 'que': {'score': 1.3333333333333335, 'vowel': 'e'}, 'ji': {'score': 1.3333333333333335, 'vowel': 'i'}, 'shoaqu': {'score': 0.91666666666666674, 'vowel': 'oa'}, 'oashk': {'score': 0.75, 'vowel': 'oa'}, 'cpou': {'score': 0.75, 'vowel': 'ou'}, 'choa': {'score': 1.3333333333333335, 'vowel': 'oa'}, 'cou': {'score': 1.3333333333333335, 'vowel': 'ou'}, 'bou': {'score': 1.3333333333333335, 'vowel': 'ou'}, 'o': {'score': 0.75, 'vowel': 'o'}, 'coa': {'score': 1.3333333333333335, 'vowel': 'oa'}, 'chou': {'score': 1.3333333333333335, 'vowel': 'ou'}, 'yla': {'score': 0.75, 'vowel': 'a'}, 'yqua': {'score': 0.75, 'vowel': 'a'}, 'ou': {'score': 0.75, 'vowel': 'ou'}, 'chwe': {'score': 0.75, 'vowel': 'e'}, 'tu': {'score': 1.3333333333333335, 'vowel': 'u'}, 'co': {'score': 1.3333333333333335, 'vowel': 'o'}, 'ce': {'score': 1.3333333333333335, 'vowel': 'e'}, 'sou': {'score': 1.3333333333333335, 'vowel': 'ou'}, 'je': {'score': 1.3333333333333335, 'vowel': 'e'}, 'shoab': {'score': 0.91666666666666674, 'vowel': 'oa'}, 'shoac': {'score': 0.91666666666666674, 'vowel': 'oa'}, 'cu': {'score': 1.3333333333333335, 'vowel': 'u'}, 'zhno': {'score': 0.75, 'vowel': 'o'}, 'cha': {'score': 1.3333333333333335, 'vowel': 'a'}, 'che': {'score': 1.3333333333333335, 'vowel': 'e'}, 'pu': {'score': 1.3333333333333335, 'vowel': 'u'}, 'chla': {'score': 0.75, 'vowel': 'a'}, 'chi': {'score': 1.3333333333333335, 'vowel': 'i'}, 'wquu': {'score': 0.75, 'vowel': 'u'}, 'ybou': {'score': 0.75, 'vowel': 'ou'}, 'shsho': {'score': 0.75, 'vowel': 'o'}, 'pa': {'score': 1.3333333333333335, 'vowel': 'a'}, 'chu': {'score': 1.3333333333333335, 'vowel': 'u'}, 'pe': {'score': 1.3333333333333335, 'vowel': 'e'}, 'cwoa': {'score': 0.75, 'vowel': 'oa'}, 'pi': {'score': 1.3333333333333335, 'vowel': 'i'}, 'wqua': {'score': 0.75, 'vowel': 'a'}, 'woach': {'score': 0.91666666666666674, 'vowel': 'oa'}, 'cya': {'score': 0.75, 'vowel': 'a'}, 'quoaw': {'score': 0.91666666666666674, 'vowel': 'oa'}, 'wque': {'score': 0.75, 'vowel': 'e'}, 'me': {'score': 1.3333333333333335, 'vowel': 'e'}, 'wwe': {'score': 0.75, 'vowel': 'e'}, 'pqua': {'score': 0.75, 'vowel': 'a'}, 'jque': {'score': 0.75, 'vowel': 'e'}, 'zha': {'score': 1.3333333333333335, 'vowel': 'a'}, 'zhoav': {'score': 0.91666666666666674, 'vowel': 'oa'}, 'ui': {'score': 0.75, 'vowel': 'ui'}, 'chche': {'score': 0.75, 'vowel': 'e'}, 'zho': {'score': 1.3333333333333335, 'vowel': 'o'}, 'chqua': {'score': 0.75, 'vowel': 'a'}, 'pwea': {'score': 0.75, 'vowel': 'ea'}, 'zhui': {'score': 1.3333333333333335, 'vowel': 'ui'}, 'shzhe': {'score': 0.75, 'vowel': 'e'}, 'zhla': {'score': 0.75, 'vowel': 'a'}, 'quou': {'score': 1.3333333333333335, 'vowel': 'ou'}, 'no': {'score': 1.3333333333333335, 'vowel': 'o'}, 'na': {'score': 1.3333333333333335, 'vowel': 'a'}, 'yoa': {'score': 1.3333333333333335, 'vowel': 'oa'}, 'quoa': {'score': 1.3333333333333335, 'vowel': 'oa'}, 'u': {'score': 0.75, 'vowel': 'u'}, 'you': {'score': 1.3333333333333335, 'vowel': 'ou'}, 'nu': {'score': 1.3333333333333335, 'vowel': 'u'}, 'oay': {'score': 1.3333333333333335, 'vowel': 'oa'}, 'zhou': {'score': 1.3333333333333335, 'vowel': 'ou'}, 'wche': {'score': 0.75, 'vowel': 'e'}, 'zhcha': {'score': 0.75, 'vowel': 'a'}, 'shchu': {'score': 0.75, 'vowel': 'u'}, 'jche': {'score': 0.75, 'vowel': 'e'}, 'wsha': {'score': 0.75, 'vowel': 'a'}, 'zhchi': {'score': 0.75, 'vowel': 'i'}, 'a': {'score': 0.75, 'vowel': 'a'}, 'chsu': {'score': 0.75, 'vowel': 'u'}, 'e': {'score': 0.75, 'vowel': 'e'}, 'su': {'score': 1.3333333333333335, 'vowel': 'u'}, 'chse': {'score': 0.75, 'vowel': 'e'}, 'si': {'score': 1.3333333333333335, 'vowel': 'i'}, 'cshoa': {'score': 0.75, 'vowel': 'oa'}, 'so': {'score': 1.3333333333333335, 'vowel': 'o'}, 'quwu': {'score': 0.75, 'vowel': 'u'}, 'wya': {'score': 0.75, 'vowel': 'a'}, 'cce': {'score': 0.75, 'vowel': 'e'}, 'sa': {'score': 1.3333333333333335, 'vowel': 'a'}, 'se': {'score': 1.3333333333333335, 'vowel': 'e'}, 'quno': {'score': 0.75, 'vowel': 'o'}}
MELODY = constants.MELODY
MELODY_RANKS = {'H': 5,
                'L': 4,
                'HM': 2,
                'HLHL': 3,
                'M': 1,
                'LMH': 1,
                'HML': 1,
                'HLL': 1}
MUTATE_CHANCE = 0.2
BREED_CHANCE = 0.5
BREED_MAX_CHUNK = 3
SEED_SIZE = 100
MAX_POPULATION = 500
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

def fitness(a):
    def syllables():
        return reduce(lambda a,b: a*b, [SYLLABARY[s]['score'] for s in a])

    def shortnes():
        return 1-len(a)/float(MAX_SYLLABLES)

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

    if len(a) == 0:
        return 0
    
    return (shortnes()*2)*melody()*syllables()*phonology()

def compete(population):
    population.sort(key=lambda a: fitness(a),
                   reverse=True)
            
    return population

def cutoff(population):
    return filter(lambda a: fitness(a) > 0, population[:MAX_POPULATION])

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
