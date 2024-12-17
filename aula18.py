# Debugger = Depuração de código
# DE significa "tirar"
# BUG significa inseto e geralmente é um problema no seu software
# Debugger = 'Tirar um Bug'
# Breakpoint é aonde o interpretador vai parar antes de executar a linha. Se colocar o breakpoint no comentário ele não vai parar.

condicao1 = False # O interpretador sempre vai executar a primeira condição que for verdadeira e vai sair do bloco.
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

print('O interpretador pula do bloco depois de encontrar uma condição que atenda "True".')