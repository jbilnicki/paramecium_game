
import pygame
import random
import math

# creating window
screen = pygame.display.set_mode((800,600))
pygame.font.init()
pygame.display.set_caption('Paramecium')


# score
score = 0
bonus = 100

# required for displaying information

font = pygame.font.SysFont("Comic Sans MS", 20)
text = font.render("score", False, [0, 0, 0])


# player

# player's image
player_img = pygame.image.load('paramecium.png')

# player's initial coordinates
# center of the image on center of window
player_x = 368 #(800/2 - 64/2) 
player_y = 400 
speed_x = 0
speed_y = 0

# ameba
global a_speed_x, a_speed_y
amoeba_img = pygame.image.load('amoeba.png')

# random coordinates
amoeba_x = random.randint(0, 736)
amoeba_y = random.randint(0, 536)
a_speed_x = 0.1
a_speed_y = 0.1

class Bacteria(object):
    '''creates bacterium object'''
    
    b_img = pygame.image.load('bacteria.png')
    x = random.randint(0, 736)
    y = random.randint(0, 536)
    speed_x = 0.2
    speed_y = 0.2
    
    def __init__(self, b_x=x, b_y=y, b_speed_x=speed_x, b_speed_y=speed_y, image=b_img):
        self.b_x = b_x
        self.b_y = b_y
        self.b_speed_x = b_speed_x
        self.b_speed_y = b_speed_y
        self.image = image
        
    
    
    
    def gen_bacterium(self, screen):
        '''displays bacterium on the window'''
    
        screen.blit(self.image, (self.b_x, self.b_y))
        
        
    def move_b(self):
        '''function needed for bacterium movements'''
        
        self.b_x += self.b_speed_x
        if self.b_x <= 0:
            self.b_speed_x *= -1
        elif self.b_x >= 780:
            # żeby nie wystawał
            self.b_speed_x *= -1
            
        
        
        self.b_y += self.b_speed_y
        if self.b_y <= 0:
            self.b_speed_y *= -1
        elif self.b_y >= 580:
            self.b_speed_y *= -1
        
    
    def gen_b(self, screen):
    #global b_x, b_y, b_speed_x, b_speed_y
        self.b_x = random.randint(0, 735)
        self.b_y = random.randint(0, 536)
        self.b_speed_x = 0.1
        self.b_speed_y = 0.1
        self.gen_bacterium(screen)
        
    def detect_colision(self, x, y, d):
        ''' detects colision between two points with a simple equation'''
        
        distance = math.sqrt((math.pow(self.b_x - x, 2) + math.pow(self.b_y - y, 2)))
        if distance < d:
            return True
        else:
            return False
        
    
            

# display paramecium and amoeba
def player(x, y):
    screen.blit(player_img, (x, y))
    
def amoeba(x, y):
    screen.blit(amoeba_img, (x, y))

# 3 bacteria  
bac_1 = Bacteria()
#bac_1.gen_bacterium(screen)
x = random.randint(0, 736)
y = random.randint(0, 536)
bac_2 = Bacteria(x, y)
x = random.randint(0, 736)
y = random.randint(0, 536)
bac_3 = Bacteria(x, y)

    
def detect_colision(x_1, y_1, x_2, y_2, d):
    '''  detects colision between two points with a simple equation'''
    # pow = power
    distance = math.sqrt((math.pow(x_1 - x_2, 2) + math.pow(y_1 - y_2, 2)))
    if distance < d:
        return True
    else:
        return False


         ###########    
# main game loop
running = True

while running:
    # background color, with a bonus
    if score < bonus:
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
            # detects only arrows and other keys do not disturbe game
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                speed_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                speed_y = 0
            
      
    player_x += speed_x
    # player can move only inside the window
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        # such that player doesn't hide on window borders
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
        
        a_speed_x *= -1
    if score >= bonus:   
        amoeba_x += 3 * a_speed_x
    else:
        amoeba_x += a_speed_x
    
    
    if amoeba_y <= 0:
        a_speed_y *= -1
    elif amoeba_y >= 536:
        a_speed_y *= -1
        
    if score >= bonus:
        amoeba_y += 3 * a_speed_y
    else:
       amoeba_y += a_speed_y
    
    
          ############
    
    
    # player initialising  
    player(player_x, player_y)
    amoeba(amoeba_x, amoeba_y)
    #bacterium(b_x, b_y)
    
    # lista wszystkich bakterii
    bacteria = [bac_1, bac_2, bac_3]
    
            ###################
    
    # fragment kodu wykonujący się dla wszstkich obiektów klasy Bacteria
    
    for bacterium in bacteria: 
        
        bacterium.gen_bacterium(screen)
        bacterium.move_b()
        
        # sprawdzanie kolizji z bakterią
        c = player_x + 10
        d = player_y + 10
        colision_1 = bacterium.detect_colision(c, d, 20)
        if colision_1 == True:
            bacterium.b_y = -50
            score += 1
            #text_2 = font.render(str(score), False, [0, 0, 0])
            #screen.blit(text_2, [0, 70])
            bacterium.gen_b(screen)
            
            
         # sprawdzanie kolizji bakterii z amebą
        
        e = amoeba_x + 35
        f = amoeba_y + 35
        colision_3 = bacterium.detect_colision(e, f, 40)
        if colision_3 == True:
            bacterium.b_y = -50
            bacterium.gen_b(screen)
            
        # rozmnożenie bakterii
        
        # lista która posłuży do numeracji potomnych bakterii
        b_names = []
        for i in range(100):
            n = str(i)
            b_names.append(n)
            
            
        '''# prawdopodobieństwo rozmnożenia    
        p_dup = 0.01
        r = random.random()
        # żeby nie wyskakiwała na bakterii rodzicielskiej
        x = bacterium.b_x + 10
        y = bacterium.b_y + 10
        if r < p_dup:
            n_2 =  len(bacteria)
            new_bac = b_names[n_2]
            new_bac = Bacteria(x, y)
            new_bac.gen_bacterium(screen)
            new_bac.move_b()
            bacteria.append(new_bac)'''
            
            ##################
    
    # sprawdzenie kolizji gracza z amebą
    a = amoeba_x + 20
    b = amoeba_y + 20
    colision_2 =  detect_colision(a, b, player_x, player_y, 60)
    if colision_2:
        score = 0
        player_y = -100
        player(368, 400)

    
    
    # bonus 
    if score >= bonus:
        text_2 = font.render(str(score), False, [247, 247, 15])
        screen.blit(text_2, [10, 70])
        
    
    else:
        text_2 = font.render(str(score), False, [0, 0, 0])
        screen.blit(text_2, [10, 70])    
    

    screen.blit(text, [5, 25]) 
    
           
   
        
       ###########
    pygame.display.update()
    


pygame.quit()

    
    
    
        
