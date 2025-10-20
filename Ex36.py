print('Olá! Você foi direcionado a essa pagina após demostrar interesse em comprar um casa. Irei fazer algumas perguntas para seguirmos: ')
casa = float(input('Qual é o valor da casa que está querendo comprar? R$ '))
salario = float(input('Qual é seu salário? R$ '))
tempo = int(input('Em quantos anos pretende pagar a casa? '))
prestacao = casa / tempo
limite = salario * 0.30
if prestacao > limite:
    print('Emprestimo negado!')
else:
    print('Emprestimo aprovado!')