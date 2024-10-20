""" 
7 - Faça um programa que calcule o Índice de Massa Corporal (IMC) do usuário
e forneça feedback com base no valor (por exemplo, abaixo do peso, peso normal, sobrepeso).
 """

def resultado_imc(peso, altura):
    imc = peso / (altura * altura)
    if imc < 18.5:
        print(f'O seu IMC é {imc:.1f}. Cuidado: o resultado indica Magreza!')
    elif imc >= 18.5 and imc <= 24.9:
        print(f'O seu IMC é {imc:.1f} e indica normalidade. Parabéns!')
    elif imc >= 25 and imc <= 29.9:
        print(f'O seu IMC é {imc:.1f}. Cuidado: o resultado indica Sobrepeso!')
    elif imc >= 30 and imc <= 34.9:
        print(f'O seu IMC é {imc:.1f}. Cuidado: o resultado indica Obesidade Grau I!')
    elif imc >= 35 and imc <= 39.9:
        print(f'O seu IMC é {imc:.1f}. Cuidado: o resultado indica Obesidade Grau II!')
    else:
        print(f'O seu IMC é {imc:.1f}. Cuidado: o resultado indica Obesidade Grau III!')


peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
resultado_imc(peso, altura)