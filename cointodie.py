import random

print("how many dice rolls")

N = int(input())
def twocoinflipper():
    coinflip1 = random.randint(0,1)
    coinflip2 = random.randint(0,1)
    converterstring = str(coinflip1) + str(coinflip2)
    result = int(converterstring,2)
    return result


redo = []
result = []
for i in range(N):
    
    flip = twocoinflipper()
    if flip == 3:
        tryagain = 3
        while tryagain == 3:
            tryagain = twocoinflipper()
        redo.append(twocoinflipper())
    else:
        result.append(flip)
result.extend(redo)
print(result)
