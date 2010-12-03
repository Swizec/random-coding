
import random
import constants, syllables

#SYLLABARY = syllables.syllabary()
# generated one, easier for development, less waiting :)
SYLLABARY = ['gu', 'ouch', 'ge', 'gi', 'za', 'uich', 'ud', 'cha', 'che', 'ush', 'oog', 'ooc', 'ook', 'ooj', 'oot', 'ith', 'lu', 'zhea', 'noa', 'en', 'oun', 'ek', 'eg', 'oug', 'ec', 'oud', 'uch', 'ouy', 'ech', 'jea', 'ev', 'eag', 'ke', 'he', 'gea', 'ur', 'wou', 'woo', 'woa', 'wi', 'ji', 'ja', 'oang', 'uid', 'yi', 'vu', 'id', 'wea', 'pea', 'choa', 'choo', 'chou', 'chi', 'ed', 'eak', 'ead', 'un', 'zhe', 'ug', 'uc', 'uig', 'ak', 'uiv', 'ne', 'vush', 'shead', 'chen', 'vouy', 'ley', 'ruiv', 'dool', 'kuing', 'laz', 'nech', 'read', 'soob', 'dech', 'choosh', 'zhed', 'zhew', 'cez', 'luch', 'douy', 'doud', 'kuich', 'yus', 'hoov', 'yid', 'jeg', 'hug', 'nur', 'thuich', 'gead', 'chouy', 'kush', 'mif', 'kead', 'wush', 'jar', 'jan', 'wook', 'zhech', 'get', 'geh', 'gen', 'goup', 'yush', 'lup', 'luy', 'teng', 'zhezh', 'lug', 'yich', 'nouy', 'guiv', 'yar', 'neag', 'puig', 'yung', 'yooj', 'zhen', 'tung', 'choog', 'zhooj', 'chooj', 'noan', 'noak', 'couy', 'noay', 'noav', 'jush', 'nuich', 'dead', 'pel', 'wouv', 'wouy', 'wuich', 'cuich', 'zoac', 'youm', 'chur', 'kuiv', 'youy', 'koud', 'rush', 'neach', 'shiw', 'chech', 'nac', 'juiv', 'gech', 'nuiv', 'oodc', 'zhgea', 'chgea', 'vlu', 'dgea', 'ekn', 'ekk', 'ekg', 'ouly', 'uichsh', 'glu', 'uzy', 'ougs', 'uzs', 'gfoo', 'uivch', 'oakqu', 'enc', 'end', 'eng', 'enj', 'enr', 'nyi', 'ent', 'eny', 'ushw', 'ushy', 'egk', 'znu', 'ihy', 'oolz', 'clu', 'eakd', 'uichg', 'uichk', 'egch', 'kja', 'echk', 'echn', 'gchu', 'eadch', 'oojch', 'vchoo', 'gyi', 'nzu', 'chzu', 'chnoa', 'iwl', 'zhche', 'urg', 'urc', 'urn', 'tke', 'nlu', 'ugn', 'ugc', 'kwou', 'ushch', 'wgou', 'dyi', 'tgea', 'chroo', 'oujs', 'lvui', 'ench', 'ookch', 'ilk', 'tgu', 'ourd', 'ookzh', 'lge', 'ggea', 'ound', 'avn', 'ouyd', 'oochf', 'ouyn', 'ouyk', 'jquoo', 'jwou', 'oonj', 'zhwou', 'oong', 'zge', 'chwou', 'jzhe', 'uchsh', 'cgea', 'oukd', 'udsh', 'uikch', 'uzch', 'oogc', 'mhe', 'oogw', 'gja', 'ijw', 'outk', 'plu', 'ushk', 'ushl', 'ushn', 'gnoa', 'urk', 'kzea', 'iwth', 'oojg', 'cwou', 'uivg', 'oojk', 'oock', 'oocy', 'kgea', 'gzhe', 'dchoo', 'ichth', 'ooxk', 'a', 'i', 'oo', 'ou', 'e', 'u', 'jgib', 'nugh', 'chookk', 'deazv', 'fooquw', 'yubng', 'zeatng', 'zoogk', 'vlay', 'dchul', 'gagsh', 'zuwb', 'lgeal', 'neazhm', 'chithv', 'noaww', 'chuichp', 'tneab', 'neatc', 'chuym', 'zzuth', 'gewc', 'chguy', 'dzhech', 'ngchew', 'choogng', 'gyequ', 'koozm', 'gemg', 'chulng', 'thchook', 'neagg', 'gousm', 'gouchj', 'kegk', 'kithv', 'kgeax', 'noovzh', 'ounvc', 'ugchx', 'ehvj', 'oushzhj', 'ihkx', 'echvk', 'usshb', 'ekky', 'ouchdj', 'ougthv', 'invb', 'oovgm', 'ekhx', 'ewgsh', 'egthth', 'uzzp', 'ooghl', 'oudzf', 'epxm', 'oothbth', 'ookhb', 'ubvzh', 'eygg', 'oodzhb', 'ekrng', 'evtf', 'ouznb', 'egyb', 'oupdsh', 'czeachp', 'zhrihr', 'ndoongm', 'yshiwb', 'bthivs', 'nyazhqu', 'bsobb', 'zigsv', 'vikngz', 'ktnoch', 'luvpv', 'thutzk', 'kehsj', 'renwh', 'kegbqu', 'zeyrx', 'fuythr', 'shoonyh']
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
        return [random.choice(SYLLABARY) for i in xrange(random.randint(1, 10))]

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
        return [random.choice(SYLLABARY) if abs(random.random()-0.5) < MUTATE_CHANCE else k \
                    for k in a]
    elif r < 0.6:
        return filter(lambda e: e!=None, [None if abs(random.random()-0.5) < MUTATE_CHANCE else k \
                                              for k in a])
    else:
        return a+[random.choice(SYLLABARY)] if random.random()-0.5 < MUTATE_CHANCE else a

def fitness(a):
    return 1

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
                population.append(breed(population[i], population[j]))

    uniques = {}
    for s in population:
        uniques["".join(s)] = s

    return cutoff(compete([uniques[k] for k in uniques.keys()]))

def words(debug=True):
    print "Generating words"

    population = seed(SEED_SIZE)

    for i in xrange(MAX_EPOCHS):
        if debug:
            print "".join(population[0]), ",", "".join(population[-1:][0])
        population = epoch(population)
    return ["".join(a) for a in population]

if __name__=="__main__":
    print syllables.syllabary(scores=True)
#    print words()
