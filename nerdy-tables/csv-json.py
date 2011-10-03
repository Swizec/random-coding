
import csv, collections, json
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
            if len(item) < 3:
                item.append(0)
            return sum(item) if combine else item

        return list(flatten([map(clean, grouper(2, row[0:27])),
                             map(clean, grouper(3, row[28:123])),
                             map(clean, grouper(3, row[127:144]))]))
    def combine(rows):
        def col(n, day):
            return [d[n] for d in day]
        def _index(val, data):
            return data.index(val) if val in data else -1
        return [[_index(1, col(0, [row[i] for row in rows])),
                 _index(1, col(1, [row[i] for row in rows])),
                 _index(1, col(2, [row[i] for row in rows]))]
                for i in xrange(len(rows[0]))]

    return {'horny': combine([days(r[1:]) for r in data[start:start+6]]),
            'cyber': days(data[start+7][1:], True),
            'touchy': days(data[start+8][1:], True)}

if __name__ == '__main__':
    data = list(csv.reader(open("jun-aug.csv", 'rb')))

    swizec = extract(data, 6)
    masa = extract(data, 21)

    open('./data.js', 'w').write('horny_data = '+json.dumps({'swizec': swizec,
                                                             'masa': masa}))
