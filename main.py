import tkinter as tk
import pygame
import random
from tkinter import Canvas, PhotoImage


# vars
jogando = True


# window setup
root = tk.Tk()
root.title("russian revolution 2025 ultra realistic simulator")
root.geometry("500x500")


# pygame init
pygame.mixer.init()

# load bgm
pygame.mixer.music.load("c:/Users/Public/music.mp3")  
pygame.mixer.music.play(-1) 

# canvas setup
canvas = tk.Canvas(root, width=500, height=500, bg="lightblue")
canvas.pack()

# load imgs
fundo_imagem = PhotoImage(file="c:/Users/Public/fundo.png")
# bg
canvas.create_image(250, 250, image=fundo_imagem)

# player
barra = canvas.create_rectangle(200, 400, 250, 450, fill="black")


# move player
def move_player(event):
    if event.keysym == "Left":  
        canvas.move(barra, -20, 0)
    elif event.keysym == "Right":  
        canvas.move(barra, 20, 0)

""" enemies
def criar_inimigo():
    x = random.randint(50, 350)
    enemy = "c:/Users/Public/bloco.png"
    inimigo = canvas.create_rectangle(x, 50, x+30, 80, fill=enemy)
"""
# Verificar colisão
def colidiu(obj1, obj2):
    x1, y1, x2, y2 = canvas.coords(obj1)
    px1, py1, px2, py2 = canvas.coords(obj2)
    return not (x2 < px1 or x1 > px2 or y2 < py1 or y1 > py2)


# Mover inimigo
def mover_inimigo(inimigo):
    global jogando
    if not jogando:
        return
    
    coords = canvas.coords(inimigo)
    if colidiu(inimigo, barra):
        root.quit()
        return
    elif coords[3] < 500:  
        canvas.move(inimigo, 0, 5)
        root.after(100, lambda: mover_inimigo(inimigo))
    else:
        canvas.delete(inimigo)


# enemies
cores = ["red", "white"]
cor = random.choice(cores)
# create enemies
def criar_inimigo():
    if not jogando:
        return
    x = random.randint(50, 350)
    inimigo = canvas.create_rectangle(x, 50, x+30, 80, fill=cor)
    mover_inimigo(inimigo)



# spawn 
def spawn_inimigos():
    criar_inimigo()
    root.after(2000, spawn_inimigos)  

spawn_inimigos()




# bind keys
root.bind("<Left>", move_player)  
root.bind("<Right>", move_player)  

# loop tkinter
root.mainloop()
