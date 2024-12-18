# if / elif / else
# se / se não se / se não
# Estruturas Condicionais (Retorna um dado Booleano (True or False))

entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'Sim' or entrada == 'S' or entrada == 'entrar':
    print('Você entrou no sistema.')
elif entrada == 'Não' or entrada == 'N' or entrada == 'sair':
    print('Você saiu do sistema.')
else:
    print('Desculpe. Não entendi a sua resposta.')
    

print('Fora dos if\'s e elses')
