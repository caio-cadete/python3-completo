'''

Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um 
número inteiro, informe que não é um número inteiro.

'''

print(30 * '*') # Separar exercícios
print('Exercício 1)')

numero_str = input('Digite um número inteiro: ')

try:
    # numero_digito = numero_str.isdigit() # Função que chega se o usuário digitou só números
    numero_int = int(numero_str)
    if numero_int % 2 == 0:
        print('Esse número é par')
    else:
        print('Esse número é ímpar')
except:
    print('Erro')

'''

Faça um programa que pergunta a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. 
Ex: Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

'''

print(30 * '*') # Separar exercícios
print('Exercício 2)')

try:
    hora_str = input('Que horas são? ')
    hora_int = int(hora_str)

    bom_dia = hora_int >= 0 and hora_int <= 11
    boa_tarde = hora_int >= 12 and hora_int <= 17
    boa_noite = hora_int >= 18 and hora_int <= 23

    if bom_dia:
        print('Bom dia')
    elif boa_tarde:
        print('Boa tarde')
    elif boa_noite:
        print('Boa noite')
    else:
        print('Erro')

except:
    print('Você não informou números')

'''

Faça um programa que peça o primeiro nome do usuário. Se o nome
tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver entre
5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva
"Seu nome é muito grande".

'''

print(30 * '*') # Separar exercícios
print('Exercício 3)')


nome = input('Digite o seu primeiro nome: ')

if nome.isdigit() == False:
    if len(nome) <= 4 and len(nome) > 1 :
        print('Seu nome é curto')
    elif len(nome) > 4 and len(nome) <= 6:
        print('Seu nome é normal')
    elif len(nome) > 6:
        print('Seu nome é muito grande')
    else:
        print('Erro')
else:
    print('Erro')

print(30 * '*') # Separar exercícios


