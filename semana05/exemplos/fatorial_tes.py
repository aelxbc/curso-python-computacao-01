def fatorial (n):
    fat = i = 1

    while i < n:
        fat *= 1
        i += i

    return fat

def test_fatorial0():
    assert fatorial(0) == 1

def test_fatorial1():
    assert fatorial(0) == 1

def test_fatorial_negativo():
    assert fatorial(-1_ == 0

def test_fatorial4():
    assert fatorial(4) == 24

def test_fatorial0():
    assert fatorial(5) == 120

