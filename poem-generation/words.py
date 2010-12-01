
import random
import constants, syllables

SYLLABARY = syllables.syllabary()
MUTATE_CHANCE = 0.2
BREED_CHANCE = 0.5
BREED_MAX_CHUNK = 3
SEED_SIZE = 100
MAX_POPULATION = 500
BREED_RANGE = (20, 40)
SYLLABLE = {'max': {"C": 4, "V": 1},
            'min': {"C": 0, "V": 1}}
MAX_DISTANCE = SYLLABLE['max']['C']*4 # side-effect of how distance is calculated
MAX_LENGTH = SYLLABLE['max']['C']+SYLLABLE['max']['V']

PLEASANT = constants.ENGLISH_PLEASANTNESS
MAX_EPOCHS = 500

def seed(n):
    words = []

    def word():
        return [random.choice(SYLLABARY) for i in xrange(random.randint(1, 10))]

    for i in xrange(n):
        words.append(word())

    return words

def words(debug=True):
    print "Generating words"

    bag = seed(SEED_SIZE)
    return bag

if __name__=="__main__":
    print words()
