x = int(input('digite a largura: '))
y = int(input('digite a altura: '))

i = 0

while i < y:
    j = 0
    while j < x:
        print('#', end = '')
        j += 1
    print ()
    i += 1
