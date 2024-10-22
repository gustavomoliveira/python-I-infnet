""" 
15 - Crie um programa que apresente ao usuário uma série de escolhas
(como em uma história) e conduza a diferentes resultados com base nessas escolhas.
 """

# HISTÓRIA GERADA POR PROMPT NO CHAT GPT. Iria levar uma semana nesse exercício se tivesse que criar uma história... :)
# Criei um arquivo .txt com uma ideia de roteiro e algumas condições. Peguei a base dos textos gerados para montar a sequência de história.
# No programa criado, 2 escolhas diferentes determinam o final da história: O personagem escolhido e o Ato 4. Optei por deixar mais simples
# porque estava ficando extremamente complexo da forma que havia estruturado inicialmente, mas tudo finciona conforme esperado.


# O usuário começa a história escolhendo seu personagem
def escolher_personagem():
    print(f"""
Seja bem-vindo(a) a nossa história!
Daqui em diante você escolherá os rumos que essa jornada irá tomar.
Preparado(a)? Vamos começar!
          
“A Última Fronteira”
No ano de 2275, a Terra já não é habitável. A nave Prometheus busca um novo lar para a humanidade,
enfrentando o desconhecido. A bordo, quatro tripulantes, cada um com habilidades únicas, serão testados em
decisões críticas que determinarão o futuro da missão.
Os personagens são:
[1] - Capitã Zara Reyes – A líder estratégica da missão.
[2] - Dr. Elias Voss – Cientista especialista em ecossistemas alienígenas.
[3] - Tenente Kai Nakamura – Ex-soldado, responsável pela segurança da equipe.
[4] - Engenheira Ava Laurent – Responsável pela manutenção da nave e soluções técnicas.
        """)
    
    personagens = {
                1: 'Capitã Zara Reyes',
                2: 'Dr. Elias Voss',
                3: 'Tenente Kai Nakamura',
                4: 'Engenheira Ava Laurent'
            }
    
    while True:
        try:
            input_usuario = int(input('Quem você escolhe? Digite o número correspondente: '))
            if input_usuario in personagens:
                return personagens.get(input_usuario), input_usuario
            else:
                print('Erro: escolha um personagem entre 1 e 4.')
        except ValueError:
            print('Erro: insira um número válido.')

# Ato 1
def ato_1():
    print(f""" 
Durante a exploração do espaço profundo, a Prometheus intercepta um sinal de socorro
vindo de um planeta desconhecido. A tripulação discute sobre o que fazer.
O tempo é limitado, e a decisão precisa ser tomada rapidamente.
As escolhas são:
[1] - Investigar o sinal e pousar no planeta para ajudar.
[2] - Ignorar o sinal e continuar em busca de um planeta habitável.
[3] - Enviar uma sonda para investigar o sinal de longe.
[4] - Desconectar o sinal, isolando a nave de qualquer comunicação externa temporariamente.
""")
    return verifica_input()

# Função que recebe input e determina escolha do Ato 1
def escolhas_ato_1():
    escolha_ato_1 = ato_1()
    if escolha_ato_1 == 1:
        print(f""" 
O planeta revela uma colônia humana abandonada com sinais de vida alienígena.
A equipe deve decidir entre tentar contato ou fugir rapidamente.
""")
    elif escolha_ato_1 == 2:
        print(f""" 
A nave avança na missão, mas logo é atacada por piratas espaciais,
forçando um combate intenso para defender a nave.
""")
    elif escolha_ato_1 == 3:
        print(f""" 
A sonda transmite dados confusos, revelando interferências incomuns.
A equipe deve lidar com sistemas instáveis e falhas críticas na nave.
""")
    else:
        print(f"""
Ao desligar as comunicações, a nave perde a capacidade de receber sinais de socorro por um tempo.
Isso dá à equipe mais controle, mas eles ficam cegos a novas informações.
""")

# Ato 2
def ato_2():
    print(f"""
Após uma decisão difícil sobre o sinal, a nave se aproxima de um planeta promissor.
No entanto, uma tempestade de energia cósmica se aproxima rapidamente,
ameaçando destruir os sistemas da nave.
As escolhas são:
[1] - Pousar imediatamente no planeta, buscando refúgio.
[2] - Manter a nave em órbita e esperar a tempestade passar.
[3] - Desviar da tempestade e explorar outra rota espacial.
[4] - Tentar atravessar a tempestade diretamente para continuar a missão sem atraso.
""")
    return verifica_input()

# Função que recebe input e determina escolha do Ato 2
def escolhas_ato_2():
    escolha_ato_2 = ato_2()
    if escolha_ato_2 == 1:
        print(f"""
A tempestade compromete o pouso, e a equipe é forçada
a improvisar para sobreviver em um ambiente hostil e desconhecido.
""")
    elif escolha_ato_2 == 2:
        print(f"""
A tempestade danifica gravemente os sistemas de suporte de vida da nave,
colocando a tripulação em risco enquanto tentam realizar os reparos.
""")
    elif escolha_ato_2 == 3:
        print(f"""
A nave evita a tempestade, mas consome combustível crítico,
limitando as futuras opções de exploração.
""")
    else:
        print(f"""
A nave sofre danos graves. Agora, vocês precisam decidir entre buscar
refúgio em um planeta próximo ou tentar reparos em pleno espaço.
""")

