def validar_data(dia, mes, ano):
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia >= 1 and dia <= 30:
            print('Data válida.')
        else:
            print('Dia inválido.')
    elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia >= 1 and dia <= 31:
            print('Data válida.')
        else:
            print('Dia inválido.')
    elif mes == 2:
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
    else:
        print('Mês inválido.')


# formato dia/mes/ano
dia = 17
mes = 10
ano = 2024
validar_data(dia, mes, ano)