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

lista_a = [1,2,3]
lista_b = [4,5,6]
# Polimorfismo, pois o sinal de '+' se comporta de outra maneira com outro tipo de dado.
lista_c = lista_a + lista_b # Concatena listas
lista_d = lista_a.extend(lista_b) # Essa ação trabalha na 'lista a' em si e não retorna nada.
lista_b.extend(lista_a)
print(lista_c)
print(lista_d) # None
print(lista_a)
print(lista_b)