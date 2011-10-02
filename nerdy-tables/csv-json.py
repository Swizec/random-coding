
import csv, collections
from itertools import izip_longest, chain

def extract(data, start):
    def grouper(n, iterable, fillvalue=None):
        "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
        args = [iter(iterable)] * n
        return list(izip_longest(fillvalue=fillvalue, *args))
    def flatten(listOfLists):
        "Flatten one level of nesting"
        return chain.from_iterable(listOfLists)

    def days(row, combine=False):
        def clean(item):
            item = map(lambda x: int(x) if x != None and x != '' else 0,
                       list(item))
            return sum(item) if combine else item

        return list(flatten([map(clean, grouper(2, row[0:27])),
                             map(clean, grouper(3, row[28:123])),
                             map(clean, grouper(3, row[127:144]))]))

    return {'horny': [days(r[1:]) for r in data[start:start+6]],
            'cyber': days(data[start+7][1:], True),
            'touchy': days(data[start+8][1:], True)}

if __name__ == '__main__':
    data = list(csv.reader(open("jun-aug.csv", 'rb')))

    swizec = extract(data, 6)

    print swizec['touchy']
