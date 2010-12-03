
import random
import constants, syllables

#SYLLABARY = syllables.syllabary()
# generated one, easier for development, less waiting :)
MAX_SYLLABLES = 5
SYLLABARY ={'edc': {'score': 0.75, 'vowel': 'e'}, 'chuiqu': {'score': 0.91666666666666674, 'vowel': 'ui'}, 'dech': {'score': 0.91666666666666674, 'vowel': 'e'}, 'shou': {'score': 1.3333333333333335, 'vowel': 'ou'}, 'edd': {'score': 0.75, 'vowel': 'e'}, 'xel': {'score': 0.91666666666666674, 'vowel': 'e'}, 'heln': {'score': 0.33333333333333337, 'vowel': 'e'}, 'edm': {'score': 0.75, 'vowel': 'e'}, 'chxe': {'score': 0.75, 'vowel': 'e'}, 'shchui': {'score': 0.75, 'vowel': 'ui'}, 'chquequ': {'score': 0.33333333333333337, 'vowel': 'e'}, 'chtha': {'score': 0.75, 'vowel': 'a'}, 'ewqu': {'score': 0.75, 'vowel': 'e'}, 'edy': {'score': 0.75, 'vowel': 'e'}, 'xey': {'score': 0.91666666666666674, 'vowel': 'e'}, 'yew': {'score': 0.91666666666666674, 'vowel': 'e'}, 'oabs': {'score': 0.75, 'vowel': 'oa'}, 'oukm': {'score': 0.75, 'vowel': 'ou'}, 'shoud': {'score': 0.91666666666666674, 'vowel': 'ou'}, 'doom': {'score': 0.91666666666666674, 'vowel': 'oo'}, 'hal': {'score': 0.91666666666666674, 'vowel': 'a'}, 'qued': {'score': 0.91666666666666674, 'vowel': 'e'}, 'vep': {'score': 0.91666666666666674, 'vowel': 'e'}, 'shechv': {'score': 0.33333333333333337, 'vowel': 'e'}, 'shoun': {'score': 0.91666666666666674, 'vowel': 'ou'}, 'xme': {'score': 0.75, 'vowel': 'e'}, 'kuith': {'score': 0.91666666666666674, 'vowel': 'ui'}, 'wen': {'score': 0.91666666666666674, 'vowel': 'e'}, 'shdou': {'score': 0.75, 'vowel': 'ou'}, 'oucm': {'score': 0.75, 'vowel': 'ou'}, 'ved': {'score': 0.91666666666666674, 'vowel': 'e'}, 'veb': {'score': 0.91666666666666674, 'vowel': 'e'}, 'haqu': {'score': 0.91666666666666674, 'vowel': 'a'}, 'cui': {'score': 1.3333333333333335, 'vowel': 'ui'}, 'haw': {'score': 0.91666666666666674, 'vowel': 'a'}, 'rpea': {'score': 0.75, 'vowel': 'ea'}, 'moush': {'score': 0.91666666666666674, 'vowel': 'ou'}, 'ouchl': {'score': 0.75, 'vowel': 'ou'}, 'maky': {'score': 0.33333333333333337, 'vowel': 'a'}, 'ekqu': {'score': 0.75, 'vowel': 'e'}, 'bazh': {'score': 0.91666666666666674, 'vowel': 'a'}, 'gey': {'score': 0.91666666666666674, 'vowel': 'e'}, 'de': {'score': 1.3333333333333335, 'vowel': 'e'}, 'mashd': {'score': 0.33333333333333337, 'vowel': 'a'}, 'mou': {'score': 1.3333333333333335, 'vowel': 'ou'}, 'oumm': {'score': 0.75, 'vowel': 'ou'}, 'mooy': {'score': 0.91666666666666674, 'vowel': 'oo'}, 'mdou': {'score': 0.75, 'vowel': 'ou'}, 'moo': {'score': 1.3333333333333335, 'vowel': 'oo'}, 'zsha': {'score': 0.75, 'vowel': 'a'}, 'nou': {'score': 1.3333333333333335, 'vowel': 'ou'}, 'shezth': {'score': 0.33333333333333337, 'vowel': 'e'}, 'hik': {'score': 0.91666666666666674, 'vowel': 'i'}, 'uilr': {'score': 0.75, 'vowel': 'ui'}, 'nedng': {'score': 0.33333333333333337, 'vowel': 'e'}, 'daz': {'score': 0.91666666666666674, 'vowel': 'a'}, 'kma': {'score': 0.75, 'vowel': 'a'}, 'bboup': {'score': 0.33333333333333337, 'vowel': 'ou'}, 'gehzh': {'score': 0.33333333333333337, 'vowel': 'e'}, 'wse': {'score': 0.75, 'vowel': 'e'}, 'shizhk': {'score': 0.33333333333333337, 'vowel': 'i'}, 'vnge': {'score': 0.75, 'vowel': 'e'}, 'ngool': {'score': 0.91666666666666674, 'vowel': 'oo'}, 'ooyd': {'score': 0.75, 'vowel': 'oo'}, 'vda': {'score': 0.75, 'vowel': 'a'}, 'sha': {'score': 1.3333333333333335, 'vowel': 'a'}, 'oufch': {'score': 0.75, 'vowel': 'ou'}, 'oubm': {'score': 0.75, 'vowel': 'ou'}, 'ouqu': {'score': 1.3333333333333335, 'vowel': 'ou'}, 'kkej': {'score': 0.33333333333333337, 'vowel': 'e'}, 'emx': {'score': 0.75, 'vowel': 'e'}, 'ngmouk': {'score': 0.33333333333333337, 'vowel': 'ou'}, 'sew': {'score': 0.91666666666666674, 'vowel': 'e'}, 'sheg': {'score': 0.91666666666666674, 'vowel': 'e'}, 'shed': {'score': 0.91666666666666674, 'vowel': 'e'}, 'en': {'score': 1.3333333333333335, 'vowel': 'e'}, 'oun': {'score': 1.3333333333333335, 'vowel': 'ou'}, 'oum': {'score': 1.3333333333333335, 'vowel': 'ou'}, 'ouc': {'score': 1.3333333333333335, 'vowel': 'ou'}, 'ed': {'score': 1.3333333333333335, 'vowel': 'e'}, 'eaqub': {'score': 0.75, 'vowel': 'ea'}, 'cvech': {'score': 0.33333333333333337, 'vowel': 'e'}, 'oud': {'score': 1.3333333333333335, 'vowel': 'ou'}, 'avng': {'score': 0.75, 'vowel': 'a'}, 'ouz': {'score': 1.3333333333333335, 'vowel': 'ou'}, 'ngesh': {'score': 0.91666666666666674, 'vowel': 'e'}, 'doud': {'score': 0.91666666666666674, 'vowel': 'ou'}, 'nkou': {'score': 0.75, 'vowel': 'ou'}, 'dwou': {'score': 0.75, 'vowel': 'ou'}, 'ez': {'score': 1.3333333333333335, 'vowel': 'e'}, 'zcaqu': {'score': 0.33333333333333337, 'vowel': 'a'}, 'ew': {'score': 1.3333333333333335, 'vowel': 'e'}, 'goun': {'score': 0.91666666666666674, 'vowel': 'ou'}, 'ouw': {'score': 1.3333333333333335, 'vowel': 'ou'}, 'doum': {'score': 0.91666666666666674, 'vowel': 'ou'}, 'er': {'score': 1.3333333333333335, 'vowel': 'e'}, 'fouchth': {'score': 0.33333333333333337, 'vowel': 'ou'}, 'shloum': {'score': 0.33333333333333337, 'vowel': 'ou'}, 'coudm': {'score': 0.33333333333333337, 'vowel': 'ou'}, 'xde': {'score': 0.75, 'vowel': 'e'}, 'shkou': {'score': 0.75, 'vowel': 'ou'}, 'wouc': {'score': 0.91666666666666674, 'vowel': 'ou'}, 'xouxj': {'score': 0.33333333333333337, 'vowel': 'ou'}, 'wou': {'score': 1.3333333333333335, 'vowel': 'ou'}, 'xak': {'score': 0.91666666666666674, 'vowel': 'a'}, 'izhh': {'score': 0.75, 'vowel': 'i'}, 'zavzh': {'score': 0.33333333333333337, 'vowel': 'a'}, 'wouw': {'score': 0.91666666666666674, 'vowel': 'ou'}, 'dezqu': {'score': 0.33333333333333337, 'vowel': 'e'}, 'thque': {'score': 0.75, 'vowel': 'e'}, 'ped': {'score': 0.91666666666666674, 'vowel': 'e'}, 'oumr': {'score': 0.75, 'vowel': 'ou'}, 'zmac': {'score': 0.33333333333333337, 'vowel': 'a'}, 'pea': {'score': 1.3333333333333335, 'vowel': 'ea'}, 'esh': {'score': 1.3333333333333335, 'vowel': 'e'}, 'wyou': {'score': 0.75, 'vowel': 'ou'}, 'zoud': {'score': 0.91666666666666674, 'vowel': 'ou'}, 'oudc': {'score': 0.75, 'vowel': 'ou'}, 'mea': {'score': 1.3333333333333335, 'vowel': 'ea'}, 'dmad': {'score': 0.33333333333333337, 'vowel': 'a'}, 'koush': {'score': 0.91666666666666674, 'vowel': 'ou'}, 'wo': {'score': 1.3333333333333335, 'vowel': 'o'}, 'chuim': {'score': 0.91666666666666674, 'vowel': 'ui'}, 'nuir': {'score': 0.91666666666666674, 'vowel': 'ui'}, 'men': {'score': 0.91666666666666674, 'vowel': 'e'}, 'chuih': {'score': 0.91666666666666674, 'vowel': 'ui'}, 'qupea': {'score': 0.75, 'vowel': 'ea'}, 'uirz': {'score': 0.75, 'vowel': 'ui'}, 'ech': {'score': 1.3333333333333335, 'vowel': 'e'}, 'yque': {'score': 0.75, 'vowel': 'e'}, 'mew': {'score': 0.91666666666666674, 'vowel': 'e'}, 'add': {'score': 0.75, 'vowel': 'a'}, 'chuir': {'score': 0.91666666666666674, 'vowel': 'ui'}, 'oudw': {'score': 0.75, 'vowel': 'ou'}, 'uirm': {'score': 0.75, 'vowel': 'ui'}, 'edsh': {'score': 0.75, 'vowel': 'e'}, 'ash': {'score': 1.3333333333333335, 'vowel': 'a'}, 'yshou': {'score': 0.75, 'vowel': 'ou'}, 'shui': {'score': 1.3333333333333335, 'vowel': 'ui'}, 'oo': {'score': 0.75, 'vowel': 'oo'}, 'cou': {'score': 1.3333333333333335, 'vowel': 'ou'}, 'han': {'score': 0.91666666666666674, 'vowel': 'a'}, 'uishr': {'score': 0.75, 'vowel': 'ui'}, 'dsou': {'score': 0.75, 'vowel': 'ou'}, 'ach': {'score': 1.3333333333333335, 'vowel': 'a'}, 'xuy': {'score': 0.91666666666666674, 'vowel': 'u'}, 'voom': {'score': 0.91666666666666674, 'vowel': 'oo'}, 'yxi': {'score': 0.75, 'vowel': 'i'}, 'bouzb': {'score': 0.33333333333333337, 'vowel': 'ou'}, 'shew': {'score': 0.91666666666666674, 'vowel': 'e'}, 'ou': {'score': 0.75, 'vowel': 'ou'}, 'cva': {'score': 0.75, 'vowel': 'a'}, 'oush': {'score': 1.3333333333333335, 'vowel': 'ou'}, 'shoush': {'score': 0.91666666666666674, 'vowel': 'ou'}, 'ashs': {'score': 0.75, 'vowel': 'a'}, 'oufn': {'score': 0.75, 'vowel': 'ou'}, 'ougk': {'score': 0.75, 'vowel': 'ou'}, 'echd': {'score': 0.75, 'vowel': 'e'}, 'ochc': {'score': 0.75, 'vowel': 'o'}, 'dxou': {'score': 0.75, 'vowel': 'ou'}, 'zhquey': {'score': 0.33333333333333337, 'vowel': 'e'}, 'ca': {'score': 1.3333333333333335, 'vowel': 'a'}, 'echk': {'score': 0.75, 'vowel': 'e'}, 'youc': {'score': 0.91666666666666674, 'vowel': 'ou'}, 'ce': {'score': 1.3333333333333335, 'vowel': 'e'}, 'xe': {'score': 1.3333333333333335, 'vowel': 'e'}, 'echw': {'score': 0.75, 'vowel': 'e'}, 'yquea': {'score': 0.75, 'vowel': 'ea'}, 'vke': {'score': 0.75, 'vowel': 'e'}, 'ngoux': {'score': 0.91666666666666674, 'vowel': 'ou'}, 'xque': {'score': 0.75, 'vowel': 'e'}, 'youzj': {'score': 0.33333333333333337, 'vowel': 'ou'}, 'ouchz': {'score': 0.75, 'vowel': 'ou'}, 'xouzhqu': {'score': 0.33333333333333337, 'vowel': 'ou'}, 'nguic': {'score': 0.91666666666666674, 'vowel': 'ui'}, 'oucsh': {'score': 0.75, 'vowel': 'ou'}, 'zxe': {'score': 0.75, 'vowel': 'e'}, 'che': {'score': 1.3333333333333335, 'vowel': 'e'}, 'koo': {'score': 1.3333333333333335, 'vowel': 'oo'}, 'vam': {'score': 0.91666666666666674, 'vowel': 'a'}, 'tyik': {'score': 0.33333333333333337, 'vowel': 'i'}, 'equ': {'score': 1.3333333333333335, 'vowel': 'e'}, 'haz': {'score': 0.91666666666666674, 'vowel': 'a'}, 'uixd': {'score': 0.75, 'vowel': 'ui'}, 'cpea': {'score': 0.75, 'vowel': 'ea'}, 'vaz': {'score': 0.91666666666666674, 'vowel': 'a'}, 'pa': {'score': 1.3333333333333335, 'vowel': 'a'}, 'hea': {'score': 1.3333333333333335, 'vowel': 'ea'}, 'eyw': {'score': 0.75, 'vowel': 'e'}, 'var': {'score': 0.91666666666666674, 'vowel': 'a'}, 'rkou': {'score': 0.75, 'vowel': 'ou'}, 'kou': {'score': 1.3333333333333335, 'vowel': 'ou'}, 'qushouf': {'score': 0.33333333333333337, 'vowel': 'ou'}, 'mnge': {'score': 0.75, 'vowel': 'e'}, 'ersh': {'score': 0.75, 'vowel': 'e'}, 'a': {'score': 0.75, 'vowel': 'a'}, 'ebp': {'score': 0.75, 'vowel': 'e'}, 'oushm': {'score': 0.75, 'vowel': 'ou'}, 'dequl': {'score': 0.33333333333333337, 'vowel': 'e'}, 'oosw': {'score': 0.75, 'vowel': 'oo'}, 'chui': {'score': 1.3333333333333335, 'vowel': 'ui'}, 'foomn': {'score': 0.33333333333333337, 'vowel': 'oo'}, 'zcou': {'score': 0.75, 'vowel': 'ou'}, 'shouyp': {'score': 0.33333333333333337, 'vowel': 'ou'}, 'noush': {'score': 0.91666666666666674, 'vowel': 'ou'}, 'ha': {'score': 1.3333333333333335, 'vowel': 'a'}, 'ooy': {'score': 1.3333333333333335, 'vowel': 'oo'}, 'elb': {'score': 0.75, 'vowel': 'e'}, 'he': {'score': 1.3333333333333335, 'vowel': 'e'}, 'me': {'score': 1.3333333333333335, 'vowel': 'e'}, 'caz': {'score': 0.91666666666666674, 'vowel': 'a'}, 'cax': {'score': 0.91666666666666674, 'vowel': 'a'}, 'ma': {'score': 1.3333333333333335, 'vowel': 'a'}, 'thun': {'score': 0.91666666666666674, 'vowel': 'u'}, 'oumch': {'score': 0.75, 'vowel': 'ou'}, 'enqu': {'score': 0.75, 'vowel': 'e'}, 'shooy': {'score': 0.91666666666666674, 'vowel': 'oo'}, 'ui': {'score': 0.75, 'vowel': 'ui'}, 'chouc': {'score': 0.91666666666666674, 'vowel': 'ou'}, 'cam': {'score': 0.91666666666666674, 'vowel': 'a'}, 'looy': {'score': 0.91666666666666674, 'vowel': 'oo'}, 'poud': {'score': 0.91666666666666674, 'vowel': 'ou'}, 'moung': {'score': 0.91666666666666674, 'vowel': 'ou'}, 'azr': {'score': 0.75, 'vowel': 'a'}, 'choum': {'score': 0.91666666666666674, 'vowel': 'ou'}, 'cad': {'score': 0.91666666666666674, 'vowel': 'a'}, 'buit': {'score': 0.91666666666666674, 'vowel': 'ui'}, 'va': {'score': 1.3333333333333335, 'vowel': 'a'}, 'xouc': {'score': 0.91666666666666674, 'vowel': 'ou'}, 'oushr': {'score': 0.75, 'vowel': 'ou'}, 'muir': {'score': 0.91666666666666674, 'vowel': 'ui'}, 'am': {'score': 1.3333333333333335, 'vowel': 'a'}, 'shouc': {'score': 0.91666666666666674, 'vowel': 'ou'}, 'oumc': {'score': 0.75, 'vowel': 'ou'}, 'vou': {'score': 1.3333333333333335, 'vowel': 'ou'}, 'uir': {'score': 1.3333333333333335, 'vowel': 'ui'}, 'ddou': {'score': 0.75, 'vowel': 'ou'}, 'il': {'score': 1.3333333333333335, 'vowel': 'i'}, 'ouhc': {'score': 0.75, 'vowel': 'ou'}, 'uiy': {'score': 1.3333333333333335, 'vowel': 'ui'}, 'vwa': {'score': 0.75, 'vowel': 'a'}, 'xouz': {'score': 0.91666666666666674, 'vowel': 'ou'}, 'ooyy': {'score': 0.75, 'vowel': 'oo'}, 'ooyx': {'score': 0.75, 'vowel': 'oo'}, 'end': {'score': 0.75, 'vowel': 'e'}, 'mva': {'score': 0.75, 'vowel': 'a'}, 'pkou': {'score': 0.75, 'vowel': 'ou'}, 'enl': {'score': 0.75, 'vowel': 'e'}, 'ooshm': {'score': 0.75, 'vowel': 'oo'}, 'wca': {'score': 0.75, 'vowel': 'a'}, 'ewz': {'score': 0.75, 'vowel': 'e'}, 'shooshs': {'score': 0.33333333333333337, 'vowel': 'oo'}, 'oushch': {'score': 0.75, 'vowel': 'ou'}, 'deagf': {'score': 0.33333333333333337, 'vowel': 'ea'}, 'enz': {'score': 0.75, 'vowel': 'e'}, 'shsha': {'score': 0.75, 'vowel': 'a'}, 'rouc': {'score': 0.91666666666666674, 'vowel': 'ou'}, 'zhing': {'score': 0.91666666666666674, 'vowel': 'i'}, 'fnou': {'score': 0.75, 'vowel': 'ou'}, 'edqu': {'score': 0.75, 'vowel': 'e'}, 'vqua': {'score': 0.75, 'vowel': 'a'}, 'zxeah': {'score': 0.33333333333333337, 'vowel': 'ea'}, 'xshe': {'score': 0.75, 'vowel': 'e'}, 'chpea': {'score': 0.75, 'vowel': 'ea'}, 'mac': {'score': 0.91666666666666674, 'vowel': 'a'}, 'peam': {'score': 0.91666666666666674, 'vowel': 'ea'}, 'debt': {'score': 0.33333333333333337, 'vowel': 'e'}, 'sdel': {'score': 0.33333333333333337, 'vowel': 'e'}, 'bquez': {'score': 0.33333333333333337, 'vowel': 'e'}, 'mavzh': {'score': 0.33333333333333337, 'vowel': 'a'}, 'peac': {'score': 0.91666666666666674, 'vowel': 'ea'}, 'dshou': {'score': 0.75, 'vowel': 'ou'}, 'zdou': {'score': 0.75, 'vowel': 'ou'}, 'e': {'score': 0.75, 'vowel': 'e'}, 'doo': {'score': 1.3333333333333335, 'vowel': 'oo'}, 'ke': {'score': 1.3333333333333335, 'vowel': 'e'}, 'noum': {'score': 0.91666666666666674, 'vowel': 'ou'}, 'pdou': {'score': 0.75, 'vowel': 'ou'}, 'mshou': {'score': 0.75, 'vowel': 'ou'}, 'egv': {'score': 0.75, 'vowel': 'e'}, 'quoomb': {'score': 0.33333333333333337, 'vowel': 'oo'}, 'yuir': {'score': 0.91666666666666674, 'vowel': 'ui'}, 'woum': {'score': 0.91666666666666674, 'vowel': 'ou'}, 'ngeyk': {'score': 0.33333333333333337, 'vowel': 'e'}, 'u': {'score': 0.75, 'vowel': 'u'}, 'ngequ': {'score': 0.91666666666666674, 'vowel': 'e'}, 'xoudp': {'score': 0.33333333333333337, 'vowel': 'ou'}, 'shishng': {'score': 0.33333333333333337, 'vowel': 'i'}, 'mha': {'score': 0.75, 'vowel': 'a'}, 'deng': {'score': 0.91666666666666674, 'vowel': 'e'}, 'dou': {'score': 1.3333333333333335, 'vowel': 'ou'}}
MELODY = constants.MELODY
MELODY_RANKS = {'H': 2,
                'HH': 2,
                'HLHL': 2,
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
        return sum([SYLLABARY[s]['score'] for s in a])

    def shortnes():
        try:
            return 1-len(a)/float(MAX_SYLLABLES)
        except ZeroDivisionError:
            return 0

    def melody():
        def distance(a, b):
            if len(a)<len(b):
                r = xrange(len(a))
                d = (len(b)-len(a))*3
            else:
                r = xrange(len(b))
                d = (len(a)-len(b))*3
            enum = {'H': 2, 'M': 1, 'L': 0}
            return sum([abs(enum[a[i]]-enum[b[i]]) for i in r])
            
        print "".join(map(lambda s: MELODY[SYLLABARY[s]['vowel']], a))
        return 1

    return syllables()*shortnes()+melody()

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
    #print syllables.syllabary(meta=True)
    print words(debug=True)
