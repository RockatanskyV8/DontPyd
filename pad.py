from bs4 import BeautifulSoup
import requests
import os
import sys

args = sys.argv[1:] #[1]

link = ''
for arg in args:
    link += '/' + arg

source = requests.get('http://dontpad.com' + link).text

soup = BeautifulSoup(source, 'lxml')

file = open(args[-1] + '.txt', 'w')
file.write(soup.find('textarea', {"id": "text"}).text)
file.close()
os.system("vim " + args[-1] + '.txt')
