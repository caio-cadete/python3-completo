'''

Enumerate - Enumera Iteráveis (Índices)

'''

lista = ['Eclésia', 'Luise', 'Alexandre']

lista_enumerada = enumerate(lista)
print(lista_enumerada)
print(next(lista_enumerada))

for i in lista_enumerada:
    print(i)

