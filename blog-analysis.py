
import feedparser, math
from BeautifulSoup import BeautifulSoup

import functools
import cPickle
def memoize(fctn):
        memory = {}
        @functools.wraps(fctn)
        def memo(*args,**kwargs):
                haxh = cPickle.dumps((args, sorted(kwargs.iteritems())))

                if haxh not in memory:
                        memory[haxh] = fctn(*args,**kwargs)

                return memory[haxh]
        if memo.__doc__:
            memo.__doc__ = "\n".join([memo.__doc__,"This function is memoized."])
        return memo

def cleanup(data):
    def cleaned(entry):
        entry.content[0].value = ''.join(BeautifulSoup(entry.content[0].value).findAll(text=True))
        return entry
    data.entries = map(cleaned, data.entries)
    return data

def word_length(entry):
    @memoize
    def average():
        return sum([len(w) for w in entry.content[0].value.split(" ")])\
                   /entry.content[0].value.count(" ")
    def deviation():
        return math.sqrt(sum([(len(w)-average())**2 for w in entry.content[0].value.split(" ")])\
                             /entry.content[0].value.count(" "))

    return (average(), deviation())



if __name__ == "__main__":
    data = feedparser.parse('/Users/Swizec/Desktop/ageekwithahat.wordpress.2011-09-25.xml')

    data = cleanup(data)

    print map(word_length, data.entries)
