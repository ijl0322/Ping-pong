import pygame, sys, time, random
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((400, 600), 0, 32)
pygame.display.set_caption("Ping Pong")



SPEED = 4
DIR_X = 2
DIR_Y = 2

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (77,204,0)
RED = (255,0,0)
PINK = (255,204,255)
BLUE = (0,0,255)
TEAL = (0,255,255)

ball = pygame.Rect(100, 150, 40, 40)

bricks = []

x = ball.top
y = ball.left

score = 0


myfont = pygame.font.SysFont(None, 30)
text = myfont.render("Score: %d" %(score), True, BLUE, WHITE)
textRect = text.get_rect()
textRect.centerx = window.get_rect().centerx
textRect.centery = 200

text2 = myfont.render(str(y), True, WHITE, RED)
textRect2 = text2.get_rect()
textRect2.centerx = window.get_rect().centerx
textRect2.centery = 400





for i in range(10):
    for j in range(5):
        color = [RED, GREEN, BLUE, TEAL, PINK]
        bricks.append([pygame.Rect((i*40) + 2 , (j*25) + 5, 36, 20), color[j]])

previous_x = 0
previous_y = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    window.fill(WHITE)
            
            
    ball.left += SPEED*DIR_X
    ball.top += SPEED*DIR_Y


    if ball.left <= 0:
        ball.left = 0
        DIR_X *= -1
    if ball.right >= 400:
        ball.right = 400
        DIR_X *= -1
    if ball.top <= 0:
        ball.top = 0
        DIR_Y *= -1
    if ball.bottom >= 600:
        ball.bottom = 600
        DIR_Y *= -1

    for brick in bricks:
        if ball.colliderect(brick[0]):
            bricks.remove(brick)
            DIR_X *= -1
            DIR_Y *= -1
            score += 1
        else:
            pygame.draw.rect(window, brick[1], brick[0], 0)
        
    pygame.draw.circle(window, BLACK, ball.center, 20)


    
    text = myfont.render("Score: %d" %(score), True, BLUE, WHITE)




    window.blit(text, textRect)
        
    pygame.display.update()
    time.sleep(0.02)
