'''
DESAFIO
Caio Victor Soares Cadete:
Monte um tabuleiro de Xadrez, no que diz respeito a quantidade de linhas e colunas
'''

'''
Xadrez tem 8 linhas e 8 colunas, ou seja i=8 e j=8.
'''

total_col = 8
total_line = 8


line = 1
while line <= total_line:
    column = 1
    while column <= total_col:
        print(f'{column=}, {line=}')
        column += 1
    line += 1


'''
Esse programa consiste em exibir as 8 linhas e 8 colunas do Xadrez, sem especificações de peças, habilidades e estratégias.
'''