# -*- coding: utf-8 -*-


# ----- IMPORT MODULE -----

from tkinter import *


# ----- PIRATE -----
def dessine_pirate(can):

    #oreilles
    can.create_oval(230,160,250,180, width=3,outline='peach puff',fill='peach puff2')
    can.create_oval(390,160,410,180, width=3,outline='peach puff',fill='peach puff2')
    
    #pistolet
    can.create_oval(510,150,530,170, width=3,outline='saddle brown',fill='saddle brown')
    can.create_line(560,120,520,160, width=20,fill='grey60')
    can.create_line(510,210,518,160, width=20,fill='saddle brown')
    can.create_line(550,140,510,180, width=10,fill='saddle brown')
    
    #main
    can.create_oval(480,170,520,210, width=3,outline='peach puff',fill='peach puff')
    can.create_oval(150,370,190,410, width=3,outline='peach puff',fill='peach puff')
    
    #bras
    can.create_line(500,190,280,340, width=45,fill='OrangeRed4')
    can.create_line(170,390,255,250, width=45,fill='OrangeRed4')
    
    #torse
    can.create_rectangle(240,240,400,380, width=2,outline='OrangeRed4',fill='OrangeRed4')
    can.create_rectangle(280,240,360,380, width=2,outline='white smoke',fill='white smoke')
    can.create_rectangle(240,380,400,410, width=2,outline='saddle brown',fill='saddle brown')
    can.create_rectangle(240,410,400,440, width=2,outline='slate gray',fill='slate gray')
    can.create_rectangle(240,410,305,540, width=2,outline='slate gray',fill='slate gray')
    can.create_rectangle(335,410,400,540, width=2,outline='slate gray',fill='slate gray')
    
    #cou
    can.create_line(320,230,320,250, width=40,fill='peach puff')
    can.create_oval(295,200,345,260, outline='peach puff',fill='peach puff')
    can.create_oval(290,200,350,250, outline='peach puff2',fill='peach puff2')
    
    #un cercle pour la tete
    can.create_oval(240,80,400,240, outline='peach puff',fill='peach puff')
    can.create_oval(295,200,345,235, width=3,outline='peach puff3',fill='peach puff3')
    
    #botes
    can.create_rectangle(235,540,310,580, width=2,outline='grey3',fill='grey3')
    can.create_rectangle(240,540,305,630, width=2,outline='grey3',fill='grey3')
    can.create_oval(210,585,290,631, outline='grey3',fill='grey3')
    can.create_arc(405,580,330,500, extent=-180, width=2,outline='salmon4',fill='salmon4')
    can.create_line(367,560,367,630, width=10,fill='salmon4')
    
    #un cercle pour la bouche
    can.create_oval(300,180,340,220, outline='grey3',fill='grey2')
    can.create_oval(360,210,280,160, outline='peach puff',fill='peach puff')
    can.create_oval(329,220,311,215, outline='red',fill='red')
    
    #les yeux
    can.create_oval(340,160,360,180, outline='grey3',fill='grey2')
    can.create_oval(265,155,305,185, outline='grey3',fill='grey2')
    can.create_line(310,130,290,160, width=6,fill='grey3')
    can.create_line(243,185,280,170, width=6,fill='grey3')

    #nez
    can.create_oval(315,180,328,200, width=3,outline='peach puff',fill='peach puff2')
    
    #chapeau
    can.create_rectangle(200,100,440,140, width=2,outline='grey2',fill='grey2')
    can.create_arc(228,50,412,230, extent=180, width=2,outline='grey2',fill='grey2')
    can.create_rectangle(200,100,440,140, width=2,outline='grey2',fill='grey2')
    can.create_oval(120,20,240,140, outline='light blue',fill='light blue')
    can.create_oval(400,20,520,140, outline='light blue',fill='light blue')
    
    #crane
    can.create_oval(300,80,340,120, outline='ivory2',fill='ivory2')
    can.create_rectangle(310,100,330,125, width=2,outline='ivory2',fill='ivory2')
    can.create_line(295,75,345,125, width=6,fill='ivory2')
    can.create_line(345,75,295,125, width=6,fill='ivory2')
    can.create_oval(325,90,335,110, outline='black',fill='black')
    can.create_oval(315,90,305,110, outline='black',fill='black')
    