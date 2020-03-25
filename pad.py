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

def edit(content):
    file = open(content, 'w')
    file.write(soup.find('textarea', {"id": "text"}).text)
    file.close()

    os.system('%s %s'%(EDITOR,path[-1]) )

    file = open(path[-1], 'r')
    raw  = file.read()

    requests.post(link, headers=headers_post, data='text=' + raw)

    file.close()

    os.remove(content)

def send(content):
    sndFile = (content).split(':')[1]

    file = open(sndFile, 'r')
    raw  = file.read()

    requests.post(link, headers=headers_post, data='text=' + raw )

    file.close()

options = args[1].split(":")[0] 

if options == 'edit':
    edit( path[-1] )
elif options == 'send':
    send( args[1] )
else :
    print(soup.find('textarea', {"id": "text"}).text)

