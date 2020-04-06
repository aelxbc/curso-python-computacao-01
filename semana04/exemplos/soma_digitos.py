numero = int(input("Entre com um número: "))
soma = 0

while numero != 0:
    resto = numero % 10
    soma = soma + resto
    numero = numero // 10

print("A soma dos digítos é:", soma)
