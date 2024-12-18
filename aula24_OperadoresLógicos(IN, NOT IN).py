# Operadores in e not in ("está entre" e "não está entre")
# Strings são iteráveis (Iteráveis significa que você pode navegar item por item)

nome = 'Cadete'
print(nome[2])
print(nome[-6])

# 0 1 2 3 4 5 - índices
# C A D E T E
# -6-5-4-3-2-1


print('C' in nome) # True
print('a' in nome) # True
print('d' in nome) # True
print('e' in nome) # True
print('t' in nome) # True
print('e' in nome) # True

print(10 * '-')

print('Ca' not in nome)     # False
print('Cadete' not in nome) # False
print('de' not in nome)     # False
print('te' not in nome)     # False
print('p' not in nome)      # True
print('q' not in nome)      # True
print('r' not in nome)      # True


print(10 * '-')


nome = input('Digite o seu nome: ')
encontrar = input('Digite o caracter que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')