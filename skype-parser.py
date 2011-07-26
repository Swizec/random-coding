
FILE = '/Users/Swizec/Desktop/mismasss.html'

from BeautifulSoup import BeautifulSoup

soup = BeautifulSoup(open(FILE).read())

print soup.pretify()
