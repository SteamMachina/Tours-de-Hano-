###############
#   Imports   #
###############
import pyglet
from pyglet import shapes
from pyglet.window import key

##############
#    Init    #
##############

#---window---#
window_lenght = 1455 # must be a multiple of 3
window_height = 500
title = "Tower Of Hanoï"
window = pyglet.window.Window(window_lenght, window_height, title)

#---bars---#
batch = pyglet.graphics.Batch()

#--- music---#
music = pyglet.resource.media('GHOST-DATA_angelic-layer.mp3', streaming=False)
music.play()

##############
#    Bars    #
##############

#---Bar 1---#
barre1a = shapes.Rectangle(270, 100,
                        15, 270,
                        color = (255, 255, 255), #blanc
                        batch = batch)
barre1b = shapes.Rectangle(100, 85, 
                        350, 15,
                        color = (255, 255, 255), #blanc
                        batch = batch)

#---Bar 2---#
barre2a = shapes.Rectangle(720, 100,
                        15, 270,
                        color = (255, 255, 255), #blanc
                        batch = batch)
barre2b = shapes.Rectangle(550, 85, 
                        350, 15,
                        color = (255, 255, 255), #blanc
                        batch = batch)

#---Bar 3---#
barre3a = shapes.Rectangle(1170, 100,
                        15, 270,
                        color = (255, 255, 255), #blanc
                        batch = batch)
barre3b = shapes.Rectangle(1000, 85, 
                        350, 15,
                        color = (255, 255, 255), #blanc
                        batch = batch)

##########################
#   rectangles creation  #
##########################

rectangle1 = shapes.Rectangle(125, 100, # rectangle le plus large
                             300, 50,
                             color = (151, 29, 64),
                             batch = batch)

rectangle2 = shapes.Rectangle(150, 150,
                             250, 50,
                             color = (166, 44, 49),
                             batch = batch)

rectangle3 = shapes.Rectangle(175, 200,
                             200, 50,
                             color = (181, 59, 34),
                             batch = batch)

rectangle4 = shapes.Rectangle(200, 250,
                             150, 50,
                             color = (196, 74, 19),
                             batch = batch)

rectangle5 = shapes.Rectangle(225, 300, # rectangle le plus petit
                             100, 50,
                             color = (211, 89, 4),
                             batch = batch)

########################
#    Rectangle list    #
########################

liste_rectangle = [
    ["rectangle1", rectangle1.position],
    ["rectangle2", rectangle2.position],
    ["rectangle3", rectangle3.position],
    ["rectangle4", rectangle4.position],
    ["rectangle5", rectangle5.position],
]

############################
#    Rectangle function    #
############################

def find(interval):
    """ 
    renvoie le plus haut réctangle d'un pôle
    """
    valeur = liste_rectangle[0][1][1] # valeur --> coordonée y du rectangle le plus haut
    nom = liste_rectangle[0][0]       #    nom --> nom du rectangle le plus haut
    nbr = 0                           #    nbr --> nbr de rectangle dans un interval donné
    for rectangle in liste_rectangle:
        if interval[0] <= rectangle[1][0] <= interval[1]:
            nbr += 1 
            if rectangle[1][1] >= valeur:
                valeur = rectangle[1][1]
                nom = rectangle[0]
    if nbr >= 1: # Il y a au moins un rectangle dans la partie
        return (nom, valeur)
    else: # La partie est vide
        return ("rectangle0", 85)

##################
#   end event    #
##################

def end_game():
    """
    closes the app and sends winning message on terminal
    """
    pyglet.app.exit()
    if clic == 31:
        print("#############################")
        print("#    Congrates! You won!    #")
        print("#############################")
    else:
        print("###########################################")
        print("#    Well done!                           #")
        print("#    But it took you ", clic, " moves.          #")
        print("#    Can you win in only 31 moves?        #")
        print("###########################################")
        
###################
#   main event    #
###################

@window.event
def on_draw():
    window.clear()
    # dessine les barres et rectangles
    batch.draw()
    
####################
#    Mouse event   #
####################

def partie(x): 
    """
    Renvoie grace au corrdoné x de la sourie, 
    si elle se situe à la partie de droite, milieux au gauche de l'écran.
    Donc si l'uttilisateur a souhaiter intéragir avec la pile 1, 2 ou 3.
    """
    if x <= (window_lenght/3):
        return 1
    elif ((window_lenght/3)*2) >= x > (window_lenght/3):
        return 2
    else:
        return 3

selected_rectangle = [] # name and y axis of the rectangle that will be moved 
def select(x):
    """
    retourne le rectangle à déplacer
    """ 
    global selected_rectangle
    if partie(x) == 1:
        selected_rectangle = find((0, 485))
    elif partie(x) == 2:
        selected_rectangle = find((486, 970))
    else:
        selected_rectangle = find((971, 1455))

def move(x):
    """
    déplace le rectangle
    """
    global liste_rectangle
    ##################
    #    Partie 1    #
    ##################
    if partie(x) == 1:
        if find((0, 485))[1] == 85 : # la partie est vide
            if selected_rectangle[0] == "rectangle0": # aucun rectangle n'a été séléctionné
                pass
            elif selected_rectangle[0] == "rectangle1":
                rectangle1.position = 125, 100
                liste_rectangle[0][1] = (rectangle1.position)
            elif selected_rectangle[0] == "rectangle2":
                rectangle2.position = 150, 100
                liste_rectangle[1][1] = (rectangle2.position)
            elif selected_rectangle[0] == "rectangle3":
                rectangle3.position = 175, 100
                liste_rectangle[2][1] = (rectangle3.position)
            elif selected_rectangle[0] == "rectangle4":
                rectangle4.position = 200, 100
                liste_rectangle[3][1] = (rectangle4.position)
            else :
                rectangle5.position = 225, 100
                liste_rectangle[4][1] = (rectangle5.position)
        elif find((0, 485))[1] == 100 : # la partie contient un rectangle
            if find((0, 485))[0] == "rectangle1":
                if selected_rectangle[0] == "rectangle2": 
                    rectangle2.position = 150, 150
                    liste_rectangle[1][1] = (rectangle2.position)      
                elif selected_rectangle[0] == "rectangle3": 
                    rectangle3.position = 175, 150
                    liste_rectangle[2][1] = (rectangle3.position)    
                elif selected_rectangle[0] == "rectangle4": 
                    rectangle4.position = 200, 150
                    liste_rectangle[3][1] = (rectangle4.position)      
                elif selected_rectangle[0] == "rectangle5": 
                    rectangle5.position = 225, 150
                    liste_rectangle[4][1] = (rectangle5.position)
                else:
                    pass
            elif find((0, 485))[0] == "rectangle2":
                if selected_rectangle[0] == "rectangle3": 
                    rectangle3.position = 175, 150
                    liste_rectangle[2][1] = (rectangle3.position)
                elif selected_rectangle[0] == "rectangle4": 
                    rectangle4.position = 200, 150
                    liste_rectangle[3][1] = (rectangle4.position)   
                elif selected_rectangle[0] == "rectangle5": 
                    rectangle5.position = 225, 150
                    liste_rectangle[4][1] = (rectangle5.position)
                else:
                    pass
            elif find((0, 485))[0] == "rectangle3":
                if selected_rectangle[0] == "rectangle4": 
                    rectangle4.position = 200, 150
                    liste_rectangle[3][1] = (rectangle4.position)     
                elif selected_rectangle[0] == "rectangle5": 
                    rectangle5.position = 225, 150
                    liste_rectangle[4][1] = (rectangle5.position)
                else:
                    pass
            elif find((0, 485))[0] == "rectangle4":
                if selected_rectangle[0] == "rectangle5":
                    rectangle5.position = 225, 150
                    liste_rectangle[4][1] = (rectangle5.position)
                else:
                    pass
            else:
                pass # le rectangle 5 est le plus petit, rien ne peu aller au dessus
        elif find((0, 485))[1] == 150 : # la partie contient deux rectangles
            if find((0, 485))[0] == "rectangle2":
                if selected_rectangle[0] == "rectangle3": 
                    rectangle3.position = 175, 200
                    liste_rectangle[2][1] = (rectangle3.position)    
                elif selected_rectangle[0] == "rectangle4": 
                    rectangle4.position = 200, 200
                    liste_rectangle[3][1] = (rectangle4.position)    
                elif selected_rectangle[0] == "rectangle5":  
                    rectangle5.position = 225, 200
                    liste_rectangle[4][1] = (rectangle5.position)
                else:
                    pass
            if find((0, 485))[0] == "rectangle3":
                if selected_rectangle[0] == "rectangle4": 
                    rectangle4.position = 200, 200
                    liste_rectangle[3][1] = (rectangle4.position) 
                elif selected_rectangle[0] == "rectangle5":
                    rectangle5.position = 225, 200
                    liste_rectangle[4][1] = (rectangle5.position)
                else:
                    pass
            if find((0, 485))[0] == "rectangle4":
                if selected_rectangle[0] == "rectangle5":
                    rectangle5.position = 225, 200
                    liste_rectangle[4][1] = (rectangle5.position)
                else:
                    pass
            if find((0, 485))[0] == "rectangle5":
                pass
        elif find((0, 485))[1] == 200 : # la partie contient trois rectangles
            if find((0, 485))[0] == "rectangle3":
                if selected_rectangle[0] == "rectangle4": 
                    rectangle4.position = 200, 250
                    liste_rectangle[3][1] = (rectangle4.position)
                elif selected_rectangle[0] == "rectangle5": 
                    rectangle5.position = 225, 250
                    liste_rectangle[4][1] = (rectangle5.position)
                else:
                    pass
            if find((0, 485))[0] == "rectangle4":
                if selected_rectangle[0] == "rectangle5": 
                    rectangle5.position = 225, 250
                    liste_rectangle[4][1] = (rectangle5.position)
                else:
                    pass
            if find((0, 485))[0] == "rectangle5":
                pass
        elif find((0, 485))[1] == 250 : # la partie contient quatre rectangles
            if find((0, 485))[0] == "rectangle4":
                if selected_rectangle[0] == "rectangle5": 
                    rectangle5.position = 225, 300
                    liste_rectangle[4][1] = (rectangle5.position)
                else:
                    pass
            if find((0, 485))[0] == "rectangle5":
                pass
        else: # la partie est déja remplie
            pass
    ##################
    #    Partie 2    #
    ##################
    if partie(x) == 2:
        if find((486, 970))[1] == 85 : # la partie est vide
            if selected_rectangle[0] == "rectangle0": # aucun rectangle n'a été séléctionné
                pass
            elif selected_rectangle[0] == "rectangle1":
                rectangle1.position = 575, 100
                liste_rectangle[0][1] = (rectangle1.position)
            elif selected_rectangle[0] == "rectangle2":
                rectangle2.position = 600, 100
                liste_rectangle[1][1] = (rectangle2.position)
            elif selected_rectangle[0] == "rectangle3":
                rectangle3.position = 625, 100
                liste_rectangle[2][1] = (rectangle3.position)
            elif selected_rectangle[0] == "rectangle4":
                rectangle4.position = 650, 100
                liste_rectangle[3][1] = (rectangle4.position)
            else :
                rectangle5.position = 675, 100
                liste_rectangle[4][1] = (rectangle5.position)
        elif find((486, 970))[1] == 100 : # la partie contient un rectangle
            if find((486, 970))[0] == "rectangle1":
                if selected_rectangle[0] == "rectangle2": 
                    rectangle2.position = 600, 150
                    liste_rectangle[1][1] = (rectangle2.position)        
                elif selected_rectangle[0] == "rectangle3": 
                    rectangle3.position = 625, 150
                    liste_rectangle[2][1] = (rectangle3.position)    
                elif selected_rectangle[0] == "rectangle4": 
                    rectangle4.position = 650, 150
                    liste_rectangle[3][1] = (rectangle4.position)     
                elif selected_rectangle[0] == "rectangle5": 
                    rectangle5.position = 675, 150
                    liste_rectangle[4][1] = (rectangle5.position)
                else:
                    pass
            elif find((486, 970))[0] == "rectangle2":
                if selected_rectangle[0] == "rectangle3": 
                    rectangle3.position = 625, 150
                    liste_rectangle[2][1] = (rectangle3.position)
                elif selected_rectangle[0] == "rectangle4": 
                    rectangle4.position = 650, 150
                    liste_rectangle[3][1] = (rectangle4.position)    
                elif selected_rectangle[0] == "rectangle5": 
                    rectangle5.position = 675, 150
                    liste_rectangle[4][1] = (rectangle5.position)
                else:
                    pass
            elif find((486, 970))[0] == "rectangle3":
                if selected_rectangle[0] == "rectangle4": 
                    rectangle4.position = 650, 150
                    liste_rectangle[3][1] = (rectangle4.position)    
                elif selected_rectangle[0] == "rectangle5": 
                    rectangle5.position = 675, 150
                    liste_rectangle[4][1] = (rectangle5.position)
                else:
                    pass
            elif find((486, 970))[0] == "rectangle4":
                if selected_rectangle[0] == "rectangle5":
                    rectangle5.position = 675, 150
                    liste_rectangle[4][1] = (rectangle5.position)
                else:
                    pass
            else:
                pass # le rectangle 5 est le plus petit, rien ne peu aller au dessus
        elif find((486, 970))[1] == 150 : # la partie contient deux rectangles
            if find((486, 970))[0] == "rectangle2":
                if selected_rectangle[0] == "rectangle3": 
                    rectangle3.position = 625, 200
                    liste_rectangle[2][1] = (rectangle3.position)    
                elif selected_rectangle[0] == "rectangle4": 
                    rectangle4.position = 650, 200
                    liste_rectangle[3][1] = (rectangle4.position)    
                elif selected_rectangle[0] == "rectangle5":  
                    rectangle5.position = 675, 200
                    liste_rectangle[4][1] = (rectangle5.position)
                else:
                    pass
            if find((486, 970))[0] == "rectangle3":
                if selected_rectangle[0] == "rectangle4": 
                    rectangle4.position = 650, 200
                    liste_rectangle[3][1] = (rectangle4.position)     
                elif selected_rectangle[0] == "rectangle5":
                    rectangle5.position = 675, 200
                    liste_rectangle[4][1] = (rectangle5.position)
                else:
                    pass
            if find((486, 970))[0] == "rectangle4":
                if selected_rectangle[0] == "rectangle5":
                    rectangle5.position = 675, 200
                    liste_rectangle[4][1] = (rectangle5.position)
                else:
                    pass
            if find((486, 970))[0] == "rectangle5":
                pass
        elif find((486, 970))[1] == 200 : # la partie contient trois rectangles
            if find((486, 970))[0] == "rectangle3":
                if selected_rectangle[0] == "rectangle4": 
                    rectangle4.position = 650, 250
                    liste_rectangle[3][1] = (rectangle4.position)
                elif selected_rectangle[0] == "rectangle5": 
                    rectangle5.position = 675, 250
                    liste_rectangle[4][1] = (rectangle5.position)
                else:
                    pass
            if find((486, 970))[0] == "rectangle4":
                if selected_rectangle[0] == "rectangle5": 
                    rectangle5.position = 675, 250
                    liste_rectangle[4][1] = (rectangle5.position)
                else:
                    pass
            if find((486, 970))[0] == "rectangle5":
                pass
        elif find((486, 970))[1] == 250 : # la partie contient quatre rectangles
            if find((486, 970))[0] == "rectangle4":
                if selected_rectangle[0] == "rectangle5": 
                    rectangle5.position = 675, 300
                    liste_rectangle[4][1] = (rectangle5.position)
                else:
                    pass
            if find((486, 970))[0] == "rectangle5":
                pass
        else: # la partie est déja remplie
            pass
    ##################
    #    Partie 3    #
    ##################        
    if partie(x) == 3:
        if find((971, 1455))[1] == 85 : # la partie est vide
            if selected_rectangle[0] == "rectangle0": # aucun rectangle n'a été séléctionné
                pass
            elif selected_rectangle[0] == "rectangle1":
                rectangle1.position = 1025, 100
                liste_rectangle[0][1] = (rectangle1.position)
            elif selected_rectangle[0] == "rectangle2":
                rectangle2.position = 1050, 100
                liste_rectangle[1][1] = (rectangle2.position)
            elif selected_rectangle[0] == "rectangle3":
                rectangle3.position = 1075, 100
                liste_rectangle[2][1] = (rectangle3.position)
            elif selected_rectangle[0] == "rectangle4":
                rectangle4.position = 1100, 100
                liste_rectangle[3][1] = (rectangle4.position)
            else :
                rectangle5.position = 1125, 100
                liste_rectangle[4][1] = (rectangle5.position)
        elif find((971, 1455))[1] == 100 : # la partie contient un rectangle
            if find((971, 1455))[0] == "rectangle1":
                if selected_rectangle[0] == "rectangle2": 
                    rectangle2.position = 1050, 150
                    liste_rectangle[1][1] = (rectangle2.position)        
                elif selected_rectangle[0] == "rectangle3": 
                    rectangle3.position = 1075, 150
                    liste_rectangle[2][1] = (rectangle3.position)    
                elif selected_rectangle[0] == "rectangle4": 
                    rectangle4.position = 1100, 150
                    liste_rectangle[3][1] = (rectangle4.position)     
                elif selected_rectangle[0] == "rectangle5": 
                    rectangle5.position = 1125, 150
                    liste_rectangle[4][1] = (rectangle5.position)
                else:
                    pass
            elif find((971, 1455))[0] == "rectangle2":
                if selected_rectangle[0] == "rectangle3": 
                    rectangle3.position = 1075, 150
                    liste_rectangle[2][1] = (rectangle3.position)
                elif selected_rectangle[0] == "rectangle4": 
                    rectangle4.position = 1100, 150
                    liste_rectangle[3][1] = (rectangle4.position)    
                elif selected_rectangle[0] == "rectangle5": 
                    rectangle5.position = 1125, 150
                    liste_rectangle[4][1] = (rectangle5.position)
                else:
                    pass
            elif find((971, 1455))[0] == "rectangle3":
                if selected_rectangle[0] == "rectangle4": 
                    rectangle4.position = 1100, 150
                    liste_rectangle[3][1] = (rectangle4.position)    
                elif selected_rectangle[0] == "rectangle5": 
                    rectangle5.position = 1125, 150
                    liste_rectangle[4][1] = (rectangle5.position)
                else:
                    pass
            elif find((971, 1455))[0] == "rectangle4":
                if selected_rectangle[0] == "rectangle5":
                    rectangle5.position = 1125, 150
                    liste_rectangle[4][1] = (rectangle5.position)
                else:
                    pass
            else:
                pass # le rectangle 5 est le plus petit, rien ne peu aller au dessus
        elif find((971, 1455))[1] == 150 : # la partie contient deux rectangles
            if find((971, 1455))[0] == "rectangle2":
                if selected_rectangle[0] == "rectangle3": 
                    rectangle3.position = 1075, 200
                    liste_rectangle[2][1] = (rectangle3.position)    
                elif selected_rectangle[0] == "rectangle4": 
                    rectangle4.position = 1100, 200
                    liste_rectangle[3][1] = (rectangle4.position)    
                elif selected_rectangle[0] == "rectangle5":  
                    rectangle5.position = 1125, 200
                    liste_rectangle[4][1] = (rectangle5.position)
                else:
                    pass
            if find((971, 1455))[0] == "rectangle3":
                if selected_rectangle[0] == "rectangle4": 
                    rectangle4.position = 1100, 200
                    liste_rectangle[3][1] = (rectangle4.position)     
                elif selected_rectangle[0] == "rectangle5":
                    rectangle5.position = 1125, 200
                    liste_rectangle[4][1] = (rectangle5.position)
                else:
                    pass
            if find((971, 1455))[0] == "rectangle4":
                if selected_rectangle[0] == "rectangle5":
                    rectangle5.position = 1125, 200
                    liste_rectangle[4][1] = (rectangle5.position)
                else:
                    pass
            if find((971, 1455))[0] == "rectangle5":
                pass
        elif find((971, 1455))[1] == 200 : # la partie contient trois rectangles
            if find((971, 1455))[0] == "rectangle3":
                if selected_rectangle[0] == "rectangle4": 
                    rectangle4.position = 1100, 250
                    liste_rectangle[3][1] = (rectangle4.position)
                elif selected_rectangle[0] == "rectangle5": 
                    rectangle5.position = 1125, 250
                    liste_rectangle[4][1] = (rectangle5.position)
                else:
                    pass
            if find((971, 1455))[0] == "rectangle4":
                if selected_rectangle[0] == "rectangle5": 
                    rectangle5.position = 1125, 250
                    liste_rectangle[4][1] = (rectangle5.position)
                else:
                    pass
            if find((971, 1455))[0] == "rectangle5":
                pass
        elif find((971, 1455))[1] == 250 : # la partie contient quatre rectangles
            if find((971, 1455))[0] == "rectangle4":
                if selected_rectangle[0] == "rectangle5": 
                    rectangle5.position = 1125, 300
                    liste_rectangle[4][1] = (rectangle5.position)
                    end_game()
                else:
                    pass
            else:
                pass
        else: # la partie est déja remplie
            pass        
clic = 0 # la sourie n'a pas encore été appuyé

@window.event
def on_mouse_press(x, y, button, modifiers):
    """
    en fonction du nombre de fois que l'on a appuyer sur la sourie
    soit on appelle la fonction pour selectionner le rectangle à déplacer
    soit on appelle la fonction pour déplacer le rectangle 
    """ 
    global clic
    clic += 1
    if clic%2 == 1:
        return select(x)
    if clic%2 == 0 :
        return move(x)

#####################
#    run program    #
#####################
pyglet.app.run()