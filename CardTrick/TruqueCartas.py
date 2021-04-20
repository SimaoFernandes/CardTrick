import criaCartas
import baralhar
import printBaralho
import escolha

cartas = criaCartas.criar()
cartasBaralhadas = baralhar.baralhar(cartas)
cartas21 = baralhar.cartas21(cartasBaralhadas)
listaCartas = baralhar.colums(cartas21)
printBaralho.printBaralho(listaCartas)

choice = escolha.choice()
baralhoChoice1 = escolha.joinChoice(choice, listaCartas)
baralhoChoice1 = baralhar.baralharChoice(baralhoChoice1)
printBaralho.printBaralho(baralhoChoice1)

choice = escolha.choice()
baralhoChoice2 = escolha.joinChoice(choice, baralhoChoice1)
baralhoChoice2 = baralhar.baralharChoice(baralhoChoice2)
printBaralho.printBaralho(baralhoChoice2)

choice = escolha.choice()
baralhoChoice3 = escolha.joinChoice(choice, baralhoChoice2)
resultado = escolha.resultado(baralhoChoice3)
print(resultado)