import math 

a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))
c = float(input("Entre com o valor de c: "))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print ("Não existe raízes reais")
else:
    if delta == 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        print ("A única raíz é: ", x1)
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print ("A primeira raíz é:", x1)
        print ("A segunda raíz é:", x2)

        
