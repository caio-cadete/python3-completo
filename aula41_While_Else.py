'''

While/Else
Recurso específico de Python

'''

string = 'Valor qualquer'


i = 0

while i < len(string):
    letra = string[i]
    # if letra == ' ':
    #     break
    print(letra)
    i += 1

else: # Se refere a incapacidade de executar o laço
    print('Nome finalizado.')
print('Fora do While.')