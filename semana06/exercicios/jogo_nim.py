def computador_escolhe_jogada(n, m):

    if n % (m+1) != 0:
        return n % (m + 1)
    elif n % m == 0:
        return m
    elif n - m < 0:
        return n
    elif n % (m+1) == 0:
        return m
    

def usuario_escolhe_jogada(n, m):

    ind = False

    while not ind:

        valor = int(input('Quantas peças você vai tirar? '))

        if valor > m or valor <= 0:
            print('Oops! Jogada inválida! Tente de novo.')

        elif valor > n and valor <= m:
            print('Oops! Jogada inválida! Tente de novo.')

        else:
            if valor <= m:
                ind = True

    return valor


def jogo():

    print('Bem-vindo ao jogo do NIM! Escolha:')
    
    x = int(input('1 - para jogar uma partida isolada\n2 - para jogar um campeonato '))

    if x == 1:
        print ('Voce escolheu uma partida isolada!')
        partida()
    elif x == 2: 
        print ('Voce escolheu uma campeonato!')
        campeonato()
    else:
        boas_vindas()

    
def partida():
    
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))

    b = True

    # computador generoso
    if n % (m+1) == 0:
        print ('\nVoce começa!\n')
        j = 1
    else:
        print('\nComputador começa!\n')
        j = 2
    while True and b:

        if j == 1:
            x = usuario_escolhe_jogada(n, m)
            print('Voce tirou', x, 'peças')
            n -= x
            if n == 0:
                print('Fim do jogo! Voce ganhou!')
                b = False
                return 1
            else:
                print('Agora restam apenas', n, 'peças no tabuleiro.')

            y = computador_escolhe_jogada(n,m)
            print('Computador tirou', y, 'peças')
            n -= y
            if n == 0:
                print('Fim do jogo! O computador ganhou!')
                b = False
                return 2
                
            
        if j == 2:
            y = computador_escolhe_jogada(n, m)
            print('PC tirou', y, 'peças')
            n -= y
            if n == 0:
                print('Fim do jogo! O computador ganhou!')
                b = False
                return 2
                
            else:
                print('Agora restam apenas', n, 'peças no tabuleiro.')
                
            x = usuario_escolhe_jogada(n, m)
            print('Voce tirou', x, 'peças')
            n -= x
            if n == 0:
                print('Fim do jogo! Voce ganhou!')
                b = False
                return 1
            else:
                print('Agora restam apenas', n, 'peças no tabuleiro.')


def campeonato():
    print('\nVoce escolheu um campeonato!\n')
    i = 0
    u = 0
    c = 0
    
    while i < 3:
        print('\n**** Rodada', i+1, '****\n')
        p = partida()
        
        if p == 1:
            u += 1
        if p == 2:
            c += 1
        i += 1
        
    print('\n**** Final do campeonato! ****')
    print ('\nPlacar: Você', u, 'X', c, 'Computador')

jogo()
    
