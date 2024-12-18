'''

Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim

'''


qtd_linhas = 5
qtd_colunas = 5

linha = 1 # A variável 'linha' por padrão é '1' no primeiro while, já que o incremento nesse mesmo loop só vem após a variável 'coluna' se tornar '5' no segundo while.

while linha <= qtd_linhas:
    coluna = 1 
    while coluna <= qtd_colunas: 
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1

print('Acabou')



