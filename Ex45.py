import random # importado biblioteca random que serve para sortear algo aleatorio
from time import sleep
print('Vamos jogar JOKÊNPO!!!')
sleep(2)
print('Escolha pedra, papel ou tesoura e que vença o melhor!!!')
sleep(2)
opcoes = ['pedra', 'papel', 'tesoura']

while True: #começar o loop do jogo
    computador = random.choice(opcoes)  # random.choice() para que ele leia uma lista, no caso a lista opções que eu coloquei
    #COLOCAR O COMPUTADOR DENTRO DO LOOP PARA QUE ELE SEMPRE FAÇA UMA ESCOLHA DIFERENTE ATE O JOGADOR ACERTAR
    jogador = input('Diga sua escolha: ').lower() #lower para aceitar maisculo e minusculo
    if jogador == computador:
        print('EMPATE')
    elif jogador == 'pedra' and computador == 'tesoura':
        print('Pedra GANHA de tesoura, você venceu!')
    elif jogador == 'papel' and computador == 'pedra':
        print('Papel GANHA de pedra, você venceu!')
    elif jogador == 'tesoura' and computador == 'papel':
        print('Tesoura GANHA de papel, você venceu')
    else:
        print('Computador VENCEU!')
        break # ENCERRAR O LOOP ASSIM QUE O COMPUTADOR VENCER
