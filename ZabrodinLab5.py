import pygame
from pygame.draw import *
import sys
import random

pygame.init()
screen = pygame.display.set_mode((400, 550))
green = (18, 252, 1)
blue = (0, 250, 250)
yellow = (250, 250, 0)
gray = (233, 249, 245)
dark_green = (23, 152, 44)
pink = (255, 189, 189)
rotten = (181,119,22)
rotten_2 = (146,127,23)
white = (255, 255, 255)
black = (0, 0, 0)
unicorn1 = (171, 225, 242)
unicorn2 = (246, 187, 236)
unicorn3 = (238, 245, 175)
light_green = (0, 255, 26)
S2 = pygame.Surface((400, 400))


rect(screen, blue, (0, 0, 400, 550 / 2))

rect(S2, blue, (0, 0, 400, 550))
for i in range (10):
    arc(S2, (250, 250, 0), rect(screen, blue, (0, 0, 400, 400)), 3.1 + i * 0.2, 3.15 + i * 0.2, 200)
screen.blit(S2, (200, -200))
circle(screen, (250, 250, 0), (400, 0), 70)
rect(screen, green, (0, 550 / 2, 400, 550 / 2))


FPS = 30

'''
Function tree() draw tree
x, y = position of tree
scale = size of tree
'''

def tree(x, y, scale):
    rect(screen, gray, (x - int(120 / scale), y - int(37.5 / scale), int(30 / scale), int(100 / scale)))
    '''leafes'''
    ellipse(screen, black, (x - int(180 / scale) - 1, y - int(110 / scale) - 1, int(155 / scale) + 2, int(100 / scale) + 2))
    ellipse(screen, black, (x - int(220 / scale) - 1, y - int(180 / scale) - 1, int(230 / scale) + 2, int(120 / scale) + 2))
    ellipse(screen, black, (x - int(170 / scale) - 1, y - int(260 / scale) - 1, int(140 / scale) + 2, int(160 / scale) + 2))
    ellipse(screen, dark_green, (x - int(180 / scale), y - int(110 / scale), int(155 / scale), int(100 / scale)))
    ellipse(screen, dark_green, (x - int(220 / scale), y - int(180 / scale), int(230 / scale), int(120 / scale)))
    ellipse(screen, dark_green, (x - int(170 / scale), y - int(260 / scale), int(140 / scale), int(160 / scale)))
    '''apples on tree'''
    circle(screen, pink, (x - int(60 / scale), y - int(210 / scale)), int(17 / scale))
    circle(screen, pink, (x - int(20 / scale), y - int(120 / scale)), int(16 / scale))
    circle(screen, pink, (x - int(195 / scale), y - int(115 / scale)), int(18 / scale))
    circle(screen, pink, (x - int(145 / scale), y - int(40 / scale)), int(15 / scale))
    '''apples on ground'''
    circle(screen, rotten, (x - int(65 / scale), y + int(70 / scale)), int(13 / scale))
    circle(screen, rotten_2, (x - int(120 / scale), y + int(80 / scale)), int(12 / scale))
    circle(screen, rotten, (x - int(150 / scale), y + int(55 / scale)), int(16 / scale))

'''
Function body() draw body, head, legs
x, y = position of left bottom angle of body
scale = size of unicorn
orientation: 1 - unicorn look to the right, 0 - to the left
'''

def body(x, y, scale, orientation):
    ellipse(screen, white, (x - int(160 / scale) * int((1 - orientation) / 2), y, int(160 / scale), int(80 / scale)))
    rect(screen, white, (x + orientation * int(40 / scale) - int(19 / scale) * int((1 - orientation) / 2), y + int(70 / scale), int(19 / scale), int(60 / scale)))
    rect(screen, white, (x + orientation * int(8 / scale) - int(15 / scale) * int((1 - orientation) / 2), y + int(50 / scale), int(15 / scale), int(90 / scale)))
    rect(screen, white, (x + orientation * int(98 / scale) - int(17 / scale) * int((1 - orientation) / 2), y + int(50 / scale), int(17 / scale), int(93 / scale)))
    rect(screen, white, (x + orientation * int(130 / scale) - int(15 / scale) * int((1 - orientation) / 2), y + int(50 / scale), int(15 / scale), int(77 / scale)))
    rect(screen, white, (x + orientation * int(100 / scale) - int(50 / scale) * int((1 - orientation) / 2), y - int(50 / scale), int(50 / scale), int(100 / scale)))
    ellipse(screen, white, (x + orientation * int(100 / scale) - int(65 / scale) * int((1 - orientation) / 2), y - int(78 / scale), int(65 / scale), int(50 / scale)))
    ellipse(screen, white, (x + orientation * int(118 / scale) - int(70 / scale) * int((1 - orientation) / 2), y - int(65 / scale), int(70 / scale), int(30 / scale)))
    circle(screen, (229, 153, 206), (x + orientation * int(138 / scale) - int(8 / scale) * int((1 - orientation) / 2), y - int(60 / scale)), int(8 / scale))
    ellipse(screen, white, (x + orientation * int(132 / scale) - int(8 / scale) * int((1 - orientation) / 2), y - int(65 / scale), int(8 / scale), int(5 / scale)))
    polygon(screen, pink, [[x + orientation * int(120 / scale), y - int(75 / scale)], [x + orientation * int(135 / scale), y - int(145 / scale)], [x + orientation * int(138 / scale), y - int(77 / scale)]])
    
