from itertools import count, cycle

for el in count(3):
    if el > 10:
        break
    print(el)

quarrel = 0
for el in cycle(['good morning!', ' good afternoon!', 'good evening!', 'good night!']):
    if quarrel > 10:
        break
    print(el)
    quarrel +=1