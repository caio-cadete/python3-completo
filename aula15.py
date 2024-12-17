# Input (entrada): É uma função que solicita dados do usuário
# Output do Visual Studio Code: Read Only


nome = input('Qual o seu nome? ') # A mensagem do Input sempre é recebida no terminal. Através do Input temos a possibilidade de coleta de dados em variáveis.
# Se atentar pois o input sempre é salvo em uma variável em tipo 'str'.
print(f'O seu nome é {nome=}')
# Qual o seu nome? Caio
# O seu nome é nome='Caio'


numero_1 = int(input('Digite um número: ')) # É preciso converter de 'str' para 'int' ou 'float' (coerção/conversão de tipos)
numero_2 = int(input('Digite outro número: ')) # É preciso converter de 'str' para 'int' ou 'float' (coerção/conversão de tipos)
print(f'O primeiro número que você digitou foi {numero_1 = :.2f}')
print(f'A soma dos números é {numero_1 + numero_2}')


numero_3 = input('Digite um número: ') # 'str'
numero_4 = input('Digite outro número: ') # 'str

print(f'A soma dos números é {numero_3 + numero_4}') # Concatenação de 'str', pois não definimos o tipo para número.


# Mais prudente, mais experiente:
# Criar uma nova variável com a coerção/conversão de tipo

numero_1 = input('Digite um número: ') # É preciso converter de 'str' para 'int' ou 'float' (coerção/conversão de tipos)
numero_2 = input('Digite outro número: ') # É preciso converter de 'str' para 'int' ou 'float' (coerção/conversão de tipos)

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'O primeiro número que você digitou foi {numero_1 = :.2f}')
print(f'A soma dos números é {numero_1 + numero_2}')