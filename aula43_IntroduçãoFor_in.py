'''

O uso do 'While' é para quando eu não sei precisamente quantas repetições teremos, como por exemplo digitar senha.

Em resumo, é um laço que poderia ter repetições infinitas.

Exemplo:

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x): ')
#     repeticoes += 1

'''



texto = 'Python'

i = 0
tamanho_string = len(texto)

while i < tamanho_string:
    print(texto[i], i)
    i += 1
    
senha_salva = '123456'
senha_digitada = ''
repeticoes = 0

print('-----------------')

'''

A definição do 'For' se baseia em uma estrutura de repetição para coisas finitas.

'''
novo_texto = ''
for letra in texto: # Essa variável "letra" foi criada por nós mesmos
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto)