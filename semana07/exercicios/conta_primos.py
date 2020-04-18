
def n_primos(n):

    total = 0

    while n != 1:
        i= 2
        primo = True
        while  i < n and primo:
            if n % i == 0:
                primo = False
            i += 1

        if primo:
            total += 1

        n -= 1

    return total
        
