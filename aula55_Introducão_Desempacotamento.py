'''

Introdução ao Desempacotamento + Tuples (Tuplas)

'''

lista = ['Maria', 'Helena', 'Caio']
print(lista)

nome_a, nome_b, nome_c = ['Maria', 'Helena', 'Caio'] # Desempacotamento
print(nome_b)

nome1, *resto = ['Maria', 'Helena', 'Caio'] # Desempacotamento
print(nome1, resto)

nome1, *_ = ['Maria', 'Helena', 'Caio'] # Desempacotamento
print(nome1, _)

_,nome2, *_ = ['Maria', 'Helena', 'Caio'] # Desempacotamento
print(nome2, _)

_,_,nome3, *_ = ['Maria', 'Helena', 'Caio'] # Desempacotamento
print(nome3, _)

# A convenção pelos programadores de Python é de que o '*_' é usado quando a variável não será utilizada. 
# Obs*: A variável não deixa de funcionar, mas ao utilizar a convenção '*_', se entende por parte dos desenvolvedores que a variável não terá utilidade.

nomes = ['Luise', 'Eclésia', 'Caio']
# A lista, carrega consigo métodos que permitem alterar valores.
nomes.append(1)
nomes[2] = 'Alexandre'
_,_,nome,*resto = nomes
print(nome)
print(nome,resto)

