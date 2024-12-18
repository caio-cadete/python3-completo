nome = 'Caio Cadete'
altura = 1.70
peso = 63
imc = ... # Esses '...' significam elipses e são usados para várias coisas, uma delas pode ser como placeholder (ou seja, um código que não foi escrito e não gera erros)

# Índice de Massa Corporal = IMC

# Caio Cadete tem 1.70 de altura, pesa 66 quilos e seu IMC é x
# Exercício
# Cálculo do IMC (IMC = peso/(altura * altura))

imc = peso/(altura**altura)
# imc = peso/(altura**2)
print(f'O índice de massa corporal do {nome} é de {imc:.8f}') #f-strings
print(nome, 'tem', altura, 'de altura')
print('pesa', peso, 'quilos e seu imc é', imc)

