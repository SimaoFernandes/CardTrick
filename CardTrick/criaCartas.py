def criar():
    cartas = ['2','3','4','5','6','7','8','9','Q','J','K','A']
    naipes = ['♥','♦','♣','♠']
    ret = []
    for x in cartas:
        for y in naipes:
            ret.append(f'{x}{y}')
    return ret