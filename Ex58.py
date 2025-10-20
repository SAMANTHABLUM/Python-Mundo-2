from random import randint
from time import sleep
computador = randint (0, 10)
palpite = 0
jogador = -1
print('VAMOS JOGAR!!')
sleep(2)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
sleep(2)
while computador != jogador:
    palpite += 1
    jogador = int(input('Em que número eu pensei? '))
    print('PROCESSANDO...')
    if computador != jogador:
        print('ERROU, tente novamente')
print('Você acertou o numero {}, depois de {} palpites.'.format(computador,palpite))