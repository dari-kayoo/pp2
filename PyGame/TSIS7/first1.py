import pygame
import random
width = 360
height = 480
FPS = 30

# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)   


# sozdaem igru i okno
pygame.init()
pygame.mixer.init()#for sound
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('My Game')
clock = pygame.time.Clock()

#cycle of game
running = True
while running:
    #  ввод процесса -* события
    #  Обновление
    #  визуализвция -* сборка
    pygame.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)  
    pygame.display.flip()      


pygame.quit() 
