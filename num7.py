# def fact(n):
#     if n == 1:
#         return 1
#     return n*fact(n-1)


def fact(n):
    rez = 1
    for el in range(1, n+1):
        rez *= el
        yield rez

f = fact(4)

for el in f:
    print(el)