# Ato 3
def ato_3():
    print(f"""
Uma mensagem criptografada é interceptada, revelando que um dos tripulantes
pode estar trabalhando secretamente com uma facção rebelde.
O traidor pode sabotar a missão a qualquer momento. Como você reage?
[1] - Confiar em seus colegas e descartar a mensagem como um engano ou falsificação.
[2] - Confrontar a tripulação e exigir explicações, gerando tensão.
[3] - Investigar secretamente e tentar descobrir a identidade do traidor sozinho.
[4] - Enviar um alerta à Terra sobre a possibilidade de traição, apesar da falta de provas sólidas.
""")
    return verifica_input()

# Função que recebe input e determina escolha do Ato 3
def escolhas_ato_3():
    escolha_ato_3 = ato_3()
    if escolha_ato_3 == 1:
        print(f"""
A confiança se mantém, mas o traidor age nas sombras,
comprometendo a segurança da missão no momento mais crítico.
""")
    if escolha_ato_3 == 2:
        print(f"""
A desconfiança aumenta entre todos, e a tripulação se divide,
o que prejudica as operações da missão e causa conflitos.
""")
    if escolha_ato_3 == 3:
        print(f"""
Você coleta pistas, mas corre o risco de ser descoberto
antes de identificar o verdadeiro culpado, aumentando as chances de sabotagem.
""")
    else:
        print(f"""
A comunicação com a Terra aciona um protocolo emergencial que
limita sua autonomia na missão, prejudicando suas decisões futuras.
""")

# Ato 4
def ato_4():
    print(f"""
Após enfrentar diversos desafios, a nave está gravemente danificada, e os recursos estão se esgotando.
Para garantir a sobrevivência do resto da tripulação, alguém precisa ficar para trás em um planeta
instável enquanto os outros escapam. Quem ficará para trás?
[1] - Capitã Zara Reyes
[2] - Dr. Elias Voss
[3] - Tenente Kai Nakamura
[4] - Engenheira Ava Laurent
""")
    return verifica_input()

# O final que é influenciado pelas escolhas do personagem e do Ato 4.
def o_fim(personagem_escolhido, escolha_final):
    if personagem_escolhido == 1:
        if escolha_final == 1:
            print("Capitã Zara Reyes se sacrificou para salvar a missão. A tripulação sobrevive, mas a moral está profundamente abalada.")
        else:
            print("A missão continua com sucesso sob o comando de Zara. Sua liderança firme garante o sucesso da missão.")
    elif personagem_escolhido == 2:
        if escolha_final == 2:
            print("Dr. Elias Voss ficou para trás, levando consigo descobertas vitais. A humanidade perde seu conhecimento, mas a tripulação sobrevive.")
        else:
            print("Elias conduz a equipe a grandes descobertas científicas, garantindo a colonização de um novo planeta.")
    elif personagem_escolhido == 3:
        if escolha_final == 3:
            print("Tenente Kai Nakamura se sacrificou heroicamente. A tripulação sobrevive, mas fica vulnerável sem seu protetor.")
        else:
            print("Kai usa suas habilidades de combate para proteger a tripulação, garantindo o sucesso da missão.")
    elif personagem_escolhido == 4:
        if escolha_final == 4:
            print("Engenheira Ava Laurent fez um sacrifício nobre, garantindo que todos os sistemas continuassem funcionando.")
        else:
            print("Graças às habilidades de Ava, a nave continua operacional e a tripulação pode seguir com a missão.")
    else:
        print("Final inesperado. O destino da nave é incerto.")

# Função de validação de escolhas do usuário
def verifica_input():
    while True:
        try:
            input_usuario = int(input('O que você deseja fazer? Digite o número correspondente de uma das 4 opções: '))
            if input_usuario >=1 and input_usuario <= 4:
                return input_usuario
            else:
                print('Erro: escolha uma opção: 1, 2, 3 ou 4.')
        except ValueError:
            print('Erro: insira um número válido.')
    
# Função que inicia a história
def iniciar_historia():
    personagem, personagem_escolhido = escolher_personagem()
    print(f'Você escolheu {personagem}. Bem-vindo à bordo!')

    # Ato 1:
    escolhas_ato_1()

    # Ato 2:
    escolhas_ato_2()

     #Ato 3:   
    escolhas_ato_3()

    #Ato 4:
    escolha_ato_4 = ato_4()

    # O fim:
    o_fim(personagem_escolhido, escolha_ato_4)

iniciar_historia()