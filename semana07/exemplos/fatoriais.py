
rodando = True
while rodando:
    fatorial = 1 
    n = int(input('Digite um número inteiro: '))
    if n < 0:
        rodando = False
    else:  
        while n != 0:
            fatorial = fatorial * n
            n -= 1
        print(fatorial)


        
