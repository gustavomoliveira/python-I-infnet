""" 
14 - Escreva um programa que permita ao usuário votar em três opções
diferentes e, no final, exiba o número de votos de cada opção.
 """

def votacao():
    chocolate = 0
    doce_de_leite = 0
    goiabada = 0

    while True:
        escolha = int(input('Qual a sua sobremesa favorita? '))
        if escolha < 0 or escolha > 3:
            print('Opção incorreta! Escolha uma opção válida no Menu.')
            continue
        
        else:
            match escolha:
                case 1:
                    chocolate += 1
                    print(f'Você votou em Chocolate. Essa opção possui {chocolate} voto(s)')
                case 2:
                    doce_de_leite += 1
                    print(f'Você votou em Doce de Leite. Essa opção possui {doce_de_leite} voto(s)')
                case 3:
                    goiabada += 1
                    print(f'Você votou em Goiabada. Essa opção possui {goiabada} voto(s)')
                case 0:
                    print(f""" 
------- Votação Encerrada! -------
Número de votos finas:
Chocolate: {chocolate}
Doce de Leite: {doce_de_leite}
Goiabada: {goiabada}
----------------------------------
 """)
                    break
                case _:
                    print('Opção inválida!')

menu = """ 
------ OPÇÕES ------
[1] - Chocolate
[2] - Doce de Leite
[3] - Goiabada
[0] - Encerrar Votação
--------------------
 """

print(menu)
votacao()
