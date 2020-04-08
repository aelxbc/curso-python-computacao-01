def fatorial (n):
    fat = i = 1

    if n >= 0:
        while i <= n:
            fat *= i
            i += 1
        return fat
    else:
        return 0
    
def test_fatorial0():
    assert fatorial(0) == 1

def test_fatorial1():
    assert fatorial(0) == 1

def test_fatorial_negativo():
    assert fatorial(-1) == 0

def test_fatorial4():
    assert fatorial(4) == 24

def test_fatorial0():
    assert fatorial(5) == 120
                    

