import random
import pygame as pg

# Konstanter
WIDTH = 1000 
HEIGHT = 600

# Størrelsen til vinduet
SIZE = (WIDTH, HEIGHT)

#farger
WHITE=(255,255,255)
GREY=(100,100,100)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

# Initiere pygame
pg.init()

# Frames Per Second (bilder per sekund)
FPS = 60

# Lager en overflate (surface) vi kan tegne på
surface = pg.display.set_mode(SIZE)

# Lager en klokke
clock = pg.time.Clock()

# Variabel som styrer om spillet skal kjøres
run = True

poeng=0

# Henter font
font = pg.font.SysFont("Arial", 32)

def vis_poeng(tekst):
    textImg = font.render(tekst, True, BLACK)
    surface.blit(textImg, (15, 15))
    
    
#lager objekter
class Objekt:
    def __init__(self):
        self.w=40
        self.h=40
    
    def tegn(self):
        pg.draw.rect(surface,self.farge,[self.x,self.y,self.w,self.h])
        
    def beveg_x(self):
        self.x+=self.vx
        
    def beveg_y(self):
        self.y+=self.vy
        
        
class Spiller(Objekt):
    def __init__(self):
        super().__init__()
        
        self.farge=BLUE
        
        self.x= 100
        self.y= 280
        
        self.vx=5
        self.vy=3
        
        self.bare=False

class Spokelse(Objekt):
    def __init__(self):
        super().__init__()
        
        self.farge=GREY
        
        self.x=random.randint(200,795-self.w)
        self.y=random.randint(0,600-self.h)
        
        self.vx=4
        self.vy=2
        
    def update(self):
        # Oppdaterer posisjonen fra farten
        self.x += self.vx
        self.y += self.vy
        
        #sjekker for kollisjon med skilleveggene
        if spokelse.x <= 200+5:
            spokelse.vx *= -1
        if spokelse.x >= 795-spokelse.w:
            spokelse.vx *= -1
            
        # Sjekker kollisjon med bunn
        if self.y + self.h>= HEIGHT:
            self.vy *= -1
            
        #sjekker kollisjon med topp
        if self.y <= 0:
            self.vy *= -1
            
        
    
class Sau(Objekt):
    def __init__(self):
        super().__init__()
        
        self.farge=BLACK
        
        self.x=random.randint(800,1000-self.w)
        self.y=random.randint(0,600-self.h)

class Hindring(Objekt):
    def __init__(self):
        super().__init__()
        
        self.farge=GREEN
        
        self.x=random.randint(200,800-self.w)
        self.y=random.randint(0,600-self.h)
        
 
spiller = Spiller()
sauer=[Sau(), Sau(), Sau()]
hindringer=[Hindring(), Hindring(), Hindring()]
spokelser=[Spokelse()]
    

