# F-STRINGS = Formatação Strings

nome = 'Caio Cadete'
altura = 1.70
peso = 63
imc = peso/(altura**altura)

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é de'
linha_3 = f'{imc:.2f}'
# {altura:,.2f} separar decimais em moeda, por exemplo 
print(linha_1)
print(linha_2)
print(linha_3)
print(f'O índice de massa corporal do {nome} é de {imc:.8f}') #f-strings

