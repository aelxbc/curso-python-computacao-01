n = int(input("Digite o valor de n: "))

fatorial = 1

if n != 0:
    while n != 0:
        fatorial = fatorial * n
        n = n - 1
    print (fatorial)
else:
    print (fatorial)