'''
Function mane() draw mane
x, y = position of left bottom angle of body
scale = size of unicorn
orientation: 1 - unicorn look to the right, 0 - to the left
'''

def mane(x, y, scale, orientation):
    for i in range(40):
        ellipse(screen, (255 - 2 * i, 189 + i, 189 + i), ( -int( 1.5 * ( i / 5 ) ** 1.9 / scale) * orientation * 1.3 + x + orientation * int(95 / scale) - int(9000 / scale) * int((1 - orientation) / 2), y - int(60 / scale) + int( 1.5 * 1.3 * i / scale ) , int((orientation + 1) / 2) * int(13 * i ** (0.5)  / scale) , int((orientation + 1) / 2) * int((15 + i / 4) / scale)))
        ellipse(screen, (255 - 2 * i, 189 + i, 189 + i), ( -int( 1.5 * ((( i - 15 ) ** 2) ** 0.5 / 5 ) ** 1.9 / scale) * orientation * 1.3 + x + orientation * int(95 / scale) - int(23 / scale) * int((1 - orientation) / 2) - int(9000 / scale) * int((1 + orientation) / 2), y - int(60 / scale) + int( 1.5 * 1.3 * i / scale ) , int(-(orientation - 1) / 2) * int(13 * i ** (0.5)  / scale) , int( -(orientation - 1) / 2) * int((15 + i / 4) / scale)))
        
'''
Function tail() draw tail
x, y = position of left bottom angle of body
scale = size of unicorn
orientation: 1 - unicorn look to the right, 0 - to the left
'''

def tail(x, y, scale, orientation):
    for i in range(25):
        ellipse(screen, (171 - 3*i, 225 + i, 242 - i), ( int(i*(-2) * orientation / scale) + x + int(30/scale) - orientation * int(40 / scale) - int(60 / scale) * int((1 - orientation) / 2) + (1 - orientation) * 9000, int(i*(2)/scale) + y + int(30 / scale), int((i * (orientation+1) + 10 * (orientation+1)) / scale), int(15 + i / scale) * (orientation+1)/2))
        ellipse(screen, (171 - 3*i, 225 + i, 242 - i), ( int(20/scale) + x - orientation * int(30 / scale) - int(60 / scale) * int((1 - orientation) / 2), int(i*(2)/scale) + y + int(30 / scale), int((i * (-1) * (orientation - 1) + 10 * (-1) * (orientation - 1)) / scale), int((23 + i) / scale) * (-1) * (orientation - 1)/2))

'''
Function unicorn() draw unicorn
x, y = position of left bottom angle of body
scale = size of unicorn
orientation: 1 - unicorn look to the right, 0 - to the left
'''

def unicorn(x, y, scale, orientation):
    body(x, y, scale, orientation)
    mane(x, y, scale, orientation)
    tail(x, y, scale, orientation)

unicorn(320, 250, 3.7, -1)
tree(70, 320, 2.7)
unicorn(380, 360, 1.7, -1)
tree(200, 285, 2.9)
tree(400, 295, 2.3)
tree(240, 320, 2.5)
unicorn(140, 310, 2.5, 1)
tree(150, 360, 2.2)
unicorn(118, 400, 1.4, 1)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

draw = False

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                draw = True
            elif i.button == 2:
                sc.fill(White)
                pygame.display.update()
        elif i.type == pygame.MOUSEBUTTONUP:
            if i.button == 1:
                draw = False
    if draw == True:
        pygame.draw.circle(screen,(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),i.pos,10)
        pygame.display.update()