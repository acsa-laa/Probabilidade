from random import randint

def probabilidade(quantidade):
	lista = [0,0,0,0,0,0]

	for p in range(0,quantidade):
		escolha = (randint(1,6))
		for i in range(0,6):
			if escolha == i+1:
				lista[i] = lista[i] + 1
	for x in range(0,6):
		print ((x+1),lista[x]) 
		prob = (lista[x]/float(quantidade))
		print('probabilidade', prob)

print('Para 10 vezes:')
probabilidade(10)
print('Para 100 vezes:')
probabilidade(100)
print('Para 100000 vezes:')
probabilidade(100000)
print('Para 1000000 vezes:')
probabilidade(1000000)