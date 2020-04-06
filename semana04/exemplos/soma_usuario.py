tamanho = int(input("Entre com o tamanho da sequência de valores: "))
i = 0
soma = 0
valor = 1

while i < tamanho:
    valor = int(input("Digite um valor a ser somado: "))
    soma += valor
    i += 1

print("A soma dos valores digitados é: ", soma)
