import requests
import numpy as np
import json 

r = requests.get('https://coderbyte.com/api/challenges/json/age-counting')
r = json.loads(r.text)['data']
r = [l for l in r.split(',')]


total = 0

for n in r:
    if n.startswith(" age="):
        if int(n[5::]) >= 50:
            total += 1
            
print('*'*100)
print(f'el total de {total} usuarios son mayores o iguales a 50 años')
print('*'*100)


group =[]
for i in range(0,len(r),2):
    n = ((r[i]+','+r[i+1]))
    list=dict((l.split('=') for l in n.split(',')))
    group.append(list)   
print(group)
#print(len(r.json()['data']))