
import csv, collections, json
from itertools import izip_longest, chain

def extract(data, start):
    def grouper(n, iterable, fillvalue=0):
        "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
        args = [iter(iterable)] * n
        return list(izip_longest(fillvalue=fillvalue, *args))
    def flatten(listOfLists):
        "Flatten one level of nesting"
        return chain.from_iterable(listOfLists)
    def col(col):
        col = list(reversed(col))
        chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        return sum([(chars.index(col[i])+1)*(len(chars)**i) for i in range(len(col))])-1

    def days(row, combine=False):
        def clean(item):
            item = map(lambda x: int(x) if x != None and x != '' else 0,
                       list(item))
            item += [0]*(3-len(item))
            return sum(item) if combine else item

        return list(flatten([map(clean, grouper(2, row[col('B'):col('BD')])),
                             map(clean, grouper(3, row[col('BD'):col('EV')])),
                             map(clean, grouper(3, row[col('EY'):col('FQ')]))]))

    def combine(rows):
        def _col(n, day):
            return [d[n] for d in day]
        def _index(val, data):
            return data.index(val)+1 if val in data else -1

        l = len(rows[0])

        return [[_index(1, _col(0, [row[i] for row in rows])),
                 _index(1, _col(1, [row[i] for row in rows])),
                 _index(1, _col(2, [row[i] for row in rows]))]
                for i in xrange(l)]

    cleaned = data[start:start+9]

    return {'horny': combine([days(r) for r in cleaned[:7]]),
            'cyber': days(cleaned[7], True),
            'touchy': days(cleaned[8], True)}

if __name__ == '__main__':
    data = list(csv.reader(open("jun-aug.csv", 'rb')))

    max_len = max([len(r) for r in data])
    data = [r+['']*(max_len-len(r)) for r in data]

    swizec = extract(data, 6)
    masa = extract(data, 21)

    open('./data.js', 'w').write('horny_data = '+json.dumps({'swizec': swizec,
                                                             'masa': masa}))
