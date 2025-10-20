n = s = c = 0
while True:
    n = int(input('Digite um numero [digite 999 para sair]: '))
    if n == 999:
        break
    s += n # s = s + n
    c += 1 # c = c + 1
print(f'Foi digitado {c} e a soma foi {s}.')