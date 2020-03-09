##----- Importation des Modules -----##
from tkinter import *

##----- Création de la fenêtre -----##
fen = Tk()
fen.title('Tracer dans un canevas')


##----- Création des boutons -----##
bouton_quitter = Button(fen, text='Quitter', command=fen.destroy)
bouton_quitter.grid(row = 1, column = 1, padx = 3, pady = 3, sticky=E)


##----- Création du canevas -----##
dessin = Canvas(fen, width = 500, height = 400, bg = 'white')
dessin.grid(row = 0, column = 0, columnspan = 2, padx = 3, pady = 3)


##----- Dessiner dans le canevas -----##
dessin.create_line(0, 20, 250, 46, width = 4, fill = "purple")
dessin.create_line(10, 250, 250, 250, width = 4, fill = "pink")
dessin.create_rectangle(100, 100, 25, 25, fill = "yellow", outline = "green")
dessin.create_oval(81, 69, 420, 126, width = 37, fill = "gold", outline =  "purple")
dessin.create_text(250, 95, text = "C'est trés moche... désolée monsieur")




centre = (200, 200)

for R in range(50, 0, -10):
	cercle=dessin.create_oval(centre[0]-R, centre[1]-R, centre[0]+R, centre[1]+R, width = 3, fill= "purple", outline = "black")
print(type(centre))



def change_color(event):
	dessin.itemconfigure(cercle, fill="pink")

def change_color2(event):
	dessin.itemconfigure(cercle, fill="blue")

fen.bind('<a>',change_color)
fen.bind('<b>',change_color2)

#def create_triangle (A,B,C):
	#dessin.create_line()
fen.bind('<Enter>',change_color)
fen.bind('<Leave>',change_color2)



##----- Programme principal -----##
fen.mainloop()                    # Boucle d'attente des événements
