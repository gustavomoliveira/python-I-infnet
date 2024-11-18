"""
15 - Substituir “;” por “,”

Faça um programa que substitua o “;” da entrada abaixo por “,”, utilizando o comando “replace”. 
Exemplo: Entrada: 1;Maria;1000

Saída: 1,Maria,1000
"""

entrada = '1;Maria;1000'

com_virgula = entrada.replace(';', ',')

print(com_virgula)