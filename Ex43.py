print('Vamos calcular seu IMC, me informe os dados abaixo:')
peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc < 25: # Não precisa checar >= 18.5, pois o primeiro 'if' já eliminou essa possibilidade
    print('PESO IDEAL')
elif imc < 30: # Não precisa checar >= 25, pois o 'elif' anterior já eliminou
    print('SOBREPESO')
elif imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')