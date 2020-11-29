<<<<<<< HEAD
# -*- coding: utf-8 -*-


# ----- IMPORT MODULES / FICHIER -----

from tkinter import *
import random
from pip import *
import pirate


# ----- POISSON -----

choix_poisson=0

def pecher(event):
    global x,y,dx,dy,choix_poisson,couleur
    choix_poisson=random.randint(0,1)
    # couleur = random.choice(coul)
    ferrer.config(text='férrer')
    can.delete(ALL)
    
    print('del - pecher')
    
    x=event.x
    y=event.y
    poisson(x,y)
    dx,dy=(x - x_main)/(-100),(y - y_main)/(-100)
    # poisson(x,y)
    pirate.dessine_pirate(can)

def poisson(x,y):
    if choix_poisson==0:
        can.delete(ALL)
        
        print('del - poisson1')
        
        can.create_line(x_main-60,y_main-60,x_main+30,y_main+30,width=5)
        can.create_line(x_main-60,y_main-60,x,y)
        can.create_polygon((105+x, 5+y),(105+x, -35+y),(145+x, 5+y), width=2,outline='black',fill='grey')
        can.create_arc(0+x,-45+y,110+x,45+y, extent=180, start=180, width=2,outline='black',fill='grey')
        can.create_arc(100+x,35+y,50+x,-35+y, extent=90, start=90, width=2,outline='black',fill='grey')
        can.create_oval(17+x,7+y,25+x,15+y, width=2,outline='white',fill='white')
        can.create_oval(19+x,9+y,22+x,13+y, width=2,outline='black',fill='black')
        can.create_arc(11+x,15+y,40+x,36+y, width=2, extent=90, start=180, outline='black')
        balle = can.create_oval(x1,y1,x1+20,y1+10, width=2,fill=couleur)
        pirate.dessine_pirate(can)
    else:
        can.delete(ALL)
        
        print('del - poisson2')
        
        can.create_line(x_main-60,y_main-60,x_main+30,y_main+30,width=5)
        can.create_line(x_main-60,y_main-60,x,y)
        can.create_oval(-10+x, -70+y, 70+x, 10+y, outline='orange', fill='orange')
        can.create_arc(-10+x, -63+y, 30+x, 3+y, extent=180, start=90, outline='white', fill='white')
        can.create_rectangle(23+x, -70+y, 37+x, 10+y, fill='white', outline='white')
        can.create_arc(40+x, -60+y, 70+x, 0+y, extent=180, start=270, outline='white', fill='white')
        can.create_arc(70+x, -50+y, 90+x, -10+y, start=90, extent=180, outline='orange', fill='orange')
        can.create_oval(0+x, -50+y, 15+x, -35+y, outline='black', fill='black')
        can.create_line(0+x, 0+y, 15+x, -15+y, width=5)
        balle = can.create_oval(x1,y1,x1+20,y1+10, width=2,fill=couleur)
        pirate.dessine_pirate(can)

def remonter():
    global nb_poissons,choix_poisson
    if ferrer.cget('text')=='férrer':
        chaine.config(text=nb_poissons+1)
        nb_poissons+=1
        depl()
    ferrer.config(text='vérouillé')

def depl():
    global x,y,dx,dy
    if x<x_main-0.1 or x>x_main+0.1 :
        x=x+dx
        y=y+dy
        poisson(x,y)
        can.after(10,depl)
    else :
        can.delete(ALL)
        
        print('del - depl')
        
        balle = can.create_oval(x1,y1,x1+20,y1+10, width=2,fill=couleur)
        pirate.dessine_pirate(can)


# ----- PISTOLET -----

x1,y1 = 545,120
flag = 0
dxa = random.randint(-10,10)
dya = random.randint(-10,10)

def tirer():
    """
    Cette fonction est appellée lorsque le bouton "Tirer" est pressé.
    Elle gère le mouvement de la balle.
    """
    global flag
    global x1, y1, dxa, dya
    #print(f'Avant reload ::: x1:{x1} ; y1:{y1} ; dxa:{dxa} ; dya:{dya}')
    if flag==0: #On teste si l'objet est statique
        flag=1  #Si c'est le cas, on passe flag à 1
        print('tirer')
    x1, y1 = x1+dxa, y1+dya #On ajoute les valeurs de dx1 et dy1 respectivement à x1 eet y1
    can.coords(balle, x1, y1, x1+20, y1+10) #On modifie les coordonnées de la balle
    print("tir effectué")
    if x1 > 630 or x1 < 10 or y1 > 630 or y1 < 10: #Si la balle se trouve à moins de 10px des bords
        flag = 0 #Flag est passé à 0
        recharger()
    #print(f'Après reload ::: x1:{x1} ; y1:{y1} ; dxa:{dxa} ; dya:{dya}')
    if flag>0:  #Si l'objet est toujours en mouvement
        fen.after(50, tirer) #On rappelle la fonction tirer au bout de 50ms
        print("avance")

def recharger():
    """
    Cette fonction est appellée lorsque la balle atteint un bord.
    Cette fonction permet de recharger le pistolet en remettant la balle à ses coordonnées initiales.
    """
    global x1, y1, dxa, dya
    can.coords(balle, 545, 120, 565, 130) #On remet la balle à ses coordonnées initiales
    x1,y1 = 545,120 #On remet x1 et y1 à leurs valeurs initiales
    dxa = random.randint(-10,10) #Pareil pour dx1
    dya = random.randint(-10,10) #et dy1
    coul = ['blue','yellow','red','black','dark grey'] #On créé une liste avec les couleurs possibles pour la balle
    couleur = random.choice(coul) #On choisit une couleur aléatoire pour la balle
    can.itemconfig(balle, fill=couleur) #On met à jour la couleur de la balle
    #print(f'Après reload ::: x1:{x1} ; y1:{y1} ; dxa:{dxa} ; dya:{dya}')


# ----- INITIALISATION FENÊTRE -----

#démarrage du programme principal : construction de la fenêtre et des widgets

#variables
coul = ['blue','yellow','red','black','dark grey'] #On créé une liste avec les couleurs possibles pour la balle
x_main,y_main=170,390 #main por la pêche
couleur=coul[random.randint(0,len(coul)-1)]
# couleur = random.choice(coul) #On choisit une couleur aléatoire pour la balle
nb_poissons=0
#
fen=Tk()
fen.title("Pirate")
can=Canvas(fen,width = 640, height = 640, bg = 'light blue')
can.bind('<Button-1>', pecher)
#un clic de souris sur le canevas va déclencher l'appel à cette fonction
can.grid()
balle=can.create_oval(x1,y1,x1+20,y1+10, width=2,fill=couleur)
bou2 = Button(fen, text='Tirer', width = 8, command=tirer)
bou2.grid()
B1=Button(fen, text='Quitter', command=fen.destroy)
B1.grid()
etiquette=Label(fen, text='nb_poissons')
etiquette.grid()
ferrer=Button(fen, text='vérouillé', command=remonter)
ferrer.grid()
chaine = Label(fen,text='0')
chaine.grid()


#------PIRATE------

pirate.dessine_pirate(can)



fen.mainloop()