import requests
import numpy as np
import pandas as pd
import json 

r = requests.get('https://coderbyte.com/api/challenges/json/age-counting')
r = json.loads(r.text)['data']
r = [l for l in r.split(',')]
total = 0

for n in r:
    if n.startswith(" age="):
        if int(n[5::]) >= 50:
            total += 1

print(f'el total de {total} usuarios son mayores o iguales a 50 años')
#print(len(r.json()['data']))