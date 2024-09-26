# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 18:22:58 2022

@author: Acer
"""

import pygame
import random
import math

# utwoezenie ekranu i nadanie nazwy
screen = pygame.display.set_mode((800,600))
pygame.font.init()
pygame.display.set_caption('Paramecium')


# liczba punktów
score = 0


# przygotowanie do wyswietlenie tych informacji

font = pygame.font.SysFont("Comic Sans MS", 20)
text = font.render("score", False, [0, 0, 0])


# gracz
# ikonka gracza
player_img = pygame.image.load('paramecium.png')
# współrzędne gracza (srodek okna)
# tylko żeby też srodek obrazka był na srodku okna
# a nie jego lewy gorny róg
player_x = 368 #(800/2 - 64/2) 64 to szerokosc obrazka
player_y = 400 # to tak na oko xd
speed_x = 0
speed_y = 0

# ameba
amoeba_img = pygame.image.load('amoeba.png')
# współrzędne losowe
amoeba_x = random.randint(0, 736)
amoeba_y = random.randint(0, 536)
a_speed_x = 0.1
a_speed_y = 0.1

# bakteria
b_img = pygame.image.load('bacteria.png')
b_x = random.randint(0, 736)
b_y = random.randint(0, 536)
b_speed_x = 0.1
b_speed_y = 0.1


# umieszczenie gracza na ekranie
def player(x, y):
    screen.blit(player_img, (x, y))
    
def amoeba(x, y):
    screen.blit(amoeba_img, (x, y))
    
def bacterium(x, y):
    screen.blit(b_img, (x, y))
    
def detect_colision(x_1, y_1, x_2, y_2, d):
    ''' wykrywa kolizję między dwoma obiektami o podanych 
    współrzędnych na podstawie prostego wzoru'''
    # pow to potęga po przecinku jej wykładnik
    distance = math.sqrt((math.pow(x_1 - x_2, 2) + math.pow(y_1 - y_2, 2)))
    if distance < d:
        return True
    else:
        return False
def gen_b():
    global b_x, b_y, b_speed_x, b_speed_y
    b_x = random.randint(0, 735)
    b_y = random.randint(0, 536)
    b_speed_x = 0.1
    b_speed_y = 0.1

         ###########    
# pętla gry
running = True

while running:
    # ustawiamy kolor tła kod RGB, zmiana jako bonus za dobrą grę
    if score < 100:
        screen.fill((51, 255, 255))
    else:
        screen.fill((0, 255, 128))
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed_x = -1
            if event.key == pygame.K_RIGHT:
                speed_x = 1
            if event.key == pygame.K_UP:
                speed_y = -1
            if event.key == pygame.K_DOWN:
                speed_y = 1
        if event.type == pygame.KEYUP:
            # żeby działało tylko dla strzałek i nie zaburzało się 
            # przy klikaniu innych klawiszy dodajemy warunek
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                speed_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                speed_y = 0
            
      
    player_x += speed_x
    # ograniczenie ruchu do wymiarów ekranu
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        # żeby nie wystawał
        player_x = 736
        
    player_y += speed_y
    if player_y <= 0:
        player_y = 0
    elif player_y >= 536:
        player_y = 536
        
           ############
           
    if amoeba_x <= 0:
        a_speed_x *= -1
    elif amoeba_x >= 736:
        # żeby nie wystawał
        a_speed_x *= -1
        
    amoeba_x += a_speed_x
    
    
    if amoeba_y <= 0:
        a_speed_y *= -1
    elif amoeba_y >= 536:
        a_speed_y *= -1
    amoeba_y += a_speed_y
    
    
          ############
          
    if b_x <= 0:
        b_speed_x *= -1
    elif b_x >= 780:
        # żeby nie wystawał
        b_speed_x *= -1
        
    b_x += b_speed_x
    
    
    if b_y <= 0:
        b_speed_y *= -1
    elif b_y >= 580:
        b_speed_y *= -1
    b_y += b_speed_y
    
    # wywołanie postaci   
    player(player_x, player_y)
    amoeba(amoeba_x, amoeba_y)
    bacterium(b_x, b_y)
    
    #bac_1 = Bacteria()
    #bac_1.gen_bac()
    #bac_2 = Bacteria()
    #bac_2.gen_bac()
    #bac_3  = Bacteria()
    #bac_3.gen_bac()
    
        
    # sprawdzanie kolizji z bakterią
    c = player_x + 10
    d = player_y + 10
    colision_1 = detect_colision(c, d, b_x, b_y, 20)
    if colision_1 == True:
        b_y = -50
        score += 1
        #text_2 = font.render(str(score), False, [0, 0, 0])
        #screen.blit(text_2, [0, 70])
        gen_b()
    
    # sprawdzenie kolizji gracza z amebą
    a = amoeba_x + 20
    b = amoeba_y + 20
    colision_2 =  detect_colision(a, b, player_x, player_y, 60)
    if colision_2:
        score = 0
        player_y = -100
        player(368, 400)
        
        
    # sprawdzanie kolizji bakterii z amebą
    e = amoeba_x + 35
    f = amoeba_y + 35
    colision_3 = detect_colision(e, f, b_x, b_y, 40)
    if colision_3 == True:
        b_y = -50
        gen_b()

    
    # bonus 
    if score >= 100:
        text_2 = font.render(str(score), False, [247, 247, 15])
        screen.blit(text_2, [10, 70])
    
    else:
        text_2 = font.render(str(score), False, [0, 0, 0])
        screen.blit(text_2, [10, 70])    
    
    #print(score)
    screen.blit(text, [5, 25]) 
    
    
        
        
       ###########
    pygame.display.update()
pygame.quit()