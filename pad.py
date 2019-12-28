from bs4 import BeautifulSoup
import requests
import os
import sys
import json

args = sys.argv[1:] #[1]

link = ''
for arg in args:
    link += '/' + arg

source = requests.get('http://dontpad.com' + link).text

soup = BeautifulSoup(source, 'lxml')

file = open(args[-1] + '.txt', 'w')
file.write(soup.find('textarea', {"id": "text"}).text)
file.close()

os.system("nano " + args[-1] + '.txt')

file = open(args[-1] + '.txt', 'r')
raw  = file.read()

source = requests.post('http://dontpad.com' + link,
                       headers={ 'Content-type':'application/x-www-form-urlencoded;charset=UTF-8' },
                       data='text=' + raw )

file.close()
