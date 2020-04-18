
def é_hipotenusa(n):

    i = n
    count = 0

    while i != 0:
        j = n
        while j != 0:
            if n**2 == i**2 + j**2:
                return True
            j -= 1
        i -= 1

def soma_hipotenusas(n):
    
    soma = 0
    
    while n != 0:
        if é_hipotenusa(n) == True:
            soma += n
        n -= 1

    return soma
        
