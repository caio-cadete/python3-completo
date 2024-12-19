'''

Listas em Python
Tipo list - Mutável
Suporte vários valores de qualquer tipo
Conhecimentos reutilizáveis - Índices e fatiamento

Métodos úteis:

    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - Apaga um índice
    clear - Limpa a lista
    extend - Estende a lista
    + - Concatena listas

    append, insert, pop, del, clear, extend, +
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)

'''

#        0  1  2  3  
lista = [10,20,30,40]
lista.append('Caio')
print(lista)
ultimo_valor = lista.pop()
print(lista, 'Último valor:', ultimo_valor)

lista.append(123)
print(lista)
del lista[-1] # Apagar qualquer Índice da lista
print(lista)

# lista.clear() # Limpa a lista
# print(lista)

lista.insert(0, 5) # Método que recebe dois argumentos: Índex e o Objeto. Esse método serve para inserir um elemento em qualquer índice da lista.

# lista.insert(50000, 5) # Se o índice fornecido for maior que o tamanho atual da lista, o Python insere o objeto no final da lista.

# lista.insert(-123, 5) # Se o índice fornecido for maior que o tamanho atual da lista, o Python insere o objeto no final da lista.

print(lista)

try:
    print(lista[5]) # IndexError: list index out of range
except IndexError as error:
    print(f'Erro: {error}')
