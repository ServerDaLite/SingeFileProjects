# Dylan Hartman
# 02 / 04 / 2024
# JackboxCracker.py

'''
1. Connect to the jackbox server [https://ecast.jackboxgames.com/api/v2/rooms/{CODE HERE}]
2. Check to see if code is valid.
- IF VALID
    - Add to an dynamic array
3. Print list of codes.
'''

from bs4 import BeautifulSoup
from urllib.error import HTTPError
from threading import Thread
from urllib.request import urlopen
from json import loads

_RANGE = range(65, 90)
StartingLetter = 'A'

def GatherData(code: str) -> str:
    html_doc = urlopen(f"https://ecast.jackboxgames.com/api/v2/rooms/{code}").read()
    soup = BeautifulSoup(html_doc, "html.parser")
    data = loads(str(soup))
    return data

def GuessSection(SecondCode):
    for C in _RANGE:
        for D in _RANGE:
            code = f"{StartingLetter}{chr(SecondCode)}{chr(C)}{chr(D)}"
            try:
                data = GatherData(code)
    
                print(f"{code} : {data['body']['appTag']}")
            except:
                continue

for B in _RANGE:
    Thread(target=GuessSection, args=(B,)).start()