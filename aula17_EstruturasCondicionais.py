# if / elif / else
# se / se não se / se não

# Entendendo a Identação
# condicao = True 
condicao = 10 != 10


if condicao: # Pode ter sozinho
    print('True')
else: # Não pode ter sozinho (Última condição a ser executada)
    print('False')

if 10 == 10:  # Pode ter sozinho
    print('True')


print('Fora do if')


condicao1 = True # O interpretador sempre vai executar a primeira condição que for verdadeira e vai sair do bloco.
condicao2 = True
condicao3 = True 
condicao4 = True 
condicao4 = True 

if condicao1: 
    print('Código para condição 1')
    print('Código para condição 1')
elif condicao2:
    # ... # elipses (placeholders)
    # pass # passar
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else: 
    print('Nenhuma condição foi satisfeita')
