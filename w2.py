import re
f = open('py4e-data.txt')
total = 0
for i in f:
    i.rstrip()
    y = re.findall('[0-9]+',i)
    if(len(y) != 0):
        y = list(map(int,y))
        total = total + sum(y)
print(total)
