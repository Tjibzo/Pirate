# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 13:45:43 2020

@author: Adriana F. ; Margot V.
"""

from tkinter import *
import random



def tirer():
    """
    Cette fonction est appellée lorsque le bouton "Tirer" est pressé.
    Elle gère le mouvement de la balle.
    """
    global flag
    global x1, y1, dx, dy
    #print(f'Avant reload ::: x1:{x1} ; y1:{y1} ; dx:{dx} ; dy:{dy}')
    if flag==0: #On teste si l'objet est statique
        flag=1  #Si c'est le cas, on passe flag à 1
    x1, y1 = x1+dx, y1+dy #On ajoute les valeurs de dx et dy respectivement à x1 eet y1
    can1.coords(balle, x1, y1, x1+20, y1+10) #On modifie les coordonnées de la balle
    if x1 > 630 or x1 < 10 or y1 > 630 or y1 < 10: #Si la balle se trouve à moins de 10px des bords
        flag = 0 #Flag est passé à 0
        recharger()
    #print(f'Après reload ::: x1:{x1} ; y1:{y1} ; dx:{dx} ; dy:{dy}')
    if flag>0:  #Si l'objet est toujours en mouvement
        fen1.after(50, tirer) #On rappelle la fonction tirer au bout de 50ms

def recharger():
    """
    Cette fonction est appellée lorsque la balle atteint un bord.
    Cette fonction permet de recharger le pistolet en remettant la balle à ses coordonnées initiales.
    """
    global x1, y1, dx, dy
    can1.coords(balle, 50, 50, 70, 60) #On remet la balle à ses coordonnées initiales
    x1,y1 = 50,50 #On remet x1 et y1 à leurs valeurs initiales
    dx = randint(-10,10) #Pareil pour dx
    dy = randint(-10,10) #et dy
    coul = ['blue','yellow','red','black','dark grey'] #On créé une liste avec les couleurs possibles pour la balle
    couleur = choice(coul) #On choisit une couleur aléatoire pour la balle
    can1.itemconfig(balle, fill=couleur) #On met à jour la couleur de la balle
    #print(f'Après reload ::: x1:{x1} ; y1:{y1} ; dx:{dx} ; dy:{dy}')
    
x1,y1 = 50,50
flag = 0
dx = randint(-10,10)
dy = randint(-10,10)
coul = ['blue','yellow','red','black','dark grey'] #On créé une liste avec les couleurs possibles pour la balle
couleur = choice(coul) #On choisit une couleur aléatoire pour la balle
pistolet = can1.create_oval(x1,y1,x1+50,y1+50, width=2,fill='yellow')
balle = can1.create_oval(x1,y1,x1+20,y1+10, width=2,fill=couleur)