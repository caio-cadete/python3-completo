'''

Tipo Tupla - Uma lista Imutável

As tuplas são imutáveis, o que significa que, uma vez criadas, seus elementos não podem ser alterados. Essa característica das tuplas as torna úteis quando você deseja garantir que os dados permaneçam constantes.

'''

# Criando uma Tupla 

# 2 opções:

# Sem parênteses:
nomes_tuple1 = 'Maria', 'Helena', 'Luis'
print(type(nomes_tuple1))

# Com parênteses:
nomes_tuple2 = ('Maria', 'Helena', 'Luis')
print(type(nomes_tuple2))


nomes_tuple1 = 'Maria', 'Helena', 'Luis'
print(nomes_tuple1[0])
print(nomes_tuple1[-1])

# Essa tentativa de modificar uma tupla demonstra que, assim como as strings, as tuplas são imutáveis.

try:
    nomes_tuple1[0] = 'Jhony'
except TypeError as error:
    print('Não é possível atribuir o valor "Jhony" ao índice 0 de uma tupla, pois ela é imutável.')


# Convertendo a lista em Tupla:

nomes = ['Luise', 'Eclésia', 'Caio']
print(type(nomes))
nomes = tuple(nomes)
print(type(nomes))
nomes = list(nomes)
print(type(nomes))

# Não faz sentido tentar adicionar um valor a uma tupla, já que elas são imutáveis. Para fazer isso, seria necessário convertê-la em uma lista, adicionar o valor e depois transformá-la novamente em uma tupla. Porém, é mais prático e lógico criar uma nova tupla diretamente com os valores desejados.

