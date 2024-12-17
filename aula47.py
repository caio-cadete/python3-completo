'''

Faça um jogo para o usuário adivinhar qual a palavra secreta.

- Você vai propor uma palavra secreta qualquer vai dar a possibilidade para o usuário digitar apenas uma letra.

- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.

    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba *.

Faça a contagem de tentativas do seu usuário.

'''

palavra_secreta = 'frango'
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
    if letra in palavra_secreta:
        for i in palavra_secreta:
            if letra == i:
                print(i)

            else:
                print(f'*')
    continue

    print(f'Você teve um total de {tentativas} tentativas.')

