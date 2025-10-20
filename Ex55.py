primeiro_p = float(input('Qual é o peso da 1 pessoa? '))
peso_maior = primeiro_p
peso_menor = primeiro_p
for c in range(2, 6):
    p = float(input('Qual é o peso da {} pessoa? '.format(c)))
    if p > peso_maior:
     peso_maior = p
    if p < peso_menor:
        peso_menor = p
print('O maior peso lido foi {} Kg'.format(peso_maior))
print('O menor peso lido foi {} Kg'.format(peso_menor))