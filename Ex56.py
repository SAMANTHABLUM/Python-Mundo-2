soma_idade = 0
homem_velho = 0
nome_homem_velho = ''
mulheres_menos_20 = 0
for c in range (1, 5):
    idade = int(input('Qual sua idade? '))
    nome = str(input('Qual seu nome? ')).strip().upper()
    sexo = str(input('M/F: ')).strip().upper()

    soma_idade += idade

    if sexo == 'M':     # verifica se é homem e mais velho
        if idade > homem_velho:
            homem_velho = idade
            nome_homem_velho = nome

    if sexo == 'F' and idade < 20:     # verifica se é mulher com menos de 20
        mulheres_menos_20 += 1

media_idade = soma_idade / 4

print('A medida de idade é {}'.format(media_idade))
if nome_homem_velho != '':
    print('O homem mais velho é {}'.format(nome_homem_velho))
else:
    print('Não encontrado nenhum homem')
print('São {} mulheres com menos de 20 anos'.format(mulheres_menos_20))