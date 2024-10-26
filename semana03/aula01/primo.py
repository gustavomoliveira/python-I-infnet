""" Número Primo """

def verificar_primo(num):
    div = 2
    primo = True
    while (primo) and (div < num - 1):
        if num % div == 0:
            primo = False
        else:
            div += 1
    return primo

def verificar_primo2(num):
    primo = True
    for div in range(2, num):
        if num % div == 0:
            primo = False
            break
    return primo

num = 5

primo = verificar_primo2(num)
print(primo)


