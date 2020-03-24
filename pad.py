from bs4 import BeautifulSoup
import requests
import os
import sys

EDITOR="nano"

args = sys.argv #[1]
path = (args[-1].split('/'))

link         = 'http://dontpad.com/' + args[-1]
headers_post = { 'Content-type':'application/x-www-form-urlencoded;charset=UTF-8' }

source = requests.get(link).text
soup = BeautifulSoup(source, 'lxml')

if args[1] == 'edit':

    file = open(path[-1], 'w')
    file.write(soup.find('textarea', {"id": "text"}).text)
    file.close()

    os.system('%s %s'%(EDITOR,path[-1]) )

    file = open(path[-1], 'r')
    raw  = file.read()

    requests.post(link, headers=headers_post, data='text=' + raw)

    file.close()

    os.remove(path[-1])

elif 'send:' in args[1]:
    sndFile = (args[1]).split(':')[1]

    file = open(sndFile, 'r')
    raw  = file.read()

    requests.post(link, headers=headers_post, data='text=' + raw )

    file.close()

else:

    print(soup.find('textarea', {"id": "text"}).text)
