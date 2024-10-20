def validar_data(dia, mes, ano):
    match mes:
        case 4 | 6 | 9 | 11:
            if dia >= 1 and dia <= 30:
                print('Data válida.')
            else:
                print('Dia inválido.')
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            if dia >= 1 and dia <= 31:
                print('Data válida.')
            else:
                print('Dia inválido.')
        case 2:
            if ano % 4 == 0:
                if dia >= 1 and dia <= 29:
                    print('Data válida.')
                else:
                    print('Dia inválido.')
            else:
                if dia >= 1 and dia <= 28:
                    print('Data válida.')
                else:
                    print('Dia inválido.')
        case _:
            print('Mês inválido.')

# princípio do SRP(single responsability principle)
def entrar_data():
    data = input('Entre com a data dd/mm/aaaa: ')
    return data

def dividir_data(data):
    dia_mes_ano = data.split('/') # retorna lista
    dia, mes, ano = dia_mes_ano # unpacking da lista atribuindo a multiplas variáveis
    return int(dia), int(mes), int(ano) # após desempacotar, conversão para int

data = entrar_data()
dia, mes, ano = dividir_data(data)
validar_data(dia, mes, ano)