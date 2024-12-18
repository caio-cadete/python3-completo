# Tipos primitivos no Python (str,int,float,bool)

# Tipos int e float

# int -> Número inteiro
# O tipo int representa qualquer número positivo ou negativo.
# int sem sinal é considerado positivo

# Número literal inteiro 
print(11) 
print(-11)
print(0)

# float -> Número com ponto flutuante
# O tipo float representa qualquer número positivo ou negativo com ponto flutuante.
# float sem sinal é considerado positivo.

print(1.1, 10.11)



# A função type mostra o tipo que o Python inferiu ao valor.
# Por convenção, tudo que tiver a letra minúscula e for executável -> callabe () é chamado de função.
# Type é uma classe, porém para ficar mais fácil chamamos agora de função.
# Tudo em python é um objeto
print(  type('Cadete')  )
print(type(10))
print(type(10.10), type(-1.1), type(0.0))
