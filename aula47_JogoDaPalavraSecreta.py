'''

Faça um jogo para o usuário adivinhar qual a palavra secreta.

- Você vai propor uma palavra secreta qualquer vai dar a possibilidade para o usuário digitar apenas uma letra.

- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.

    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba *.

Faça a contagem de tentativas do seu usuário.

'''

import os

palavra_secreta = 'frango'
letras_acertadas = ''
letra_digitada = None
letra_digitada_um_digito = None
tentativas = 0

while True:
    letra = input('Digite uma letra: ')
    if letra.isalpha():
        letra_digitada = True
    else:
        print('Retorne novamente e digite uma letra.')
        continue
    
    if len(letra) == 1:
        letra_digitada = True
        letra_digitada_um_digito = True
    else: 
        print('Digite somente UMA letra.')
        letra_digitada_um_digito = False
        continue
    
    if letra_digitada is True and letra_digitada_um_digito is True:
        print(f'Sua letra escolhida foi: {letra}')
    else:
        print(f'Letra não identificada.')
        continue

    tentativas = tentativas + 1
    
    # Lógica do Jogo da Palavra Secreta

    
    '''
    
    Essa condição verifica se a letra digitada pelo usuário pertence a palavra secreta.
    Essa variável 'letras_acertadas' tem o intuito de armazenar todas as letras que foram acertadas, ou seja pertencentes a palavra secreta.

    '''

    if letra in palavra_secreta:
        # letras_acertadas = letras_acertadas + letra
        letras_acertadas += letra

    '''
    
    Cria-se uma variável para armazenar a nossa palavra concatenada, de acordo com as tentativas, chamada de 'palavra_formada'.

    Realiza-se um loop 'for', iterando por cada índice da nossa palavra secreta.
    
    Caso o usuário acerte a letra, a letra será exibida. 
    Caso o usuário não acerte a letra, ela aparecerá como '*'.
    
    '''

    palavra_formada = ''
    for i in palavra_secreta:
        if i in letras_acertadas:
            # palavra_formada = palavra_formada + i
            palavra_formada += i
        else:
            # palavra_formada = palavra_formada + '*'
            palavra_formada += '*'

    print(f'Palavra formada: {palavra_formada}')
    if palavra_formada == palavra_secreta:
        os.system('cls') # Limpar Terminal
        print('VOCÊ GANHOU!! PARABÉNS!')
        print(f'A palavra era {palavra_secreta}.')
        print(f'Você teve um total de {tentativas} tentativas.')
        letras_acertadas = ''
        letra_digitada = None
        letra_digitada_um_digito = None
        tentativas = 0
        palavra_formada = ''
    break # Finalizar laço While