import tkinter as tk 

LARGEUR = 500
HAUTEUR = 500

racine = tk.Tk()  #permet d'ouvrir l'interface graphique

canvas = tk.Canvas(racine, bg = "pink", width = LARGEUR, height = HAUTEUR) #Défini la taille et couleur de l'interface
canvas.grid() #
canvas.create_line( (250, 0), (250, 500), fill = "white") #ligne vertival du milieu
canvas.create_line( (0, 250), (500, 250), fill = "white") #ligne horizontal du milieu
canvas.create_line( (0, 0), (500, 500), fill = "white") #axe de gauche
canvas.create_line( (0, 500), (500, 0), fill = "white") #axe de droite
canvas.create_oval( (0 , 0 ), (0 + 20, 0 + 20), fill = "black") #point haut gauche
canvas.create_oval( (500 , 0 ), ( 500 - 20 , 0 + 20 ), fill = "red") #Point haut droit 

racine.mainloop()




