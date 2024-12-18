# Conversão de tipos, Coerção
# Type Convertion, Type Casting, Coercion
# É o ato de converter um tipo em outro
# Tipos imutáveis e primitivos (literais): str, int, float, bool

# Polimorfismo: Utilizando o mesmo operador para fazer coisas diferentes.
# Isso acontece geralmente em tipagem dinâmica, pois você passa tipos para o interpretador e ele sabe o que fazer.


print(1 + 1) # Soma
print('a' + 'b') # Concatenar strings


# print('1' + 1) # Errado, somente str com str

print(int('1') + 1)
print(float('1') + 1)
print(type(float('1')))
print(bool(''))
print(bool(' '))


print(str(11) + 'b')