# Tudo em Python são objetos!
# O que caracteriza um objeto é que ele pode fazer uma ação e essas ações são chamadas métodos.
# Métodos são ações que manipulam o objeto colocando o ponto (.)

a = 'A'
b = 'B'
c = 1.1
string = 'a={} b={} c={:.2f}'
string = 'a={0} b={1} c={nome3:.2f}'
formato = string.format(
    a, b, nome3=c) # A,B são argumentos que estamos passando para dentro de .format. O C também está sendo passado para dentro de .format, porém é um parâmetro.
print(formato)


# argumento X parâmetro
# .format
# a,b = argumento
# c = parâmetro



variavel2 = 'variavel={abc}'.format(abc=1)
print(variavel2)

