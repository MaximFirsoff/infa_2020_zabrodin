

import pygame
from pygame.draw import *
from random import randint
pygame.init()

time_out = 1000
font = pygame.font.Font(None, 50)
score = 0
w = 1200
h = 900
FPS = 60
screen = pygame.display.set_mode((w, h))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def create_new_ball():
    x = randint(100, 1100)
    y = randint(100, 900)
    vx = randint(-5, 5)
    vy = randint(-5, 5)
    r = randint(20, 50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    return {
            'vx': vx,
            'vy': vy,
            'x': x,
            'y': y,
            'r': r,
            'color': color
            }
    
def create_super_ball():
    x = randint(100, 1100)
    y = randint(100, 900)
    vx = randint(-10, 10)
    vy = randint(-10, 10)
    r = randint(20, 30)
    color = COLORS[randint(0, 5)]
    for i in range(r):
        red, green, blue = color
        circle(screen, ((red - i) % 255, (green - i) % 255, (blue) % 255), (x, y), r)
    return {
            'vx': vx,
            'vy': vy,
            'x': x,
            'y': y,
            'r': r,
            'color': color
            }

def highscore(score):
    name = input()
    with open('highscores.txt', 'a') as f:
        print(name + ': ' + str(score), file=f)

balls = [create_new_ball() for i in range(10)]
super_balls = [create_super_ball() for i in range(2)]

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for ball in balls:
        circle(screen, ball['color'], (ball['x'], ball['y']), ball['r'])
        ball['x'] += ball['vx']
        ball['y'] += ball['vy']
        if ball['x'] >= w or ball['x'] <= 0:
            ball['vx'] *= -1
        if ball['y'] >= h or ball['y'] <= 0:
            ball['vy'] *= -1
            
    for super_ball in super_balls:
        for i in range(super_ball['r']):
            red, green, blue = super_ball['color']
            circle(screen, ((red - i * 40) % 255, (green - i * 20) % 255, (blue) % 255), (super_ball['x'], super_ball['y']), super_ball['r'] - i)
        super_ball['x'] += super_ball['vx']
        super_ball['y'] += super_ball['vy']
        if super_ball['x'] >= w or super_ball['x'] <= 0:
            super_ball['vx'] *= -1
        if super_ball['y'] >= h or super_ball['y'] <= 0:
            super_ball['vy'] *= -1
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            for i, ball in enumerate(balls):
                if (ball['x'] - mouse_x) ** 2 + (ball['y'] - mouse_y) ** 2 <= ball['r'] ** 2:
                    balls[i] = create_new_ball()
                    score += 1
            for i, super_ball in enumerate(super_balls):
                if (super_ball['x'] - mouse_x) ** 2 + (super_ball['y'] - mouse_y) ** 2 <= super_ball['r'] ** 2:
                    super_balls[i] = create_super_ball()
                    score += 3
    text = font.render('Score: ' + str(score), 1, (255, 255, 255))
    screen.blit(text, (0, 30))
    text = font.render('Time: ' + str(int(time_out/FPS * 10) / 10), 1, (255, 255, 255))
    screen.blit(text, (0, 0))
    time_out -= 1
    if time_out > 0:
        pygame.display.update()
        screen.fill(BLACK)
    else:
        highscore(score)
        time_out = 1000
        score = 0
        pygame.display.update()

pygame.quit()
