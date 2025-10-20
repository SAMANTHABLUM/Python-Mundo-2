from random import randint # da biblioteca random foi importada apenas o randint que escolhe números aleatórios
from time import sleep # da biblioteca time foi importada apenas o sleep que dá delay entre as msgs
print('Vamos brincar!!!')
sleep(1) # delay de 1 segundo
print('Estou pensando em um número entre 0 e 10, tente adivinhar!!')
sleep(1)
computador = randint(0, 10) # os números usados para limitar entre 0 e 10
tentativas = 0 # é uma variável para iniciar o jogo do zero e ir somando conforme o jogador tenta adivinhar
while True: # cria um loop infinito que só para no break quando o jogador acertar o número
   jogador = int(input('Qual é seu palpite? '))
   tentativas += 1 #aqui soma as tentativas do jogador para dizer no final
   if jogador == computador:
       print('PARABÉNS! Você conseguiu acertar!!!')
       break  # Sai do loop
   elif jogador < computador: #aqui usando o menor < o jogo avisa que o jogador precisa falar um numero maior
       print('ERROOOOUUUU!!! Tente um número maior.')
   else: #aqui ele avisa o jogador para usar um número menor
       print('ERROOOOUUUU!!! Tente um número menor.')
print(f'Você acertou em {tentativas} tentativas!')