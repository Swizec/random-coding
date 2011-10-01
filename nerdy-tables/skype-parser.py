
FILE = '/Users/Swizec/Desktop/mismasss.html'

from BeautifulSoup import BeautifulSoup

soup = BeautifulSoup(open(FILE).read())

# roughly counts number of words the Remote has written on Skype
print sum([s.count(' ') for s in
              [dt.nextSibling.string if dt.nextSibling.string else ''
                        for dt in filter(lambda dt: dt['class'] == 'local',
                                         soup.findAll('dt'))]])
