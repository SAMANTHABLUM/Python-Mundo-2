print('='*20)
print('CADASTRE UMA PESSOA')
print('='*20)
maior_idade = 0
homem = 0
mulher_menor = 0 # posso escrever maior_idade = homem = mulher_menor = 0 / tudo igual a zero
while True:
    idade = int(input('Idade: '))
    sexo = ' ' #PRECISA SER UM ESPAÇO ENTRE ''
    while sexo not in 'MF': # JEITO PARA QUE PERGUNTE ATE A PESSOA COLOCAR A OPÇÃO CORRETA
        sexo = str(input('Sexo [F/M]: ')).upper().strip()[0]
    print('--'*10)

    if idade >= 18:
        maior_idade += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher_menor += 1
    continuar = ' ' #MESMA COISA QUE COM O SEXO
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {maior_idade}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mulher_menor} mulheres com menos de 20 anos')
