'''

Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = identidade

'''

# Nós estudamos anteriormente nas outras aulas que a variável é um apelido para uma coisa que está na memória
v1 = 'a' 
v2 = 'a' 
v3 = 'b' 
v4 = 'c' 

# O Python salva o mesmo id na memória para variáveis que possuem o mesmo valor
print(id(v1)) 
print(id(v2)) 
print(id(v3)) 
print(id(v4)) 

'''
Em resumo, duas variáveis com valores idênticos apontam para o mesmo valor de ID na memória.
'''


# Exemplo de Código ruim: 
# Definição/Criação de variável dentro de um 'if', 'elif' ou 'else'.
# Caso a condição seja False a variável 'passou_no_if' nunca será criada
# Altere a variável condição para testar:

condicao = True
# Intuito disso: Saber se o interpretador passou em determinado local por algum motivo qualquer (depende do algoritmo que estamos criando)
if condicao:
    passou_no_if = True 
    print('Faça algo')
else:
    passou_no_if = None
    print('Não faça algo')

print(passou_no_if)



# Exemplo de Código bom e intuitivo:
# Definição da variável fora do bloco de código 'if', aonde ela é 'None' por padrão e caso seja alterada conseguiríamos ver.
# Altere a variável condição para testar:

condicao = False
passou_no_if = None 

if condicao:
    passou_no_if = True # Bandeira fincada quando tiver algum valor -> Flag
    print('Faça algo')
else:
    print('Não faça algo')

print(passou_no_if, 5*'-' ,passou_no_if is None)
print(passou_no_if, 5*'-' , passou_no_if is not None)

if passou_no_if is None:
    print('Não passou no if')

if passou_no_if is not None: # ou else
    print('Passou no if')