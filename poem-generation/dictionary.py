
import random
import constants

ALPHABET = constants.ENGLISH_ALPHABET
MUTATE_CHANCE = 0.05
BREED_CHANCE = 0.3
BREED_MAX_CHUNK = 3
SEED_SIZE = 10

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
    return [random.choice(ALPHABET.keys()) if abs(random.random()-0.5) < MUTATE_CHANCE else k for k in a]


if __name__ == "__main__":
    words = seed(SEED_SIZE)
    print words[0]
    print mutate(words[0])
    print breed(words[0], words[1])
