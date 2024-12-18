'''
 
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que já vimos, porém existem outros que veremos durante o curso: str, int, float, bool (suficiente para fazer a maioria das coisas no Python)

build-in: Tipo 'embutido' que vem dentro do Python, ou seja, é nativo.
Python é uma linguagem muito grande, caso tenha alguma dúvida, é importante consultar a documentação.

'''

"""Dados Imutáveis"""
string = 'Caio Cadete'
outra_variavel = string # Copiando valor da variável 'string' para 'outra_variavel' 


# string[3] = 'ABC' # Não da para fazer isso, pois o dado 'str' é imutável. Daria para fazer isso no Python, porém somente com dados mutáveis.
print(string[3]) # o


outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(outra_variavel)

meu_nome = 'Caio Cadete'
mudar_sobrenome = f'{meu_nome[0:4]} Soares'
print(mudar_sobrenome)

# str,int,float e bool são objetos (tem ações que posso executar dentro desses objetos, manipulando-os)

# Métodos de String

nome = 'caio'
print(nome.capitalize())
salario = '1578.23'
print(salario.zfill(10)) # Definir um lenght (comprimento), caso não tenha algarismos ocorrerá o preenchimento de zeros a esquerda para totalizar esse comprimento.






