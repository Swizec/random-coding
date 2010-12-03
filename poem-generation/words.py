
import random
import constants, syllables

#SYLLABARY = syllables.syllabary()
# generated one, easier for development, less waiting :)
MAX_SYLLABLES = 4
SYLLABARY = {'rte': 0.75, 'quuis': 0.91666666666666674, 'yuich': 0.91666666666666674, 'xem': 0.91666666666666674, 'mthea': 0.75, 'roo': 1.3333333333333335, 'roa': 1.3333333333333335, 'pte': 0.75, 'shosx': 0.33333333333333337, 'tki': 0.75, 'shoa': 1.3333333333333335, 'xev': 0.91666666666666674, 'ngoo': 1.3333333333333335, 'dfuij': 0.33333333333333337, 'ltac': 0.33333333333333337, 'edx': 0.75, 'oozhng': 0.75, 'wcoo': 0.75, 'xey': 0.91666666666666674, 'mang': 0.91666666666666674, 'shoo': 1.3333333333333335, 'oukl': 0.75, 'tfeag': 0.33333333333333337, 'le': 1.3333333333333335, 'nga': 1.3333333333333335, 'la': 1.3333333333333335, 'lo': 1.3333333333333335, 'xoaquz': 0.33333333333333337, 'enzh': 0.75, 'koung': 0.91666666666666674, 'young': 0.91666666666666674, 'poac': 0.91666666666666674, 'rouml': 0.33333333333333337, 'jip': 0.91666666666666674, 'ti': 1.3333333333333335, 'buing': 0.91666666666666674, 'ngequb': 0.33333333333333337, 'te': 1.3333333333333335, 'rshoa': 0.75, 'oapzh': 0.75, 'ta': 1.3333333333333335, 'lra': 0.75, 'ixsh': 0.75, 'gep': 0.91666666666666674, 'tje': 0.75, 'zhang': 0.91666666666666674, 'yroo': 0.75, 'rwi': 0.75, 'shoash': 0.91666666666666674, 'ye': 1.3333333333333335, 'mou': 1.3333333333333335, 'dat': 0.91666666666666674, 'nozh': 0.91666666666666674, 'mekth': 0.33333333333333337, 'puing': 0.91666666666666674, 'lui': 1.3333333333333335, 'zhey': 0.91666666666666674, 'ma': 1.3333333333333335, 'moa': 1.3333333333333335, 'xaquk': 0.33333333333333337, 'shoong': 0.91666666666666674, 'zhudg': 0.33333333333333337, 'toosh': 0.91666666666666674, 'cheatj': 0.33333333333333337, 'yoosh': 0.91666666666666674, 'ngourg': 0.33333333333333337, 'shoozh': 0.91666666666666674, 'zhthea': 0.75, 'poazh': 0.91666666666666674, 'efd': 0.75, 'angm': 0.75, 'oafsh': 0.75, 'oahn': 0.75, 'oquz': 0.75, 'vda': 0.75, 'mtoan': 0.33333333333333337, 'oungng': 0.75, 'flor': 0.33333333333333337, 'shyo': 0.75, 'she': 1.3333333333333335, 'fedn': 0.33333333333333337, 'shi': 1.3333333333333335, 'rar': 0.91666666666666674, 'ycho': 0.75, 'roung': 0.91666666666666674, 'sho': 1.3333333333333335, 'mlo': 0.75, 'el': 1.3333333333333335, 'tel': 0.91666666666666674, 'erth': 0.75, 'ej': 1.3333333333333335, 'ngej': 0.91666666666666674, 'ze': 1.3333333333333335, 'oazhx': 0.75, 'ea': 0.75, 'muizhth': 0.33333333333333337, 'rra': 0.75, 'ery': 0.75, 'nger': 0.91666666666666674, 'tey': 0.91666666666666674, 'nguiysh': 0.33333333333333337, 'mef': 0.91666666666666674, 'ey': 1.3333333333333335, 'rmos': 0.33333333333333337, 'our': 1.3333333333333335, 'ter': 0.91666666666666674, 'ngey': 0.91666666666666674, 'wiqup': 0.33333333333333337, 'tlo': 0.75, 'er': 1.3333333333333335, 'xekn': 0.33333333333333337, 'uichf': 0.75, 'uizh': 1.3333333333333335, 'angf': 0.75, 'lezh': 0.91666666666666674, 'ejd': 0.75, 'theash': 0.91666666666666674, 'lak': 0.91666666666666674, 'uichj': 0.75, 'uich': 1.3333333333333335, 'zhicp': 0.33333333333333337, 'mud': 0.91666666666666674, 'koumy': 0.33333333333333337, 'toad': 0.91666666666666674, 'ra': 1.3333333333333335, 'ukqu': 0.75, 'thnga': 0.75, 'fti': 0.75, 'xoo': 1.3333333333333335, 'oump': 0.75, 'zhtoo': 0.75, 'kerk': 0.33333333333333337, 'ruj': 0.91666666666666674, 'xook': 0.91666666666666674, 'rui': 1.3333333333333335, 'pui': 1.3333333333333335, 'yshoa': 0.75, 'lej': 0.91666666666666674, 'bi': 1.3333333333333335, 'thxe': 0.75, 'ypoo': 0.75, 'wounsh': 0.33333333333333337, 'oazh': 1.3333333333333335, 'foa': 1.3333333333333335, 'mme': 0.75, 'je': 1.3333333333333335, 'pfij': 0.33333333333333337, 'joo': 1.3333333333333335, 'etr': 0.75, 'chthea': 0.75, 'om': 1.3333333333333335, 'ngoam': 0.91666666666666674, 'zip': 0.91666666666666674, 'uimth': 0.75, 'eyng': 0.75, 'oazhr': 0.75, 'ngoag': 0.91666666666666674, 'touj': 0.91666666666666674, 'xoumg': 0.33333333333333337, 'o': 0.75, 'jpui': 0.75, 'vxe': 0.75, 'tout': 0.91666666666666674, 'ngoax': 0.91666666666666674, 'ung': 1.3333333333333335, 'boa': 1.3333333333333335, 'ou': 0.75, 'tiqu': 0.91666666666666674, 'os': 1.3333333333333335, 'or': 1.3333333333333335, 'fe': 1.3333333333333335, 'chta': 0.75, 'rang': 0.91666666666666674, 'key': 0.91666666666666674, 'ngec': 0.91666666666666674, 'xyoo': 0.75, 'mer': 0.91666666666666674, 'ryoo': 0.75, 'xe': 1.3333333333333335, 'pon': 0.91666666666666674, 'plo': 0.75, 'thdea': 0.75, 'shoam': 0.91666666666666674, 'xzhoush': 0.33333333333333337, 'ngoaqu': 0.91666666666666674, 'redm': 0.33333333333333337, 'poa': 1.3333333333333335, 'dui': 1.3333333333333335, 'mmew': 0.33333333333333337, 'loa': 1.3333333333333335, 'vob': 0.91666666666666674, 'koo': 1.3333333333333335, 'tor': 0.91666666666666674, 'douw': 0.91666666666666674, 'eym': 0.75, 'loo': 1.3333333333333335, 'long': 0.91666666666666674, 'coojj': 0.33333333333333337, 'eyp': 0.75, 'shuif': 0.91666666666666674, 'eyr': 0.75, 'ruish': 0.91666666666666674, 'too': 1.3333333333333335, 'ed': 1.3333333333333335, 'shui': 1.3333333333333335, 'jngui': 0.75, 'ral': 0.91666666666666674, 'fey': 0.91666666666666674, 'oo': 0.75, 'ngthea': 0.75, 'erm': 0.75, 'raj': 0.91666666666666674, 'theal': 0.91666666666666674, 'dooz': 0.91666666666666674, 'ooh': 1.3333333333333335, 'thoonl': 0.33333333333333337, 'chui': 1.3333333333333335, 'chips': 0.33333333333333337, 'thuich': 0.91666666666666674, 'toot': 0.91666666666666674, 'bui': 1.3333333333333335, 'toor': 0.91666666666666674, 'ethz': 0.75, 'ytah': 0.33333333333333337, 'oajd': 0.75, 'oujng': 0.75, 'chlol': 0.33333333333333337, 'ynga': 0.75, 'ngoak': 0.91666666666666674, 'ert': 0.75, 'uy': 1.3333333333333335, 'shoor': 0.91666666666666674, 'oazhch': 0.75, 'klo': 0.75, 'shooy': 0.91666666666666674, 'rloqu': 0.33333333333333337, 'ur': 1.3333333333333335, 'oung': 1.3333333333333335, 'yeav': 0.91666666666666674, 'ui': 0.75, 'rfuiqu': 0.33333333333333337, 'yoong': 0.91666666666666674, 'uirch': 0.75, 'ud': 1.3333333333333335, 'ngui': 1.3333333333333335, 'lshoa': 0.75, 'ngoazh': 0.91666666666666674, 'dnguiy': 0.33333333333333337, 'ngat': 0.91666666666666674, 'ang': 1.3333333333333335, 'lpui': 0.75, 'ngap': 0.91666666666666674, 'xkoub': 0.33333333333333337, 'uik': 1.3333333333333335, 'uij': 1.3333333333333335, 'uim': 1.3333333333333335, 'chal': 0.91666666666666674, 'vo': 1.3333333333333335, 'xoup': 0.91666666666666674, 'xour': 0.91666666666666674, 'oazhj': 0.75, 'pouzht': 0.33333333333333337, 'tam': 0.91666666666666674, 'yoazh': 0.91666666666666674, 'ib': 1.3333333333333335, 'ngaj': 0.91666666666666674, 'oungch': 0.75, 'yoo': 1.3333333333333335, 'ujl': 0.75, 'vuic': 0.91666666666666674, 'puip': 0.91666666666666674, 'lchech': 0.33333333333333337, 'yoms': 0.33333333333333337, 'ldou': 0.75, 'oam': 1.3333333333333335, 'oak': 1.3333333333333335, 'kshoog': 0.33333333333333337, 'zhoul': 0.91666666666666674, 'mdo': 0.75, 'goax': 0.91666666666666674, 'puid': 0.91666666666666674, 'oat': 1.3333333333333335, 'jxe': 0.75, 'oangf': 0.75, 'ngang': 0.91666666666666674, 'twith': 0.33333333333333337, 'nguich': 0.91666666666666674, 'you': 1.3333333333333335, 'yos': 0.91666666666666674, 'ythea': 0.75, 'dshoox': 0.33333333333333337, 'xoocb': 0.33333333333333337, 'zhyoo': 0.75, 'dga': 0.75, 'xdoa': 0.75, 'angr': 0.75, 'uing': 1.3333333333333335, 'kis': 0.91666666666666674, 'tooj': 0.91666666666666674, 'luich': 0.91666666666666674, 'boo': 1.3333333333333335, 'klosh': 0.33333333333333337, 'zhshoa': 0.75, 'yooy': 0.91666666666666674, 'thea': 1.3333333333333335, 'choung': 0.91666666666666674, 'fi': 1.3333333333333335, 'lar': 0.91666666666666674, 'oungzh': 0.75, 'e': 0.75, 'shoung': 0.91666666666666674, 'ke': 1.3333333333333335, 'i': 0.75, 'thoa': 1.3333333333333335, 'oungp': 0.75, 'eangc': 0.75, 'chuikg': 0.33333333333333337, 'oungt': 0.75, 'xeay': 0.91666666666666674, 'tho': 1.3333333333333335, 'theang': 0.91666666666666674, 'u': 0.75, 'ytoo': 0.75, 'kxoa': 0.75, 'pngui': 0.75, 'yuid': 0.91666666666666674, 'loug': 0.91666666666666674, 'ngeyd': 0.33333333333333337, 'theams': 0.33333333333333337}
MUTATE_CHANCE = 0.2
BREED_CHANCE = 0.5
BREED_MAX_CHUNK = 3
SEED_SIZE = 100
MAX_POPULATION = 500
BREED_RANGE = (20, 40)
MAX_EPOCHS = 100

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
        return sum([SYLLABARY[s] for s in a])

    def shortnes():
        try:
            return 1-len(a)/float(MAX_SYLLABLES)
        except ZeroDivisionError:
            return 0

    return syllables()*shortnes()

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
            print "".join(population[0]), ",", "".join(population[-1:][0]), len(population)
        population = epoch(population)
    return ["".join(a) for a in population]

if __name__=="__main__":
#    print syllables.syllabary(scores=True)
    print words(debug=True)
