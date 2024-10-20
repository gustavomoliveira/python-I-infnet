""" 
9 - Desenvolva um programa que aplique descontos progressivos com base no valor da compra:
desconto de 10% para compras acima de R$100, 15% para compras acima de R$200,
seguindo a projeção até R$500, para valores maiores do que esse, o desconto é fixado em 25%.
 """
def calculo_desconto(compra):
    if compra < 100:
        print(f'Sem desconto! Valor total a pagar é de R${compra:.2f}')
    elif compra <= 200:
        result = compra * 0.9
        print(f'Você ganhou 10% de desconto! Valor total a pagar é de R${result:.2f}.')
    elif compra <= 300:
        result = compra * 0.85
        print(f'Você ganhou 15% de desconto! Valor total a pagar é de R${result:.2f}.')
    elif compra <= 400:
        result = compra * 0.825
        print(f'Você ganhou 17.5% de desconto! Valor total a pagar é de R${result:.2f}.')
    elif compra <= 500:
        result = compra * 0.8
        print(f'Você ganhou 20% de desconto! Valor total a pagar é de R${result:.2f}.')
    else:
        result = compra * 0.75
        print(f'Você ganhou 25% de desconto! Valor total a pagar é de R${result:.2f}.')


compra = float(input('Digite o valor da sua compra: '))
calculo_desconto(compra)