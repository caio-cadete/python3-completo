'''

Iterável -> STR, RANGE, ETC (Método: __iter__)
Método é uma ação que vai ser executada dentro de um objeto.

texto = 'Caio'
Ao utilizar o 'For, a primeira coisa que ele faz é solicitar um iterador para o objeto texto.

Iterador -> Quem sabe entregar um valor por vez
Next -> Me entregue o próximo valor
Iter -> Me entregue seu iterador

'''

# __ é chamado de 'dunder' no Python. 

texto = 'Caio' # Iterável
iterator = iter('Caio') # __iter__() # Transformando a String em Iterador/Entregador
print(iterator)
# Next (Entrega o próximo valor do iterável)
print(next(iterator)) # .__next__()
print(next(iterator)) # .__next__()
print(next(iterator)) # .__next__()
print(next(iterator)) # .__next__()

try:
    print(iterator.__next__())
except StopIteration:
    print('Erro:', StopIteration)

# while True:
#     try:
#         letra = next(iterator)
#         print(letra)
#     except StopIteration:
#         print(StopIteration)
#         break

# print(texto.__next__()) # Erro: StopIteration
# print(next(texto)) # Erro: StopIteration


