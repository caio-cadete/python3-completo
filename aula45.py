'''

Iterável -> STR, RANGE, ETC (__iter__)
Iterador -> Quem sabe entregar um valor por vez
Next -> Me entregue o próximo valor
Iter -> Me entregue seu iterador

'''

# __ é chamado de dunder no Python. 

texto = iter('Caio') # __iter__() # Entregador 

# Next (Entrega o próximo valor do iterável)
print(next(texto)) # .__next__()
print(next(texto)) # .__next__()
print(next(texto)) # .__next__()
print(next(texto)) # .__next__()


print(texto.__next__()) # Erro: StopIteration