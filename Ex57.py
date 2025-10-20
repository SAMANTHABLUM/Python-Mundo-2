sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo [F/M]: ')).strip().upper()
    if sexo != 'M' and sexo != 'F':
        print('ERRO, digite novamente!')
print('Sexo {} registrado com sucesso!'.format(sexo))