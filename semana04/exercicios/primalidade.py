n = int(input("Digite o valor de n: "))
i= 2
primo = True

while  i < n and primo:
    if n % i == 0:
        primo = False
    i += 1

if primo:
    print ('primo')
else:
    print ('não primo')
