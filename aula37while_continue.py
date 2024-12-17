'''

Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim

Quem sustenta o 'while' é o incremento. O incremento é o coração do loop.
Caso nós coloquemos o 'continue' antes do incremento, isso gerará um laço infinito.

break -> Finaliza o laço (usado para o while que está mais próximo)
continue -> Reinicia o laço (usado para o while que está mais próximo)

'''

contador = 0

while contador <= 100:
    contador += 1 # Cuidado! Ao utilizar o 'continue' antes do incremento ao lado, teremos um loop infinito

    # print(contador)
    # break # Ele vai finalizar o laço imediatamente

    if contador == 6:
        print('Não vou mostrar o 6')
        continue # Reinicia o laço 

    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue # Reinicia o laço   


    print(contador)

    if contador == 40:
        break # Finaliza o laço


print('Acabou')
   


