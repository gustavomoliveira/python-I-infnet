""" Manipulação de Strings """

# aspas simples ou duplas para sua declaração
string = 'teste'
string = "teste"

# strings são imutáveis
nome = 'gustavo'
print(nome)
# nome[0] = 'G'
# print(nome) # TypeError: 'str' object does not support item assignment

# transformar em str
num = 3.12
num_string = str(num)
print(num_string)
print(type(num_string))

# concatenar str - '+' somente para concatenar str. não incluir nums
nome = 'Gustavo'
sobrenome = 'Mendes'
nome_completo = nome + ' ' + sobrenome
print(nome_completo)

# split()
conta = '1, Gustavo, 500'
campos = conta.split(',')
print(campos)
id = int(campos[0])
nome = campos[1]
saldo = float(campos[2])
print(id, nome, saldo)