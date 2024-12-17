'''
Iterando strings com while

'''

    # + 01234567891011
nome = 'Caio Cadete' # 11 caracteres
    # - 1110987654321
len_name = len(nome)
indice = 0

# while indice <= len_name:
#     print(nome[indice])
#     indice += 1

# Minha tentativa
# while indice <= len_name:
#     print(nome[indice], end='*')
#     indice += 1

# Correção
novo_nome = ''
while indice < len_name:
    letra = nome[indice] 
    novo_nome += f'*{letra}'
    indice += 1

print(novo_nome)

