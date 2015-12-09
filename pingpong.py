import pygame, sys, time
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((400, 600), 0, 32)
pygame.display.set_caption("Ping Pong")

SPEED = 4
DIR_X = 1
DIR_Y = 1

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (77,204,0)
RED = (255,0,0)
PINK = (255,204,255)
BLUE = (0,0,255)
TEAL = (0,255,255)



ball = pygame.Rect(100, 150, 60, 60)
#pygame.draw.circle(window, BLACK, (200, 500), 20, 0)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    for i in range(10):
        for j in range(5):
            color = [RED, GREEN, BLUE, TEAL, PINK]
            pygame.draw.rect(window, color[j], ((i*40) + 2 , (j*25) + 5, 36, 20))
            
    window.fill(WHITE)
            
    ball.left += SPEED*DIR_X
    ball.top += SPEED*DIR_Y

    if ball.left < 0 or ball.left > 400:
        DIR_X *= -1
    if ball.top < 0 or ball.top > 600:
        DIR_Y *= -1
    
    pygame.draw.rect(window, BLACK, ball)        
    pygame.display.update()
    time.sleep(0.02)