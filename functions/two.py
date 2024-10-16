import random

def is_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True
    
dictt = {"odd": 0, 
        "even": 0}

def generate():
    N = random.randint(0,1000)
    print(N)
    for number in range(1,N):
        if is_odd(number) == True:
            dictt['odd'] += 1
        else:
            dictt['even'] +=1
    print(dictt)
    
generate()