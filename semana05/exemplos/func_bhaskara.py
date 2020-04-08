import math 

def imprime_tela_inicial():

    a = float(input('Entre com o valor de a: '))
    b = float(input('Entre com o valor de b: '))
    c = float(input('Entre com o valor de c: '))

    d = calcula_delta(a, b, c)

    imprime_raiz(a, b, d)




def calcula_delta(a, b, c):

    d = b ** 2 - 4 * a * c
    if d < 0:
        return -1
    else:
        return d

def calcula_raiz(a, b, d):

    if d >= 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        return x1
    else:
        return -1

    
def imprime_raiz(a, b, d):

    if d < 0:
        print ('Não existe raízes reais')
    else:
        if d == 0:
            x1 = calcula_raiz(a, b, d)
            print ("a raiz desta equacão é", x1)
        else:
            x1 = calcula_raiz(a, b, d)
            x2 = calcula_raiz(a, -b, d)
      
            if x1 > x2:            
                print ("as raízes da equação são", x2, "e", x1)
            else:
                print ("as raízes da equação são", x1, "e", x2)
        
        
