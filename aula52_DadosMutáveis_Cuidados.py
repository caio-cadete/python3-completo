'''

Cuidados com dados mutáveis
= Copiado o valor (Imutáveis)
= Aponta para o mesmo valor de memória (Mutável)

'''

# Dados Imutáveis
print('Dados Imutáveis:')

nome = 'Caio'
print(nome)
print(id(nome))
outra_variavel = nome
 
# Podemos apontar a variável nome para outro lugar na memória 

nome = 'João'
print(nome)
print(id(nome))
print(outra_variavel)

# O Garbage collector (GC), ou coletor de lixo, é um processo que gerencia automaticamente a memória de um programa, eliminando objetos que não estão mais sendo utilizados, como o valor 'Caio', que foi substituído por 'João' e não possui mais referências.

print('\r')

# Dados Mutáveis
print('Dados Mutáveis:')

# Apelido do Valor = Valor(es)
# O valor que está na memória e tem o id()
lista_a = ['Caio', 'Cadete']

# Nesse caso não estou copiando a lista a para a lista b, eu estou fazendo esses dois apelidos apontarem para um mesmo valor na memória

lista_b = lista_a
lista_a [0] = 'Qualquer coisa'
print(lista_a, lista_b)

# Apontando para o mesmo valor na memória
print(id(lista_a), id(lista_b))

# Copiando a lista e apontando para um valor diferente na memória
lista_c = lista_a.copy()
print(lista_c, id(lista_c))
