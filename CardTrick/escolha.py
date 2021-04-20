def choice():
    while(True):
        choice1 = input('Escolha uma carta e introduza a linha onde ela se encontra ->')
        if choice1.isnumeric():
            if(int(choice1)<=3 and int(choice1)>=1):
                return(int(choice1))
        print('Deve ser um numero inteiro entre 1 e 3')

def joinChoice(choice, listaCartas):
    ret = []
    if choice == 1:
        ret.append(listaCartas[1])
        ret.append(listaCartas[0])
        ret.append(listaCartas[2])
    elif choice == 2:
        ret.append(listaCartas[0])
        ret.append(listaCartas[1])
        ret.append(listaCartas[2])
    elif choice == 3:
        ret.append(listaCartas[0])
        ret.append(listaCartas[2])
        ret.append(listaCartas[1])
    return ret

def resultado(baralho):
    return(f'A carta escolhida foi -> {baralho[1][3]}')