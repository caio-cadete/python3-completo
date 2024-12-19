'''

Listas em Python
Tipo list - Mutável
Suporte vários valores de qualquer tipo
Conhecimentos reutilizáveis - Índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)

'''

# Ao apagar itens de uma lista GRANDE, o processamento pode ser demorado, por conta da reordenação de índices.
# É importante evitar situações que façam os índices da lista serem reordenados.

# Em uma lista, é mais prático adicionar ou remover itens do final.
# Ao trabalhar com o final da lista, o Python só precisa ajustar o índice final, em vez de reordenar todos os elementos.


#        0  1  2  3  4  5
lista = [10,20,30,40]


# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])

lista.append(50) # Adicionar valores ao final da minha lista
lista.pop() # Remove valores ao final da minha lista
lista.append(60) # Adicionar valores ao final da minha lista 
lista.append(70) # Adicionar valores ao final da minha lista
ultimo_valor = lista.pop() # Remove valores ao final da minha lista
lista.pop(-2) 
print(lista, 'Removido,', ultimo_valor )