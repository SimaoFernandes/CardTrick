import random
def baralhar(cartas):
    random.shuffle(cartas)
    return cartas

def cartas21(cartas):
    ret = []
    for x in cartas:
        ret.append(x)
        if len(ret) == 21:
            return ret

def colums(cartas):
    a = []
    b = []
    c = []
    for x in range(len(cartas)):
        if x % 3 == 0:
            a.append(cartas[x])
        if x % 3 == 1:
            b.append(cartas[x])
        if x % 3 == 2:
            c.append(cartas[x])
    ret = [a,b,c]
    return ret

def baralharChoice(baralho):
    baralho = baralho[0] + baralho[1] + baralho[2]
    a = []
    b = []
    c = []
    for x in range(len(baralho)):
        if x % 3 == 0:
            a.append(baralho[x])
        if x % 3 == 1:
            b.append(baralho[x])
        if x % 3 == 2:
            c.append(baralho[x])
    ret = [a,b,c]
    return ret