from time import sleep
print('Vamos descobrir quais são os números PARES entre 1 e 50!')
sleep(1)
for c in range (1, 51):
    if c % 2 == 0:
        print('Os numero pares são {}.'.format(c))