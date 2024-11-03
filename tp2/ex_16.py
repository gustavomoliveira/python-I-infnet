"""
16 - A partir do programa anterior (Cálculo de Médias de Alunos),
utilize DocStrings para documentar seu código.
"""

def validar_nome(txt):
    """
    Valida que 'nome' receba apenas caracteres alfabéticos e
    aceite espaços para o caso de strings compostas, por exemplo.

    Parâmetro:
    - txt (str): A inserção por input() do usuário.

    Retorno:
    - str: Resultado validado da inserção do usuário.
    """
    while True:
        nome = input(txt)
        if all(letra.isalpha() or letra.isspace() for letra in nome):
            return nome
        else:
            print('ERRO: Digite apenas letras/caracteres.')

def validar_nota(txt):
    """
    Valida que 'nota' receba um número de ponto flutuante e
    que o mesmo seja maior ou igual a 0 e menor ou igual a 10.

    Parâmetros:
    - txt (str): A inserção via input() do usuário.

    Retorno:
    - float: Resultado validado da inserção do usuário.
    """
    while True:
        try:
            nota = float(input(txt))
            if 0 <= nota <= 10:
                return nota
        except ValueError:
            print('ERRO: Digite apenas números.')

def entrar_dados():
    """
    Entrada de dados, em loop, do programa.

    Os dados já foram validados de acordo com as regras de input() para 'nome', 'nota1' e 'nota2'.

    O loop é encerrado caso o usuário insira a string 'FIM' no campo 'nome.'

    As entradas são armazenadas em uma lista 'turma'.

    Retorno:
    - []: Lista aninhada de outras listas correspondentes aos dados inseridos.
    """
    turma = []
    while True:
        nome = validar_nome('Digite o nome do aluno (ou "FIM" para encerrar): ').upper()
        if nome == 'FIM':
            print('Entrada de dados encerrada.')
            print()
            break
        else:
            nota1 = validar_nota('Digite a primeira nota: ')
            nota2 = validar_nota('Digite a segunda nota: ')
            aluno = [nome, nota1, nota2]
            turma.append(aluno)
    return turma

def calcular_media(turma):
    """
    Calcula a média entre duas notas para cada aluno.

    Parâmetro:
    - []: Lista aninhada de outras listas com dados de 'aluno', 'nota1' e 'nota2'.

    Retorna:
    - []: Lista aninhada de outras listas correspondentes a 'aluno' e 'media'.
    """
    alunos_e_medias = []
    for aluno in turma:
        soma = aluno[1] + aluno[2]
        media = soma / 2
        aluno_e_media = [aluno[0], media]
        alunos_e_medias.append(aluno_e_media)
    return alunos_e_medias

def exibir_aluno_e_media(alunos_e_medias):
    """
    Exibe a relação entre 'aluno' e 'media' correspondentes.

    Parâmetros:
    - []: Lista aninhada de outras listas com dados de 'aluno' e 'media'.
    """
    for item in alunos_e_medias:
        print(f'{item[0].title()} possui média {round(item[1], 2)}.')
    print()

def exibir_aprovação(medias):
    """
    Exibe 'aluno' e 'media' e cria condição necessária para status de aprovação ou não.

    Parâmetros:
    - []: Lista aninhada de outras listas com dados de 'aluno' e 'media'.
    """
    for media in medias:
        if media[1] >= 6:
            print(f'{media[0].title()} está APROVADO(A) com média {round(media[1], 2)}')
        else:
            print(f'{media[0].title()} está EM PROVA FINAL com média {round(media[1], 2)}')
    print()

def calcular_media_turma(alunos_e_medias):
    """
    Calcula a média total entre todos os alunos.

    Parâmetros:
    - []: Lista aninhada de outras listas com dados de 'aluno' e 'media'.

    Retorna:
    - float: Resultado da média entre todos os alunos.
    """
    soma_medias = 0
    for aluno in alunos_e_medias:
        soma_medias += aluno[1]

    media_turma = soma_medias / len(alunos_e_medias)
    return media_turma
    
turma = entrar_dados()
alunos_e_medias = calcular_media(turma)
exibir_aluno_e_media(alunos_e_medias)
exibir_aprovação(alunos_e_medias)
media_turma = calcular_media_turma(alunos_e_medias)
print(f'A média geral da turma é {round(media_turma, 2)}')
print()