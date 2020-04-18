def éPrimo(n):
    i= 2
    primo = True
    while  i < n and primo:
        if n % i == 0:
            primo = False
        i += 1
        
    if primo:
        return True
    else:
        return False


n = int(input('Digite um número inteiro: '))

while n > 0:
    if éPrimo(n):
        print (n, 'é primo!')
    else:
        print(n, 'não é primo :-(')

    n = int(input('Digite um número inteiro: '))


