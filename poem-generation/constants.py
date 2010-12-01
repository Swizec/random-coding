
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
#  height-frontness-roundedness-length-nasalization-tenseness
# if C:
#  closure-articulation
ENGLISH_ALPHABET = \
{'a': "V-",
 'b': "C-sl",
 'c': "C-sv",
 'ch': "C-aap",
 'd': "C-sa",
 'e': "V-",
 'ea': "V-",
 'f': "C-fld",
 'g': "<v-sv",
 'h': "C-fg",
 'i': "V-",
 'j': "C-aap",
 'k': "C-sv",
 'l': "C-aa",
 'm': "C-nl",
 'n': "C-na",
 'ng': "C-nv",
 'o': "V-",
 'ou': "V-",
 'oa': "V-",
 'oo': "V-",
 'p': "C-sl",
 'q': "C-",
 'r': "C-aa",
 's': "C-fa",
 'sh': "C-fap",
 't': "C-sa",
 'th': "C-fd",
 'v': "C-fld",
 'u': "V-",
 'ui': "V-",
 'w': "C-al",
 'x': "C-",
 'y': "C-aa",
 'z': "C-fa",
 'zh': "C-fap",
 }
