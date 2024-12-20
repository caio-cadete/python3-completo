'''

Exercício: Exiba os índices da lista

0 Maria
1 Helena
2 Luiz

'''

lista_exercicio = ['Maria', 'Helena', 'Luiz']
lista_exercicio.append('Caio')

# Usando Método .index do Python:
for i in lista_exercicio:
    indice = lista_exercicio.index(i)
    print(f'Nome: {lista_exercicio[indice]}, Índice: {indice}' )

print('\r')

# Usando 'While':

indice = 0

while indice < len(lista_exercicio):
    print(f'Índice: {indice}, {type(indice)}')
    print(f'Nome: {lista_exercicio[indice]}, {type(lista_exercicio[indice])}')
    indice += 1

print('\r')

# Usando 'For':
# Usando o recurso da Aula Anterior (aula53_For_in_Lista.py):
# Lembre-se que o 'range()' sempre começa com 0.

indices = range(len(lista_exercicio))
print(indices)

for indice in indices:
    print(f'Índice: {indice}, {type(indice)}')
    print(f'Nome: {lista_exercicio[indice]}, {type(lista_exercicio[indice])}')

    # print(f'Índice: {indice, lista_exercicio[indice]}, {type(indice)}')