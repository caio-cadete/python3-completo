'''

Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim

'''

# Loop infinito (executado eternamente)
condicao = True
while condicao:
    # ...
    # pass
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')
    # print(1)
    # print(2)
    # print(3)
    # break

# CTRL + C ou CTRL + BREAK (KeyboardInterrupt)
# Para quebrar o laço infinito 'while' você pode colocar a condição em False em algum momento ou você pode digitar 'break' dentro de um laço

# Unreachable (inalcançável)
while True:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')
    # print(1)
    # print(2)
    # print(3)
print(123)





