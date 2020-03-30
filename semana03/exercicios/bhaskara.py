import math 

a = float(input())
b = float(input())
c = float(input())

delta = b ** 2 - 4 * a * c

if delta < 0:
    print ("esta equação não possui raízes reais")
else:
    if delta == 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        print ("a raiz desta equacão é", x1)
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)

        if x1 > x2:            
            print ("as raízes da equação são", x2, "e", x1)
        else:
            print ("as raízes da equação são", x1, "e", x2)

        
