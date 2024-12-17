'''

"\" está na variável para garantir que a linha será quebrada.

Métodos de String:
* Converter para letra maiúscula: str.upper()
* Converter para letra minúscula: str.lower()

lowercase (minúsculo)
uppercase (maísculo)

'''


frase = 'O Python é uma linguagem de programação '\
        'multiparadigma. '\
        'Python foi criado por Guido van Rossum'
# Multiparadigma (vamos aprender alguns paradigmas ao longo do curso)
# Quero saber qual a letra apareceu mais vezes nessa frase

indice = 0
contagem_maior_letra = 0
letra_maior_contagem = ''
frase = frase.replace(' ' , '').replace('.', '').lower()
while indice < len(frase):
    letra = frase[indice] 
    contagem_letra = frase.count(letra)

    if contagem_maior_letra < contagem_letra:

        contagem_maior_letra = contagem_letra

        letra_maior_contagem = letra

    indice += 1

print('A letra que apareceu mais vezes foi ' f'"{letra_maior_contagem}", que apareceu 'f'{contagem_maior_letra}x.' )
    