while run:
    clock.tick(FPS)
    
    keys = pg.key.get_pressed()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    surface.fill(WHITE)
    
    pg.draw.rect(surface,BLACK,(200,0,5,600))
    pg.draw.rect(surface,BLACK,(795,0,5,600))
    
    
    if keys[pg.K_RIGHT]:
        if spiller.bare == False:
            spiller.vx = 5
        else:
            spiller.vx = 2.5
        spiller.beveg_x()
    if keys[pg.K_LEFT]:
        if spiller.bare == False:
            spiller.vx = -5
        else:
            spiller.vx = -2.5
        spiller.beveg_x()
    if keys[pg.K_DOWN]:
        if spiller.bare == False:
            spiller.vy = 3
        else:
            spiller.vy = 1.5
        spiller.beveg_y()
    if keys[pg.K_UP]:
        if spiller.bare == False:
            spiller.vy = -3
        else:
            spiller.vy = -1.5
        spiller.beveg_y()
    
    if spiller.x >= WIDTH-spiller.w:
        spiller.x = WIDTH-spiller.w
    if spiller.x <= 0:
        spiller.x = 0
    if spiller.y >= HEIGHT-spiller.h:
        spiller.y = HEIGHT-spiller.h
    if spiller.y <= 0:
        spiller.y = 0
        
        
        
    if spiller.bare==True:
        spiller.farge=BLACK
        if spiller.x<=200-spiller.w:
            spiller.bare = False
            spiller.farge=BLUE
            spokelser.append(Spokelse())
            hindringer.append(Hindring())
            sauer.append(Sau())
            poeng+=1
                
    
    spiller.tegn()
    
    for spokelse in spokelser:
        spokelse.update()
        spokelse.tegn()
        
        if spokelse.y <= spiller.y <= spokelse.y + spokelse.h and spokelse.x <= spiller.x <= spokelse.x + spokelse.w:
            run = False
            print(f"Game over, du fikk {poeng} poeng")
        if spokelse.y <= spiller.y+spiller.h <= spokelse.y + spokelse.h and spokelse.x <= spiller.x <= spokelse.x + spokelse.w:
            run = False
            print(f"Game over, du fikk {poeng} poeng")
        if spokelse.y <= spiller.y <= spokelse.y + spokelse.h and spokelse.x <= spiller.x+spiller.w <= spokelse.x + spokelse.w:
            run = False
            print(f"Game over, du fikk {poeng} poeng")
        if spokelse.y <= spiller.y+spiller.h <= spokelse.y + spokelse.h and spokelse.x <= spiller.x+spiller.w <= spokelse.x + spokelse.w:
            run = False
            print(f"Game over, du fikk {poeng} poeng")

        
    for hindring in hindringer:
        hindring.tegn()
        
        if hindring.y <= spiller.y <= hindring.y + hindring.h and sau.x <= spiller.x <= hindring.x + hindring.w:
            run=False
        if hindring.y <= spiller.y+spiller.h <= hindring.y + hindring.h and hindring.x <= spiller.x <= hindring.x + hindring.w:
            run=False
        if hindring.y <= spiller.y <= hindring.y + hindring.h and hindring.x <= spiller.x+spiller.w <= hindring.x + hindring.w:
            run=False
        if hindring.y <= spiller.y+spiller.h <= hindring.y + hindring.h and hindring.x <= spiller.x+spiller.w <= hindring.x + hindring.w:
            run=False
    
    for sau in sauer:
        sau.tegn()
        
        if spiller.bare==False:
            if sau.y <= spiller.y <= sau.y + sau.h and sau.x <= spiller.x <= sau.x + sau.w:
                sau.x= 1002
                spiller.bare=True
            if sau.y <= spiller.y+spiller.h <= sau.y + sau.h and sau.x <= spiller.x <= sau.x + sau.w:
                sau.x= 1002
                spiller.bare=True
            if sau.y <= spiller.y <= sau.y + sau.h and sau.x <= spiller.x+spiller.w <= sau.x + sau.w:
                sau.x= 1002
                spiller.bare=True
            if sau.y <= spiller.y+spiller.h <= sau.y + sau.h and sau.x <= spiller.x+spiller.w <= sau.x + sau.w:
                sau.x= 1002
                spiller.bare=True
            
        elif spiller.bare == True:
            if sau.y <= spiller.y <= sau.y + sau.h and sau.x <= spiller.x <= sau.x + sau.w:
                run = False
            if sau.y <= spiller.y+spiller.h <= sau.y + sau.h and sau.x <= spiller.x <= sau.x + sau.w:
                run = False
            if sau.y <= spiller.y <= sau.y + sau.h and sau.x <= spiller.x+spiller.w <= sau.x + sau.w:
                run = False
            if sau.y <= spiller.y+spiller.h <= sau.y + sau.h and sau.x <= spiller.x+spiller.w <= sau.x + sau.w:
                run = False
        
    vis_poeng(f"Poeng: {poeng}")
    pg.display.flip()
    
    
pg.quit()






