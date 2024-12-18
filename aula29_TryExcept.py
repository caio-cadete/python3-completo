'''

Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar

Em algumas outras linguagens de programação é 'Try/Catch', e essa sintaxe tem o principal intuito de tentar (Try) executar um código que não tenha erro de sintaxe,
caso não consiga ela vai capturar o erro de lógica e você pode fazer o que quiser depois.

Obs*: O False em boolean não é erro.

'''
numero_str = input('Vou dobrar o número digitado: ')

try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT: ', numero_float)
# # print(f'O dobro de {numero} é {numero * 2}')
    print(f'O dobro de {numero_str} é {numero_str * 2:.2f}') # ERRO -> O PROGRAMA VAI PULAR PARA O EXCEPT
except:
    print('Isso não é um número')


# if numero_str.isdigit():

#     numero_float = float(numero_str)
# # print(f'O dobro de {numero} é {numero * 2}')
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')


# Chamamos de "FailFast": O intuito de errar com agilidez no 'Try', aonde queremos errar o mais rápido possível para que essa exceção venha ser capturada.
# Em vez de receber o feedback do erro, você capturar essa exceção, podendo manipular ela. 