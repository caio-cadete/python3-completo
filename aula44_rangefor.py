'''

For + Range
range -> range(start, stop, step)

obs*: o step também podemos usar negativos para irmos de trás para frente.

'''

# No While: 

# i = 0
# while i <= 5:
#     i += 1
#     print(i)



# No For + Range:

numeros = range(1,11) 
for count in numeros:  # Essa variável "count" foi criada por nós mesmos
    print(count)


# O For pega o nosso iterável, do seu iterável ele pede o nosso iterador , e ele pega esse iterador e solicita para o iterador qual que é o próximo valor e entrega nessa variável que criamos qual o próximo valor, repetindo sucessivamente, até os valores terminarem.