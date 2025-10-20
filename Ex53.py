frase = input("Digite uma frase: ").strip().lower()  # remove espaços extras e coloca em minúsculo
frase_limpa = frase.replace(" ", "")  # tira todos os espaços
inversa = frase_limpa[::-1]  # inverte a string
if frase_limpa == inversa:
    print("É um PALÍNDROMO!")
else:
    print("NÃO é um palíndromo.")