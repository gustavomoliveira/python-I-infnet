
def calcular_soma_e_media():   
    min = 0
    MAX = 100
    total_nums = []
    while min != MAX:
        min += 1
        total_nums.append(min)
    return total_nums

total_nums = calcular_soma_e_media()
soma = sum(total_nums)
media = soma / len(total_nums)
print(f"""
------------- SOMA ------------------------
A soma dos números entre 1 e 100 é {soma}.

------------- MÉDIA -----------------------
A média dos números entre 1 e 100 é {media}.
""")