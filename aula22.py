# Operadores Lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia toda expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor.
# São considerados falsy: 0, 0.0, '' e False
# Também existe o tipo 'None' (não existe) que é usado para representar um 'Não valor'

# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')
# senha_permitida = '123456'


# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')


# Avaliação de Curto Circuito (A linguagem checa só até aonde precisa para economizar recursos)


abc = False or False or 0 or 'abc' # abc

senha = input('Senha: ') or 'Sem senha'

print(senha)

if senha == 'Sem senha':
    print(abc)
else:
    print('Caio Cadete')

# Se qualquer avaliação/condição for considerada verdadeira, ele vai parar exatamente nesse valor, ou seja ele não checa mais nada após da falsa.