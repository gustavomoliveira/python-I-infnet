from datetime import datetime

def somar_total(cliente):
    soma_total = 0 
    for total in cliente:
        soma_total += total[4]
    return soma_total

def data_hora_atual():
    data_hora_atual = datetime.now()
    data = data_hora_atual.strftime('%d/%m/%Y')
    hora = data_hora_atual.strftime('%H:%M')
    return f'{data} {hora}'