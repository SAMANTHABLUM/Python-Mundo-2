print('Informe suas notas e saiba o resultado do seu ANO LETIVO:')
n1 = float(input('Qual foi sua primeira nota? '))
n2 = float(input('Qual foi sua segunda nota? '))
media = (n1 + n2) / 2
if media < 5.0:
    print('REPROVADO')
elif media >= 5 and media <= 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
