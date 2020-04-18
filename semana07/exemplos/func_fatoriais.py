
def fatorial(n):
    
    if n < 0:
        return None
    else:
        f = 1
        while n != 0:
                f = f * n
                n -= 1
        return f


def fatoriais():

    rodando = True
    while rodando:
        n = int(input('Digite um número inteiro: '))
        if n < 0:
            rodando = False
        else:
            f = fatorial(n)
            print(f)
