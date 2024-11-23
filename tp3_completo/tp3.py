# Exercício 1
def validar_nome_sobrenome(msg):
    while True:
        palavra = input(msg).strip()
        if all(char.isalpha() or char.isspace() for char in palavra):
            return palavra
        else:
            print('ERRO: Digite apenas letras/caracteres.')

def nome_e_sobrenome():
    nome = validar_nome_sobrenome('\nDigite o nome: ').title()
    sobrenome = validar_nome_sobrenome('\nDigite o sobrenome: ').title()
    print()
    print(nome + ' ' + sobrenome)

nome_e_sobrenome()

# Exercício 2
def validar_input(msg):
    while True:
        entrada = input(msg).strip()
        if all(char.isalpha() or char.isspace() for char in entrada):
            return entrada
        else:
            print('ERRO: Digite um caractere válido.')

def validar_nome_sobrenome():
    while True:
        nome_sobrenome = validar_input('Digite o nome e sobrenome(pelo menos 2 caracteres cada): ').split()
        for palavra in nome_sobrenome:
            if len(palavra) >= 2:
                return nome_sobrenome
        else:
            print(f'\nERRO: {" ".join(nome_sobrenome).title()} não cumprem os requisitos indicados.\n')

nome_sobrenome = validar_nome_sobrenome()
print(f'\nOlá, {" ".join(nome_sobrenome).title()}!')

# Exercício 3
def validar_input(msg):
    while True:
        entrada = input(msg).strip()
        if all(char.isalpha() or char.isspace() for char in entrada):
            return entrada
        else:
            print('\nERRO: Digite caracteres válidos.\n')

def exibir_sobrenome_nome():
    while True:
        entrada = validar_input('Digite seu nome e sobrenome: ').split()
        if len(entrada) < 2:
            print('\nERRO: Digite, pelo menos, um nome e um sobrenome.\n')
        else:
            nome = ' '.join(entrada[:-1]).title()
            sobrenome = ' '.join(entrada[-1:]).upper()
            return sobrenome, nome
    
sobrenome, nome = exibir_sobrenome_nome()
print(f'\n{sobrenome}, {nome}\n')

# Exercício 4
from datetime import datetime

def validar_entrada(msg):
    while True:
        try:
            entrada = input(msg)
            if datetime.strptime(entrada, "%d/%m/%Y"):
                return str(entrada)
        except ValueError:
            print('\nERRO: Digite uma data existente e no formato dd/mm/aaaa.')

def data_formato_inteiro():
    entrada = validar_entrada('\nDigite uma data no formato dd/mm/aaaa: ').split('/')
    dia = int(entrada[0])
    mes = int(entrada[1])
    ano = int(entrada[2])
    return dia, mes, ano

def validar_inteiros(dia, mes, ano):
    if all(isinstance(valor, int) for valor in [dia, mes, ano]):
        print(f'\nA data {dia:02d}/{mes:02d}/{ano} é composta por números inteiros.\n')
    else:
        print(f'\nA data {dia:02d}/{mes:02d}/{ano} NÃO é composta por números inteiros.\n')

dia, mes, ano = data_formato_inteiro()
validar_inteiros(dia, mes, ano)

# Exercício 5
def converter_data():
    entrada = input('\nDigite uma data no formato dd/mm/aaaa: ').split('/')
    dia = int(entrada[0])
    mes = int(entrada[1])
    ano = int(entrada[2])
    return dia, mes, ano

def fevereiro_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def validar_mes(mes):
    if mes < 1 or mes > 12:
        print(f'ERRO: Mês inválido')
        return False
    return True

def validar_dias(dia, mes, ano):
    dias_nos_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if mes == 2 and fevereiro_bissexto(ano):
        dias_nos_meses[1] = 29

    if dia < 1 or dia > dias_nos_meses[mes - 1]:
        return False
    return True
        
def validar_data(dia, mes, ano):
    if not validar_mes(mes) or not validar_dias(dia, mes, ano):
        return f'\nA data {dia:02d}/{mes:02d}/{ano} NÃO é válida.\n'
    return f'\nA data {dia:02d}/{mes:02d}/{ano} é válida.\n'
              
dia, mes, ano = converter_data()
mensagem = validar_data(dia, mes, ano)
print(mensagem)

# Exercício 6
from datetime import datetime

def validar_entrada(msg):
    while True:
        try:
            entrada = input(msg)
            if datetime.strptime(entrada, "%d/%m/%Y"):
                return str(entrada)
        except ValueError:
            print('\nERRO: Digite uma data existente e no formato dd/mm/aaaa.')

def converter_data():
    entrada = validar_entrada('\nDigite uma data no formato dd/mm/aaaa: ').split('/')
    dia = int(entrada[0])
    mes = int(entrada[1])
    ano = int(entrada[2])
    return dia, mes, ano

def escrever_data(dia, mes, ano):
    nomes_meses = [
        'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 
        'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
    ]
    nome_mes = nomes_meses[mes -1]
    return f'\n{dia:02d} de {nome_mes} de {ano}\n.'

dia, mes, ano = converter_data()
mensagem = escrever_data(dia, mes, ano)
print(mensagem)

