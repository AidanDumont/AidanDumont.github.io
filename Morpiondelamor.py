lun = [1, 0, 1]
lde = [0, 0, 0]
ltroa = [1, 1, 1]
gry = [lun, lde, ltroa]
#gry = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

def affichage(tableau:list):
    n = len(tableau)
    for i in range(n):
        print(tableau[i])
def demande (numJou : int)->list:
    if numJou == 1:
        print("o tor du jeur 1")
    else:
        print("o tor du jeur 2")
    rigne, coronnu = input("rigne, coronnu").split(",")
    return [int(rigne), int(coronnu)]

def verf(tableau : list)->int:
    sommes=[0,0,0,0,0,0,0,0]
    #grille[0]=lun grille[1]=lde grille[2]=ltroa if sum(grille[0]):
    #lignes
    sommes[0] = tableau[0][0] + tableau[0][1] + tableau [0][2]
    sommes[1] = tableau[1][0] + tableau[1][1] + tableau [1][2]
    sommes[2] = tableau[2][0] + tableau[2][1] + tableau [2][2]
    #colonnes
    sommes[3] = tableau[0][0] + tableau[1][0] + tableau [2][0]
    sommes[4] = tableau[0][1] + tableau[1][1] + tableau [2][1]
    sommes[5] = tableau[0][2] + tableau[1][2] + tableau [2][2]
    #diagonales
    sommes[6] = tableau[0][0] + tableau[1][1] + tableau [2][2]
    sommes[7] = tableau[0][2] + tableau[1][1] + tableau [2][0]
    for element in sommes :
        if element ==3: return 1
        elif element == -3: return -1
    return 0






def play():
    gry =[[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

    joueur = 1
    gagner = verf(gry)
    while (gagner != "X" or gagner != "O"):
        rigne, coronnu = demande(joueur)
        gry [rigne][coronnu] = joueur
        affichage(gry)
        gagner = verf(gry)
        if gagner == "X": print ("Jeur1 a gane")
        elif gagner == "O": print("Jeur2 a gane")
        joueur = -joueur


winner = play()
print(winner)
