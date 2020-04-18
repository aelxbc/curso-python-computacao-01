import math

def calcula_delta(a, b, c):

    d = b ** 2 - 4 * a * c
    if d < 0:
        return -1
    else:
        return d

def main():

    a_ipt = float(input('Entre com o valor de a: '))
    b_ipt = float(input('Entre com o valor de b: '))
    c_ipt = float(input('Entre com o valor de c: '))

    imprime_raizes(a_ipt, b_ipt, c_ipt)

def calcula_raiz(a, b, c):

    d = calcula_delta(a, b, c)
    
    if d >= 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        return x1
    else:
        return -1

    
def imprime_raizes(a, b, c):

    d = calcula_delta(a, b, c)
    
    if d < 0:
        print ('Não existe raízes reais')
    else:
        if d == 0:
            x1 = (-b + math.sqrt(d)) / (2*a)
            print ('a raiz desta equacão é', x1)
        else:
            x1 = (-b + math.sqrt(d)) / (2*a)
            x2 = (-b - math.sqrt(d)) / (2*a)
      
            if x1 > x2:            
                print ("as raízes da equação são", x2, "e", x1)
            else:
                print ("as raízes da equação são", x1, "e", x2)
        
        
