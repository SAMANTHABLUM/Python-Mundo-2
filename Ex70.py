print('{:-^40}'.format(' MERCADO DIVERSO ')) # jeito para ficar a palavra centralizada entre os traços
total_gasto = 0
quant_caro = 0
nome_barato = ''
preco_barato = 0
primeiro_produto = True
while True:
    produto = str(input('Nome do produto: '))
    valor = float(input('Qual o valor: R$'))

    total_gasto += valor
    if valor >= 1000: #descobrir qual custa mais de R$1.000,00
        quant_caro += 1
    if primeiro_produto or valor < preco_barato: # descobrir o produto mais barato
        preco_barato = valor
        nome_barato = produto
        primeiro_produto = False
    continuar = ' ' # NAO ESQUECER DO ESPAÇO - LINHA NECESSARIA PARA QUE SÓ SEJA ACEITO S/N
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total gasto foi: {total_gasto:.2f}')
print(f'{quant_caro} produtos custam mais de R$1.000,00')
print(f'{nome_barato} é o produto mais barato custando {preco_barato:.2f}')