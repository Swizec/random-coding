
# refenced from http://www.zompist.com/kitlong.html#phono

CONSONANTS = {'articulation': ['labial', # lips (w), lips + teeth (f)
                               'dental', # teeth (th, French or Spanish t)
                               'alveolar', # behind the teeth (s, English t, Spanish r)
                               'palato-alveolar', # further back from the teeth (sh, American r)
                               'palatal', # top of palate (Russian ch)
                               'velar', # back of the mouth (k, ng)
                               'uvular', # way back in the mouth (Arabic q, French r)
                               'glottal' # back in the throat (h, glottal stop as in John Lennon saying bottle).
                               ],
              'closure': ['stop' # (stopping the airflow entirely: p t k)
                          'fricative', # (impeding it enough to cause audible friction: f s sh kh)
                          'approximant', # (barely impeding it: r l w y).
                          'affricate'  # is a stop plus a fricative, which must occur at the same place of articulation: t + sh = ch, d + zh = j.
                          ],
              'modifiers': ['voicing',
                            'nasalization',
                            'aspiration',
                            'palatilization'
                            ]
              }

VOWELS ={'height': ['high', 'mid', 'low'],
         'frontness': ['front', 'central', 'back'],
         'roundednes': [True, False],
         'length': ['long', 'short'],
         'nasalization': [True, False],
         'tenseness': [True, False]}

TONE = ['high', 'low']


# this is roughly the english alphabet
# definition goes like so:
# first letter V|C == vowel or consonant
# if V:
#  height-frontness-roundedness-tenseness
# if C:
#  closure-articulation
ENGLISH_ALPHABET = \
{'a': "V-lfsl",
 'b': "C-sl",
 'c': "C-sv",
 'ch': "C-afap",
 'd': "C-sa",
 'e': "V-mfsl",
 'ea': "V-hfst",
 'f': "C-fld",
 'g': "C-sv",
 'h': "C-fg",
 'i': "V-hfsl",
 'j': "C-afap",
 'k': "C-sv",
 'l': "C-aa",
 'm': "C-nl",
 'n': "C-na",
 'ng': "C-nv",
 'o': "V-lbrl",
 'ou': "V-lbrt",
 'oa': "V-mbrt",
 'oo': "V-hbrt",
 'p': "C-sl",
 'qu': "C-sg",
 'r': "C-aa",
 's': "C-fa",
 'sh': "C-fap",
 't': "C-sa",
 'th': "C-fd",
 'v': "C-fld",
 'u': "V-hbrl",
 'ui': "V-hfrl",
 'w': "C-al",
 'x': "C-",
 'y': "C-aa",
 'z': "C-fa",
 'zh': "C-fap",
 }

# by gut feeling I basically ranked consonants based on soft = high, hard = low

ENGLISH_PLEASANTNESS = \
{'': 0,
 'sl': 2,
 'sld': 0,
 'sd': 0,
 'sa': 0,
 'sap': 0,
 'sv': 1,
 'sg': 0,
 'fl': 0,
 'fld': 2,
 'fd': 2,
 'fa': 1,
 'fap': 2,
 'fv': 0,
 'fg': 0,
 'afl': 0,
 'afld': 0,
 'afd': 0,
 'afa': 0,
 'afap': 1,
 'afv': 0,
 'afg': 0,
 'al': 1,
 'ald': 0,
 'ad': 0,
 'aa': 2,
 'aap': 1,
 'av': 0,
 'ag': 0,
 'nl': 2,
 'nld': 0,
 'na': 1,
 'nap': 0,
 'nv': 0,
 'ng': 0,
# vowels - round and/or high is considered pretty, I think
 'hfrl': 0,
 'hfsl': 2,
 'hbrl': 1,
 'hbsl': 0,
 'hfrt': 0,
 'hfst': 0,
 'hbrt': 2,
 'hbst': 0,
 'mfrl': 0,
 'mfsl': 2,
 'mbrl': 0,
 'mbsl': 0,
 'mfrt': 0,
 'mfst': 1,
 'mbrt': 1,
 'mbst': 0,
 'lfrl': 2,
 'lfsl': 0,
 'lbrl': 1,
 'lbsl': 0,
 'lfrt': 0,
 'lfst': 0,
 'lbrt': 2,
 'lbst': 0,
}

MELODY = {
 'a': "L",
 'e': "M",
 'ea': "H",
 'i': "H",
 'o': "L",
 'ou': "L",
 'oa': "M",
 'oo': "H",
 'u': "H",
 'ui': "H"
}

# borrowed from english
# http://en.wikipedia.org/wiki/Sonority_hierarchy
SONORITY = {
    'p': 0,
    't': 0,
    'k': 0,
    'b': 1,
    'd': 1,
    'g': 1,
    's': 2,
    'f': 2,
    'th': 2,
    'z': 3,
    'v': 3,
    'm': 4,
    'n': 4,
    'l': 5,
    'r': 6,
    'ea': 6,
    'i': 7,
    'ui': 7,
    'u': 7,
    'e': 8,
    'ou': 8,
    'o': 8,
    'oo': 9,
    'a': 9
}
