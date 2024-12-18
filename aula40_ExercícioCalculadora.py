'''

Strings são imutáveis, isso significa que quando fazemos operações, outra string é retornada.

Funciona:

nome = 'João'
nome = f'{nome[:2]}a{nome[3]}'
print(nome)

Não Funciona:

nome = 'João'
nome[2] = a

'''


#  Calculadora com While 

while True:

    print(f'\r\nBem vindo a calculadora com While!\r\n')
    numeros_permitidos = None # Flag (bandeira)

    x = input('Digite o primeiro número: ')
    y = input('Digite o segundo número: ')
    operator = input('Digite um operador (+-/*) : ')    
    x_float = 0 
    y_float = 0 

    try: 
        # É preciso definir a variável fora do bloco para que ela exista no momento de averiguação de condicionais.
        x_float = float(x)
        y_float = float(y)
        numbers_allowed = True # Flag (bandeira)

    except:
    # except Exception as error: (Captar o erro para fazer alguma operação, por exemplo)
        print('Informe somente números.')
        numbers_allowed = None # Flag (bandeira)
        continue
            
    operators_allowed = '+-/*'
    
    if operator not in operators_allowed:
        print('Operador inválido.')
        continue

    if len(operator) > 1 :
        print('Digite somente um operador.')
        continue
    
    print('Realizando sua conta. Confira o resultado abaixo:')
    if operator == '+':

        print(f'{x_float} + {y_float} =', x_float + y_float)

    elif operator == '-':

        print(f'{x_float} - {y_float} =', x_float - y_float)

    elif operator == '/':

        print(f'{x_float} / {y_float} =', x_float / y_float)

    elif operator == '*':
    
        print(f'{x_float} * {y_float} =', x_float * y_float)
    else:
        print('Nunca deveria chegar aqui.') # Teste

    sair = input('Quer sair? [s]im : ').lower().startswith('s')

    if sair is True:
         
         print('Você saiu.')
         break


# Diferença:

# ==: Verifica se o valor é verdadeiro de forma geral (por exemplo, 1, "True", etc.).

# is: Verifica se é o objeto True exatamente.

# Então, use == quando você quer verificar se algo é "verdadeiro", e is quando você quer garantir que seja o objeto True especificamente.






