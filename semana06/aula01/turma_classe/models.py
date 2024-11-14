""" Classe """

class Aluno():
    # construtor
    def __init__(self, nome, n1, n2):
        self.nome = nome
        self.nota1 = n1
        self.nota2 = n2
    # método da classe
    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2
    # sobrescrita para impressão
    def __str__(self):
        return f'{self.nome} {self.nota1} {self.nota2}'
    
# objeto da classe Aluno
aluno = Aluno('Gustavo', 6, 7)
print(aluno)