#Natasha Ramos-Gomez
#COP4538
#1/28/2020

import sys

st = sys.argv[0]
dt = {}

for ch in st:
        if ch not in dt:
            dt[ch] = 0
        dt[ch] = dt[ch] + 1

uniChar = True

for ch in st:
        print(ch, ":", dt[ch])
        if dt[ch] != 1:
            uniChar = False

if uniChar:
        print("This string is Unique! All characters only appear once.")
else:
        print("This string is not unique! A few characters appear more than once.")
              
 

