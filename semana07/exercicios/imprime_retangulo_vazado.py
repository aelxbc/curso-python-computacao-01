largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))

i = 0

while i < altura:
    j = 0
    while j < largura:
        if j == 0 or i == 0 or j == largura-1 or i == altura-1:
            print('#', end = '')
        else:
            print(' ', end = '')
        j += 1
    print()
    i += 1
