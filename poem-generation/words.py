
import random
import constants, syllables

#SYLLABARY = syllables.syllabary()
# generated one, easier for development, less waiting :)
SYLLABARY = {'quchui': {'score': 0.75, 'vowel': 'ui'}, 'quzui': {'score': 0.75, 'vowel': 'ui'}, 'shou': {'score': 1.3333333333333335, 'vowel': 'ou'}, 'chgo': {'score': 0.75, 'vowel': 'o'}, 'shoa': {'score': 1.3333333333333335, 'vowel': 'oa'}, 'bva': {'score': 0.75, 'vowel': 'a'}, 'bou': {'score': 1.3333333333333335, 'vowel': 'ou'}, 'quba': {'score': 0.75, 'vowel': 'a'}, 'go': {'score': 1.3333333333333335, 'vowel': 'o'}, 'tzhui': {'score': 0.75, 'vowel': 'ui'}, 'tte': {'score': 0.75, 'vowel': 'e'}, 'jtou': {'score': 0.75, 'vowel': 'ou'}, 'zhchui': {'score': 0.75, 'vowel': 'ui'}, 'zme': {'score': 0.75, 'vowel': 'e'}, 'shzhou': {'score': 0.75, 'vowel': 'ou'}, 'bno': {'score': 0.75, 'vowel': 'o'}, 'chzui': {'score': 0.75, 'vowel': 'ui'}, 'te': {'score': 1.3333333333333335, 'vowel': 'e'}, 'shquu': {'score': 0.75, 'vowel': 'u'}, 'zhzui': {'score': 0.75, 'vowel': 'ui'}, 'ye': {'score': 1.3333333333333335, 'vowel': 'e'}, 'jte': {'score': 0.75, 'vowel': 'e'}, 'tba': {'score': 0.75, 'vowel': 'a'}, 'nou': {'score': 1.3333333333333335, 'vowel': 'ou'}, 'chquou': {'score': 0.75, 'vowel': 'ou'}, 'qube': {'score': 0.75, 'vowel': 'e'}, 'kzou': {'score': 0.75, 'vowel': 'ou'}, 'wbe': {'score': 0.75, 'vowel': 'e'}, 'she': {'score': 1.3333333333333335, 'vowel': 'e'}, 'wba': {'score': 0.75, 'vowel': 'a'}, 'quui': {'score': 1.3333333333333335, 'vowel': 'ui'}, 'sho': {'score': 1.3333333333333335, 'vowel': 'o'}, 'zhshe': {'score': 0.75, 'vowel': 'e'}, 'hzhe': {'score': 0.75, 'vowel': 'e'}, 'ze': {'score': 1.3333333333333335, 'vowel': 'e'}, 'za': {'score': 1.3333333333333335, 'vowel': 'a'}, 'zhzhe': {'score': 0.75, 'vowel': 'e'}, 'tsou': {'score': 0.75, 'vowel': 'ou'}, 'ksou': {'score': 0.75, 'vowel': 'ou'}, 'shto': {'score': 0.75, 'vowel': 'o'}, 'jou': {'score': 1.3333333333333335, 'vowel': 'ou'}, 'quchoar': {'score': 0.33333333333333337, 'vowel': 'oa'}, 'wgo': {'score': 0.75, 'vowel': 'o'}, 'zhtoa': {'score': 0.75, 'vowel': 'oa'}, 'chvo': {'score': 0.75, 'vowel': 'o'}, 'ququo': {'score': 0.75, 'vowel': 'o'}, 'gou': {'score': 1.3333333333333335, 'vowel': 'ou'}, 'ui': {'score': 0.75, 'vowel': 'ui'}, 'woa': {'score': 1.3333333333333335, 'vowel': 'oa'}, 'chve': {'score': 0.75, 'vowel': 'e'}, 'be': {'score': 1.3333333333333335, 'vowel': 'e'}, 'quu': {'score': 1.3333333333333335, 'vowel': 'u'}, 'ba': {'score': 1.3333333333333335, 'vowel': 'a'}, 'zhke': {'score': 0.75, 'vowel': 'e'}, 'hoakr': {'score': 0.33333333333333337, 'vowel': 'oa'}, 'quoah': {'score': 0.91666666666666674, 'vowel': 'oa'}, 'qua': {'score': 1.3333333333333335, 'vowel': 'a'}, 'tui': {'score': 1.3333333333333335, 'vowel': 'ui'}, 'quoat': {'score': 0.91666666666666674, 'vowel': 'oa'}, 'que': {'score': 1.3333333333333335, 'vowel': 'e'}, 'quoap': {'score': 0.91666666666666674, 'vowel': 'oa'}, 'je': {'score': 1.3333333333333335, 'vowel': 'e'}, 'chzhui': {'score': 0.75, 'vowel': 'ui'}, 'shno': {'score': 0.75, 'vowel': 'o'}, 'ja': {'score': 1.3333333333333335, 'vowel': 'a'}, 'quo': {'score': 1.3333333333333335, 'vowel': 'o'}, 'shui': {'score': 1.3333333333333335, 'vowel': 'ui'}, 'choa': {'score': 1.3333333333333335, 'vowel': 'oa'}, 'quse': {'score': 0.75, 'vowel': 'e'}, 'quoach': {'score': 0.91666666666666674, 'vowel': 'oa'}, 'oa': {'score': 0.75, 'vowel': 'oa'}, 'quzhe': {'score': 0.75, 'vowel': 'e'}, 'oatzh': {'score': 0.75, 'vowel': 'oa'}, 'chou': {'score': 1.3333333333333335, 'vowel': 'ou'}, 'zzui': {'score': 0.75, 'vowel': 'ui'}, 'wla': {'score': 0.75, 'vowel': 'a'}, 'zui': {'score': 1.3333333333333335, 'vowel': 'ui'}, 'ququu': {'score': 0.75, 'vowel': 'u'}, 'chzhou': {'score': 0.75, 'vowel': 'ou'}, 'bsa': {'score': 0.75, 'vowel': 'a'}, 'chsho': {'score': 0.75, 'vowel': 'o'}, 'shoal': {'score': 0.91666666666666674, 'vowel': 'oa'}, 'tou': {'score': 1.3333333333333335, 'vowel': 'ou'}, 'tgo': {'score': 0.75, 'vowel': 'o'}, 'tche': {'score': 0.75, 'vowel': 'e'}, 'zhno': {'score': 0.75, 'vowel': 'o'}, 'dna': {'score': 0.75, 'vowel': 'a'}, 'che': {'score': 1.3333333333333335, 'vowel': 'e'}, 'cho': {'score': 1.3333333333333335, 'vowel': 'o'}, 'chu': {'score': 1.3333333333333335, 'vowel': 'u'}, 'toa': {'score': 1.3333333333333335, 'vowel': 'oa'}, 'tchou': {'score': 0.75, 'vowel': 'ou'}, 'jui': {'score': 1.3333333333333335, 'vowel': 'ui'}, 'jshe': {'score': 0.75, 'vowel': 'e'}, 'wbui': {'score': 0.75, 'vowel': 'ui'}, 'chui': {'score': 1.3333333333333335, 'vowel': 'ui'}, 'bui': {'score': 1.3333333333333335, 'vowel': 'ui'}, 'wvo': {'score': 0.75, 'vowel': 'o'}, 'ychoa': {'score': 0.75, 'vowel': 'oa'}, 'oatt': {'score': 0.75, 'vowel': 'oa'}, 'zhu': {'score': 1.3333333333333335, 'vowel': 'u'}, 'shchou': {'score': 0.75, 'vowel': 'ou'}, 'zhoaqu': {'score': 0.91666666666666674, 'vowel': 'oa'}, 'tzhe': {'score': 0.75, 'vowel': 'e'}, 'zhoav': {'score': 0.91666666666666674, 'vowel': 'oa'}, 'shchoa': {'score': 0.75, 'vowel': 'oa'}, 'zhe': {'score': 1.3333333333333335, 'vowel': 'e'}, 'zhtui': {'score': 0.75, 'vowel': 'ui'}, 'tno': {'score': 0.75, 'vowel': 'o'}, 'quzhui': {'score': 0.75, 'vowel': 'ui'}, 'choah': {'score': 0.91666666666666674, 'vowel': 'oa'}, 'hoal': {'score': 0.91666666666666674, 'vowel': 'oa'}, 'choal': {'score': 0.91666666666666674, 'vowel': 'oa'}, 'choam': {'score': 0.91666666666666674, 'vowel': 'oa'}, 'chwui': {'score': 0.75, 'vowel': 'ui'}, 'woat': {'score': 0.91666666666666674, 'vowel': 'oa'}, 'woav': {'score': 0.91666666666666674, 'vowel': 'oa'}, 'choay': {'score': 0.91666666666666674, 'vowel': 'oa'}, 'o': {'score': 0.75, 'vowel': 'o'}, 'zhui': {'score': 1.3333333333333335, 'vowel': 'ui'}, 'choav': {'score': 0.91666666666666674, 'vowel': 'oa'}, 'choaw': {'score': 0.91666666666666674, 'vowel': 'oa'}, 'quou': {'score': 1.3333333333333335, 'vowel': 'ou'}, 'no': {'score': 1.3333333333333335, 'vowel': 'o'}, 'oal': {'score': 1.3333333333333335, 'vowel': 'oa'}, 'ne': {'score': 1.3333333333333335, 'vowel': 'e'}, 'quoa': {'score': 1.3333333333333335, 'vowel': 'oa'}, 'oat': {'score': 1.3333333333333335, 'vowel': 'oa'}, 'toaqu': {'score': 0.91666666666666674, 'vowel': 'oa'}, 'chbe': {'score': 0.75, 'vowel': 'e'}, 'zhou': {'score': 1.3333333333333335, 'vowel': 'ou'}, 'oatch': {'score': 0.75, 'vowel': 'oa'}, 'choach': {'score': 0.91666666666666674, 'vowel': 'oa'}, 'chsou': {'score': 0.75, 'vowel': 'ou'}, 'wno': {'score': 0.75, 'vowel': 'o'}, 'zhoa': {'score': 1.3333333333333335, 'vowel': 'oa'}, 'chje': {'score': 0.75, 'vowel': 'e'}, 'shsou': {'score': 0.75, 'vowel': 'ou'}, 'a': {'score': 0.75, 'vowel': 'a'}, 'tquu': {'score': 0.75, 'vowel': 'u'}, 'chpui': {'score': 0.75, 'vowel': 'ui'}, 'chtou': {'score': 0.75, 'vowel': 'ou'}, 'chse': {'score': 0.75, 'vowel': 'e'}, 'tchui': {'score': 0.75, 'vowel': 'ui'}, 'wchou': {'score': 0.75, 'vowel': 'ou'}, 'chchui': {'score': 0.75, 'vowel': 'ui'}, 'chtoa': {'score': 0.75, 'vowel': 'oa'}, 'tquo': {'score': 0.75, 'vowel': 'o'}, 'se': {'score': 1.3333333333333335, 'vowel': 'e'}}
MAX_SYLLABLES = 5
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
