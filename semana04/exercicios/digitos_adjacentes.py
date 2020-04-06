n = int(input('Digite um número inteiro: '))
adjacente = False

while n != 0 and not adjacente:
    r = n % 10
    n = n // 10
    if r == n % 10:
        adjacente = True

if adjacente:
    print ('sim')
else:
    print ('não')

        
