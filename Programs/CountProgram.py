''' 

Esse é o programa do contador
O seu melhor amigo que te ensina a contar nas horas difíceis!

'''

start = input('Digite o número que você deseja iniciar a contagem: ')
finish = input('Digite o número que você deseja parar a contagem: ')

if start and finish: # True
    try:
        start_float = float(start)
        finish_float = float(finish)
    except:
        print('Não foi possível converter os valores em float') # Caso tenha algum valor Null ou diferente de Int/Float.

else:
     print('Valores null ou NaN')
    
condicao1 = start_float < finish_float
condicao2 = start_float > finish_float

if condicao1 or condicao2:

    while start_float <= finish_float:
        print(start_float)
        start_float += 1

    while start_float >= finish_float:
        print(start_float)
        start_float -= 1

else: 
    print('Os números são iguais')

