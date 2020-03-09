import random

maxVal = 2

def creerListe(nVal: int) -> list:
	#Génère une liste de nVal éléments
	lNb = random.choices(range(maxVal), k = nVal)
	
	#A adapter pour obtenir des couleurs.
	
	return lNb
	
def couleurs2(L: list) -> list:
	Lo = 0
	Hi = len(L)-1
	while Lo <= Hi:
		
		if L[Lo] == 0:
			Lo +=1
		else:
			L[Hi], L[Lo] = L[Lo], L[Hi]
			Hi -=1
		print(L)
	return L
	
	
	
	return
	
	
def couleurs3(L: list) -> list:
	return
	
#Génère une liste de 10 éléments
print(creerListe(10))
