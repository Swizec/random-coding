
if __name__=='__main__':
    f = open('data.csv')

    data = [l.strip().split(',') for l in f]
    labels = data[0]
    data = [dict([(labels[i], int(r[i]) if r[i].isdigit() else r[i]) for i in xrange(len(labels))])
            for r in data[1:]]

    f.close()

    f = open('data.js', 'w')
    f.write("var DATA = %s" % data)
    f.close()
