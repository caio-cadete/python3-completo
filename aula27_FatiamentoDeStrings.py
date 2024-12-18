'''

Fatiamento de strings
012345678
Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: A função len retorna a quantidade de caracteres da str


'''


# O espaço é um caracter válido e conta bytes normal na programação.
# Contagem é diferente e índice. O python é indexado em 0, mas a sua contagem começa de 1.
variavel = 'Olá mundo'
print(variavel[5])
print(variavel[3])
print(variavel[-4])

print(variavel[0:3])
print(variavel[4:])

print(variavel[0:5])
print(variavel[:5])


print(variavel[-8:-2])

print(len(variavel[3]))
print(len(variavel))

# A função len() não funciona somente com strings,
# inclusive no VS Code ela diz que funciona com
# um objeto de tipo 'Sized'.


# Fatiamento [i:f:p] [::]
# O 'p' ou passo significa de quantos em caracteres vai pular.
print(variavel[0:9:1]) 
print(variavel[0:len(variavel):2])
print(variavel[0:9:3])

print(20 * '-')

print(variavel[::-1]) # Leitura ao contrário
print(variavel[-1:-10:-1]) # Leitura ao contrário