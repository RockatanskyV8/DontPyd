from bs4 import BeautifulSoup
import requests
import os
import sys

args = sys.argv #[1]
link = (args[-1].split('/'))

source = requests.get('http://dontpad.com/' + args[-1]).text
soup = BeautifulSoup(source, 'lxml')

if args[1] == 'edit':

    file = open(link[-1] + '.txt', 'w')
    file.write(soup.find('textarea', {"id": "text"}).text)
    file.close()

    os.system("nano " + link[-1] + '.txt')

    file = open(link[-1] + '.txt', 'r')
    raw  = file.read()

    requests.post('http://dontpad.com/' + args[-1],
                   headers={ 'Content-type':'application/x-www-form-urlencoded;charset=UTF-8' },
                   data='text=' + raw )

    file.close()

elif 'send:' in args[1]:
    aux = (args[1]).split(':')[1]

    file = open(aux, 'r')
    raw  = file.read()

    requests.post('http://dontpad.com/' + args[-1],
                   headers={ 'Content-type':'application/x-www-form-urlencoded;charset=UTF-8' },
                   data='text=' + raw )

    file.close()

else:

    print(soup.find('textarea', {"id": "text"}).text)
