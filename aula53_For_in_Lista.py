'''

For in com listas

'''

# Relembrando como funciona o Iterador:
abc = 'ABC'
oi = iter(abc) # oi = abc.__iter__()
print(oi)
print(next(oi)) # print(oi.__next__)
print(next(oi)) # print(oi.__next__)
print(next(oi)) # print(oi.__next__)

print('\r')

for i in abc:
    print(i)

print('\r')

# Uma lista é um iterável em Python.

lista = ['Caio', 'Victor', 'Soares', 'Cadete', 23, 'anos', True]

for objeto in lista:
    print(objeto, type(objeto))


