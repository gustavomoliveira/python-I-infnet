""" Aula 02 11/10 - Conceitos Básicos """
# linguagem interpretada assim como JS
# variável tipo snake_case

a = 3
print(type(a)) # type para verificar o tipo
a = 3.14
print(type(a))
a = 'Gustavo' # aspas duplas ou simples
print(type(a))
a = True
print(type(a))
# mesma variável, transformada de int em real > str > boolean. característica de uma liguagem fracamente tipada

""" Operadores aritméticos"""

op1 = 5
op2 = 2
result = op1 + op2
print(f'O resultado da soma é {result}')
result = op1 - op2
print(f'O resultado da subtração é {result}')
result = op1 * op2
print(f'O resultado da multiplicação é {result}')
result = op1 / op2 # divisão
print(f'O resultado da divisão é {result}')
result = op1 // op2 # divisão inteira
print(f'O resultado da divisão inteira é {result}')
result = op1 % op2 # módulo assim como em JS
print(f'O resto é {result}')
result = op1 ** op2 # exponenciação
print(f'O resultado da exponenciação é {result}')

""" Operadores relacionais """

result = op1 > op2
print(result)
result = op1 >= op2
print(result)
result = op1 < op2
print(result)
result = op1 <= op2 
print(result)
result = op1 == op2 # igual
print(result)
result = op1 != op2 # diferente
print(result)

""" Operadores lógicos and(&&), or(||), not(!=) """

result = (op1 > op2 and op1 == op2)
print(result)
result = (op1 > op2 and op1 != op2)
print(result)
# or, basta uma ser verdadeira
result = (op1 > op2 or op1 == op2)
print(result)
# not, inverte a sentença
result = (not (op1 > op2))
print(result)

""" Condicional """

num = -1
if num == 0:
    print('Número igual a zero')
elif num > 0:
    print('Número é maior que zero')
else:
    print('Número é menor que zero')

# match é o switch do python