# Exercício 7
def validar_input(msg):
    while True:
        entrada = input(msg).strip().lower()
        if all(char.isalpha() for char in entrada):
            return entrada
        else:
            print('\nERRO: Digite um caractere válido.')

def validar_palindromo():
    palavra = validar_input('\nDigite uma palavra e descubra se ela é um palíndromo: ')
    if palavra[::-1] == palavra:
        return f'\nA palavra {palavra} é palíndromo!\n'
    return f'\nA palavra {palavra} NÃO é um palíndromo...\n'

mensagem = validar_palindromo()
print(mensagem)

# Exercício 8
def validar_input(msg):
    while True:
        entrada = input(msg).strip()
        if all(char.isalpha() or char.isspace() for char in entrada):
            return entrada
        else:
            print('ERRO: Digite apenas letras e espaços.')

def contar_vogais():
    entrada = validar_input('\nDigite uma palavra ou frase para contar suas vogais: ')
    vogais = ['a', 'e', 'i', 'o', 'u']
    contador = 0
    
    for letra in entrada:
        if letra in vogais:
            contador += 1
    return f'\nVocê digitou "{entrada.title()}" que possui {contador} vogais.\n'
    
mensagem = contar_vogais()
print(mensagem)

# Exercício 9
def validar_telefone(msg):
    while True:
        entrada = input(msg).strip()
        if all(num.isdigit() for num in entrada) and len(entrada) == 11:
            return f'\n({entrada[:2]}) {entrada[2:7]}-{entrada[7:]}\n'
        else:
            print(f'\nERRO: O número de telefone precisa de 11 dígitos e apenas números.\n')

mensagem = validar_telefone('\nDigite um número de telefone com 11 dígitos: ')
print(mensagem)

# Exercício 10
def validar_entrada(msg):
    while True:
        try:
            entrada = int(input(msg))
            if 1 <= entrada <= 7:
                return entrada
            else:
                print('\nERRO: Número inválido.\n')
        except ValueError:
            print('\nERRO: Digite um número inteiro.\n')

def exibir_dia_da_semana(entrada):
    dias = ['Domingo', 'Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sábado']
    return dias[entrada - 1]

entrada = validar_entrada('\nDigite um número (1 a 7) para verificar o dia da semana: ')
mensagem = exibir_dia_da_semana(entrada)
print(f'\n{mensagem}\n')

# Exercício 11
def validar_cpf(msg):
    while True:
        entrada = input(msg).strip()
        if all(num.isdigit() for num in entrada) and len(entrada) == 11:
            return f'\n{entrada[:3]}.{entrada[3:6]}.{entrada[6:9]}-{entrada[9:]}\n'
        else:
            print(f'\nERRO: O número do CPF precisa de 11 dígitos e apenas números.\n')

mensagem = validar_cpf('\nDigite um número de CPF com 11 dígitos e apenas dígitos: ')
print(mensagem)

# Exercício 12
def validar_frase(msg):
    while True:
        frase = input(msg).strip()
        if all(char.isalpha() or char.isspace() for char in frase):
            return frase
        else:
            print('\nERRO: Digite apenas letras.\n')

def inverter_frase():
    frase = validar_frase('\nDigite uma frase: ')
    frase_invertida = ''

    for char in reversed(frase):
        frase_invertida += char
    return frase_invertida

frase_invertida = inverter_frase()
print(f'\n{frase_invertida}\n')

# Exercício 13
def validar_frase(msg):
    while True:
        frase = input(msg).strip()
        if all(char.isalpha() or char.isspace() for char in frase):
            return frase
        else:
            print('\nERRO: Digite apenas letras.\n')

def inverter_frase():
    frase = validar_frase('\nDigite uma frase qualquer: ')
    return frase[::-1]

frase_invertida = inverter_frase()
print(f'\n{frase_invertida}\n')

# Exercício 14
def validar_frase(msg):
    while True:
        frase = input(msg).strip()
        if all(char.isalpha() or char.isspace() for char in frase):
            return frase
        else:
            print('\nERRO: Digite apenas letras.\n')

def fatiar_frase():
    frase = validar_frase('\nDigite uma frase qualquer: ')
    cinco_primeiros = frase[:5]
    cinco_ultimos = frase[-5:]
    return cinco_primeiros, cinco_ultimos

cinco_primeiros, cinco_ultimos = fatiar_frase()
print(f'\nCinco primeiros caracteres: {cinco_primeiros}')
print(f'\nCinco últimos caracteres: {cinco_ultimos}\n')

# Exercício 15
def substituir():
    entrada = '1;Maria;1000'
    com_virgula = entrada.replace(';', ',')
    return com_virgula

com_virgula = substituir()
print(com_virgula)

# Exercício 16
def validar_num(msg):
    while True:
        try:
            num = int(input(msg))
            return num
        except ValueError:
            print('ERRO: Digite um número.')

def calcular_media(num1, num2):
    media = (num1 + num2) / 2
    return media

num1 = validar_num('\nDigite o primeiro número: ')
num2 = validar_num('\nDigite o segundo número: ')
media = calcular_media(num1, num2)
print(f'\nA média entre {num1} e {num2} é igual a {media}.\n')
