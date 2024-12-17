'''

Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
Obs*: Um 'x' minúsculo gera um hexadecimal minúsculo e o 'X' maiúsculo gera um hexadecimal maiúsculo.

'''

# O que é interpolação?
# R: Interpolação com .format, só que agora de um jeito diferente

nome = 'Caio'
preco = 1000.76543210
variavel_interpolacao = '%s, o preço total foi  de R$%.2f'  % (nome,preco) 
print(variavel_interpolacao)
# variavel_fstrings = f'{nome}, o preço total foi  de R${preco:,.2f}'
# print(variavel_fstrings)
print('O hexadecimal de %d é %08x' % (1500,1500))


# Formatos que posso escolher:
# 1- F-Strings
# 2- .format
# 3- Interpolação de Strings