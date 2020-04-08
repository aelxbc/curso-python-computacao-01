
def fatorial(n):

    fat = 1

    if n != 0:
        while (n > 1):
            fat = fat * n
            n = n - 1
        return  fat
    else:
        return fat

def testa_fatorial():

    if fatorial(1) == 1:
        print("Funciona para 1")
    else:
        print("Não funciona pra 1")
        
    if fatorial(2) == 2:
        print("Funciona para 2")
    else:
        print("Não funciona pra 2")

    if fatorial(0) == 1:
        print("Funciona para 0")
    else:
        print("Não funciona pra 0")

    if fatorial(5) == 120:
        print("Funciona para 5")
    else:
        print("Não funciona pra 5")

def numero_binomial(n, k):

    if k == 0 or k == n:
        return 1
    else:
        if  k == 1:
            return n
        else:
            return fatorial(n) // ( fatorial(k) * fatorial(n-k) )
