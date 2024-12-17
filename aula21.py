# Operadores Lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras.
# Se qualquer valor for considerado falso, a expressão inteira será considerado falso, a expressão inteira será avaliada naquele valor.
# São considerados falsy: 0, 0.0, '' e False
# Também existe o tipo 'None' (não existe) que é usado para representar um 'Não valor'

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

# if True: (o if só vai ser executado se a função for True)
# ...
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Avaliação de Curto Circuito (A linguagem checa só até aonde precisa para economizar recursos)
print(True and True and True) # True
print(True and True and False) # False
print(False and True and False) # False

print(bool(''))
print(bool(' '))

# Se qualquer avaliação/condição for considerada falsa, ele vai parar exatamente nesse valor, ou seja ele não checa mais nada após da falsa.