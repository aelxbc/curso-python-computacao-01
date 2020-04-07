def primo(n):
    i= 2
    primo = True
    
    while  i < n and primo:
        if n % i == 0:
            primo = False
        i += 1
    if primo:
        return n
    else:
        return 0

def maior_primo(p):

    while p != 0:
        if p == primo(p):
            return p
            break
        else:
            p -= 1


        
    

       
    


   
    
