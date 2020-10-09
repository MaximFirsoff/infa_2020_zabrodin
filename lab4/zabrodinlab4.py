'''Б02-002 Забродин Артём'''

import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 800))
S2 = pygame.Surface((600, 800))


def draw_window(x, y, size_X, size_Y):
    rect(screen, (213, 255, 230), (x, y, size_X, size_Y))
    rect(screen, (135, 205, 222), (x + 4 + size_X * 0.025, y + size_Y * 0.025, 0.42 * size_X, 0.25 * size_Y))
    rect(screen, (135, 205, 222), (x + 4 + size_X * 0.025, y + size_Y * 0.325, 0.42 * size_X, 0.65 * size_Y))
    rect(screen, (135, 205, 222), (x + size_X * 0.525, y + size_Y * 0.025, 0.42 * size_X, 0.25 * size_Y))
    rect(screen, (135, 205, 222), (x + size_X * 0.525, y + size_Y * 0.325, 0.42 * size_X, 0.65 * size_Y))

def draw_a_cat(x, y, size_X, size_Y, body_color_red, body_color_green, body_color_blue, eye_color_red, eye_color_green, eye_color_blue, orientation):
    if orientation == 1:
        ellipse(screen, (0, 0, 0), [x + size_X / 1.9 + size_X / 25 - 1, y + 0.12 * size_Y + size_Y / 40 - 1, size_X / 2.2 + 2, size_Y / 2.7 + 2])
        ellipse(screen, (body_color_red, body_color_green, body_color_blue), [x + size_X / 1.9 + size_X / 25, y + 0.12 * size_Y + size_Y / 40, size_X / 2.2, size_Y / 2.7])

        ellipse(screen, (0, 0, 0),[x + size_X / 8 - 1, y - size_Y / 30 - 1, size_X / 2 + 2, 0.9 * size_Y + 2])  # body line
        ellipse(screen, (body_color_red, body_color_green, body_color_blue), [x + size_X / 8, y - size_Y / 30, size_X / 2, 0.93 * size_Y])  # body

        ellipse(screen, (0, 0, 0),[x + size_X / 15 - 1, y + 0.43 * size_Y - 1, size_X / 12 + 2, size_Y / 2.4 + 2])  # back paw line
        ellipse(screen, (body_color_red, body_color_green, body_color_blue), [x + size_X / 15, y + 0.43 * size_Y, size_X / 12, size_Y / 2.4])  # back paw

        ellipse(screen, (0, 0, 0),[x + size_X / 7 - 1, y + 0.7 * size_Y - 1, size_X / 7 + 2, size_Y / 3.6 + 2])  # front paw line
        ellipse(screen, (body_color_red, body_color_green, body_color_blue), [x + size_X / 7, y + 0.7 * size_Y, size_X / 7, size_Y / 3.6])  # front paw

        ellipse(screen, (0, 0, 0), [x - 1, y - 1, size_X / 4.2 + 2, size_Y / 1.35 + 2], 1)  # head line
        ellipse(screen, (body_color_red, body_color_green, body_color_blue), [x, y, size_X / 4.2, size_Y / 1.35])  # head

        ellipse(screen, (0, 0, 0), [x + size_X / 2.1 - 1, y + 0.47 * size_Y - 1, size_X / 5.5 + 2, size_Y / 1.75 + 2])  # leg base line
        ellipse(screen, (body_color_red, body_color_green, body_color_blue), [x + size_X / 2.1, y + 0.47 * size_Y, size_X / 5.5, size_Y / 1.75])  # leg base

        ellipse(screen, (0, 0, 0),[x + size_X / 1.59 - 1, y + 0.8 * size_Y - 1, size_X / 15 + 2, size_Y / 2 + 2])  # leg line
        ellipse(screen, (body_color_red, body_color_green, body_color_blue), [x + size_X / 1.59, y + 0.8 * size_Y, size_X / 15, size_Y / 2])  # leg

        polygon(screen, (0, 0, 0), [(x + size_X / 4.3, y - 0.1 * size_Y), (x + size_X / 4.8, y + 0.2 * size_Y), (x + size_X / 6.3, y + 0.05 * size_Y), (x + size_X / 4.3, y - 0.1 * size_Y)])  # right ear line
        polygon(screen, (body_color_red, body_color_green, body_color_blue), [(x + size_X / 4.3 - 1, y - 0.1 * size_Y + 1), (x + size_X / 4.8 - 1, y + 0.2 * size_Y - 1), (x + size_X / 6.3 + 1, y + 0.05 * size_Y), (x + size_X / 4.3 - 1, y - 0.1 * size_Y + 1)])  # right ear
        polygon(screen, (255, 157, 122), [(x + size_X / 4.44, y - 0.075 * size_Y), (x + size_X / 4.95, y + 0.135 * size_Y), (x + size_X / 5.75, y + 0.05 * size_Y), (x + size_X / 4.44, y - 0.075 * size_Y)])  # right ear interior

        polygon(screen, (0, 0, 0),[(x, y - 0.1 * size_Y), (x + size_X / 45, y + 0.2 * size_Y), (x + size_X / 13, y + 0.05 * size_Y),(x, y - 0.1 * size_Y)])  # left ear line
        polygon(screen, (body_color_red, body_color_green, body_color_blue), [(x + 1, y - 0.1 * size_Y + 1), (x + size_X / 45 + 1, y + 0.2 * size_Y - 1),(x + size_X / 13 - 1, y + 0.04 * size_Y),(x + 1, y - 0.1 * size_Y + 1)])  # left ear
        polygon(screen, (255, 157, 122), [(x + 0.012 * size_X, y - 0.05 * size_Y), (x + size_X / 38, y + 0.135 * size_Y),(x + size_X / 15.6, y + 0.05 * size_Y), (x + 0.012 * size_X, y - 0.05 * size_Y)])  # left ear interior

        ellipse(screen, (0, 0, 0), [x + size_X / 28 - 1, y - 1 + size_Y / 4, size_X / 14.5 + 2, size_Y / 4.2 + 2 ],1)  # left eye line
        ellipse(screen, (eye_color_red, eye_color_green, eye_color_blue), [x + size_X / 28, y + size_Y / 4, size_X / 14.5, size_Y / 4.2])  # left eye
        ellipse(screen, (0, 0, 0), [x + size_X / 28 + size_X / 29, y + size_Y / 3.9, size_X / 80, size_Y / 4.6 ])  # left eye lid
        ellipse(screen, (234, 245, 234), [x + size_X / 28 + size_X / 100, y + size_Y / 3.7, size_X / 35, size_Y / 10 ])  # left eye shine

        ellipse(screen, (0, 0, 0), [x + size_X / 7.2 - 1, y - 1 + size_Y / 4, size_X / 14.5 + 2, size_Y / 4.2 + 2 ], 1)  # right eye line
        ellipse(screen, (eye_color_red, eye_color_green, eye_color_blue), [x + size_X / 7.2, y + size_Y / 4, size_X / 14.5, size_Y / 4.2])  # right eye
        ellipse(screen, (0, 0, 0), [x + size_X / 7.2 + size_X / 29, y + size_Y / 3.9, size_X / 80, size_Y / 4.6])  # right eye lid
        ellipse(screen, (234, 245, 234), [x + size_X / 7.2 + size_X / 100, y + size_Y / 3.7, size_X / 35, size_Y / 10])  # left eye shine

        polygon(screen, (0, 0, 0), [(x + size_X / 8.4 - size_X / 80 - 1, y + size_Y / 2 - 1),(x + size_X / 8.4 + size_X / 80 + 1, y + size_Y / 2 - 1), (x + size_X / 8.4, y + size_Y / 1.8 + 1), (x + size_X / 8.4 - size_X / 80 - 1, y + size_Y / 2 - 1)])  # nose
        polygon(screen, (255, 157, 155), [(x + size_X / 8.4 - size_X / 80, y + size_Y / 2), (x + size_X / 8.4 + size_X / 80, y + size_Y / 2), (x + size_X / 8.4, y + size_Y / 1.8), (x + size_X / 8.4 - size_X / 80, y + size_Y / 2)])  # nose

        line(screen, (0, 0, 0), (x + size_X / 8.4, y + size_Y / 1.8), (x + size_X / 8.4, y + size_Y / 1.6), 1)  # line from nose to mouth
        arc(screen, (0, 0, 0), [x + size_X / 8.4, y + size_Y / 1.75, size_X / 40, size_Y / 12], 3.8, 6.28, 1)  # right lip
        arc(screen, (0, 0, 0), [x + size_X / 8.4 - size_X / 44, y + size_Y / 1.75, size_X / 40, size_Y / 12], 3.14, 6.28, 1)  # left lip

        # left whisker
        arc(screen, (0, 0, 0), [x + size_X / 8.4 - size_X / 2.5, y + 0.525 * size_Y, size_X / 1.8, size_Y * 2], 1.25, 1.95, 1)
        arc(screen, (0, 0, 0), [x + size_X / 8.4 - size_X / 2.5 - size_X / 40, y + 0.465 * size_Y, size_X / 1.8, size_Y * 2], 1.15, 1.85, 1)
        arc(screen, (0, 0, 0), [x + size_X / 8.4 - size_X / 2.5 + size_X / 40, y + 0.575 * size_Y, size_X / 1.8, size_Y * 2], 1.35, 2.05, 1)

        # right whisker
        arc(screen, (0, 0, 0), [x + size_X / 8.4 - size_X / 6.5, y + 0.525 * size_Y, size_X / 1.8, size_Y * 2], 1.25, 1.95, 1)
        arc(screen, (0, 0, 0), [x + size_X / 8.4 - size_X / 6.5 + size_X / 40, y + 0.465 * size_Y, size_X / 1.8, size_Y * 2], 1.35, 2.03, 1)
        arc(screen, (0, 0, 0), [x + size_X / 8.4 - size_X / 6.5 - size_X / 40, y + 0.575 * size_Y, size_X / 1.8, size_Y * 2], 1.15, 1.85, 1)


    elif orientation == 0:

        ellipse(screen, (0, 0, 0), [x - size_X / 2.1 - size_X / 3.2 - 1, y + 0.12 * size_Y + size_Y / 40 - 1, size_X / 2.2 + 2, size_Y / 2.7 + 2])
        ellipse(screen, (body_color_red, body_color_green, body_color_blue), [x - size_X / 2.1 - size_X / 3.2, y + 0.12 * size_Y + size_Y / 40, size_X / 2.2, size_Y / 2.7])

        ellipse(screen, (0, 0, 0), [x - size_X / 2.5 - 1, y - size_Y / 30 - 1, size_X / 2 + 2, 0.9 * size_Y + 2])  # body line
        ellipse(screen, (body_color_red, body_color_green, body_color_blue), [x - size_X / 2.5, y - size_Y / 30, size_X / 2, 0.93 * size_Y])  # body

        ellipse(screen, (0, 0, 0), [x + size_X / 10 - 1, y + 0.43 * size_Y - 1, size_X / 12 + 2, size_Y / 2.4 + 2])  # back paw line
        ellipse(screen, (body_color_red, body_color_green, body_color_blue), [x + size_X / 10, y + 0.43 * size_Y, size_X / 12, size_Y / 2.4])  # back paw

        ellipse(screen, (0, 0, 0), [x - size_X / 37 - 1, y + 0.7 * size_Y - 1, size_X / 7 + 2, size_Y / 3.6 + 2])  # front paw line
        ellipse(screen, (body_color_red, body_color_green, body_color_blue), [x - size_X / 37, y + 0.7 * size_Y, size_X / 7, size_Y / 3.6])  # front paw

        ellipse(screen, (0, 0, 0), [x - 1, y - 1, size_X / 4.2 + 2, size_Y / 1.35 + 2], 1)  # head line
        ellipse(screen, (body_color_red, body_color_green, body_color_blue), [x, y, size_X / 4.2, size_Y / 1.35])  # head

        ellipse(screen, (0, 0, 0), [x - size_X / 2.35 - 1, y + 0.47 * size_Y - 1, size_X / 5.5 + 2, size_Y / 1.75 + 2])  # leg base line
        ellipse(screen, (body_color_red, body_color_green, body_color_blue), [x - size_X / 2.35, y + 0.47 * size_Y, size_X / 5.5, size_Y / 1.75])  # leg base

        ellipse(screen, (0, 0, 0), [x - size_X / 2.15 - 1, y + 0.8 * size_Y - 1, size_X / 15 + 2, size_Y / 2 + 2])  # leg line
        ellipse(screen, (body_color_red, body_color_green, body_color_blue), [x - size_X / 2.15, y + 0.8 * size_Y, size_X / 15, size_Y / 2])  # leg

        polygon(screen, (0, 0, 0), [(x + size_X / 4.3, y - 0.1 * size_Y), (x + size_X / 4.8, y + 0.2 * size_Y), (x + size_X / 6.3, y + 0.05 * size_Y), (x + size_X / 4.3, y - 0.1 * size_Y)])  # rightearline
        polygon(screen, (body_color_red, body_color_green, body_color_blue), [(x + size_X / 4.3 - 1, y - 0.1 * size_Y + 1), (x + size_X / 4.8 - 1, y + 0.2 * size_Y - 1), (x + size_X / 6.3 + 1, y + 0.05 * size_Y), (x + size_X / 4.3 - 1, y - 0.1 * size_Y + 1)])  # rightear
        polygon(screen, (255, 157, 122), [(x + size_X / 4.44, y - 0.075 * size_Y), (x + size_X / 4.95, y + 0.135 * size_Y), (x + size_X / 5.75, y + 0.05 * size_Y), (x + size_X / 4.44, y - 0.075 * size_Y)])  # right ear

        polygon(screen, (0, 0, 0), [(x, y - 0.1 * size_Y), (x + size_X / 45, y + 0.2 * size_Y), (x + size_X / 13, y + 0.05 * size_Y), (x, y - 0.1 * size_Y)])  # left ear line
        polygon(screen, (body_color_red, body_color_green, body_color_blue), [(x + 1, y - 0.1 * size_Y + 1), (x + size_X / 45 + 1, y + 0.2 * size_Y - 1), (x + size_X / 13 - 1, y + 0.05 * size_Y), (x + 1, y - 0.1 * size_Y + 1)])  # left ear
        polygon(screen, (255, 157, 122), [(x + 0.012 * size_X, y - 0.05 * size_Y), (x + size_X / 38, y + 0.135 * size_Y), (x + size_X / 15.6, y + 0.05 * size_Y), (x + 0.012 * size_X, y - 0.05 * size_Y)])  # left ear interior

        ellipse(screen, (0, 0, 0), [x + size_X / 28 - 1, y - 1 + size_Y / 4, size_X / 14.5 + 2, size_Y / 4.2 + 2], 1)  # left eye line
        ellipse(screen, (eye_color_red, eye_color_green, eye_color_blue), [x + size_X / 28, y + size_Y / 4, size_X / 14.5, size_Y / 4.2])  # left eye
        ellipse(screen, (0, 0, 0), [x + size_X / 20 + size_X / 50, y + size_Y / 3.9, size_X / 80, size_Y / 4.6])  # left eyelid
        ellipse(screen, (234, 245, 234), [x + size_X / 53 + size_X / 35, y + size_Y / 3.7, size_X / 35, size_Y / 10])  # left eye shine

        ellipse(screen, (0, 0, 0), [x + size_X / 7.2 - 1, y - 1 + size_Y / 4, size_X / 14.5 + 2, size_Y / 4.2 + 2], 1)  # right eye line
        ellipse(screen, (eye_color_red, eye_color_green, eye_color_blue), [x + size_X / 7.2, y + size_Y / 4, size_X / 14.5, size_Y / 4.2])  # right eye
        ellipse(screen, (0, 0, 0), [x + size_X / 6.4 + size_X / 50, y + size_Y / 3.9, size_X / 80, size_Y / 4.6])  # right eyelid
        ellipse(screen, (234, 245, 234), [x + size_X / 8.4 + size_X / 35, y + size_Y / 3.7, size_X / 35, size_Y / 10])  # left eye shine

        polygon(screen, (0, 0, 0), [(x + size_X / 8.4 - size_X / 80 - 1, y + size_Y / 2 - 1), (x + size_X / 8.4 + size_X / 80 + 1, y + size_Y / 2 - 1), (x + size_X / 8.4, y + size_Y / 1.8 + 1), (x + size_X / 8.4 - size_X / 80 - 1, y + size_Y / 2 - 1)])  # nose
        polygon(screen, (255, 157, 155), [(x + size_X / 8.4 - size_X / 80, y + size_Y / 2), (x + size_X / 8.4 + size_X / 80, y + size_Y / 2), (x + size_X / 8.4, y + size_Y / 1.8), (x + size_X / 8.4 - size_X / 80, y + size_Y / 2)])  # nose

        line(screen, (0, 0, 0), (x + size_X / 8.4, y + size_Y / 1.8), (x + size_X / 8.4, y + size_Y / 1.6), 1)  # line from noose to mouth
        arc(screen, (0, 0, 0), [x + size_X / 8.4, y + size_Y / 1.75, size_X / 40, size_Y / 12], 3.8, 6.28, 1)  # right lip
        arc(screen, (0, 0, 0), [x + size_X / 8.4 - size_X / 44, y + size_Y / 1.75, size_X / 40, size_Y / 12], 3.14, 6.3, 1)  # left lip

        # whiskers
        # right
        arc(screen, (0, 0, 0), [x + size_X / 8.4 - size_X / 6.5, y + 0.525 * size_Y, size_X / 1.8, size_Y * 2], 1.25, 1.95, 1)
        arc(screen, (0, 0, 0), [x + size_X / 8.4 - size_X / 6.5 + size_X / 40, y + 0.465 * size_Y, size_X / 1.8, size_Y * 2], 1.35, 2.03, 1)
        arc(screen, (0, 0, 0), [x + size_X / 8.4 - size_X / 6.5 - size_X / 40, y + 0.575 * size_Y, size_X / 1.8, size_Y * 2], 1.15, 1.85, 1)

        # left
        arc(screen, (0, 0, 0), [x + size_X / 8.4 - size_X / 2.5, y + 0.525 * size_Y, size_X / 1.8, size_Y * 2], 1.25, 1.95, 1)
        arc(screen, (0, 0, 0), [x + size_X / 8.4 - size_X / 2.5 - size_X / 40, y + 0.465 * size_Y, size_X / 1.8, size_Y * 2], 1.15, 1.85, 1)
        arc(screen, (0, 0, 0), [x + size_X / 8.4 - size_X / 2.5 + size_X / 40, y + 0.575 * size_Y, size_X / 1.8, size_Y * 2], 1.35, 2.05, 1)


def ball(x, y, r, orientation):
    circle(screen, (0, 0, 0), (x, y), r + 1)
    circle(screen, (154, 154, 154), (x, y), r)

    if orientation == 0:
        arc(screen, (0, 0, 0), [x - r - 0.17 * r, y - r + 0.25 * r, 1.9 * r, 1.9 * r], 0, 1.66, 1)
        arc(screen, (0, 0, 0), [x - r - 0.35 * r, y - r + 0.35 * r, 2 * r, 2 * r], 0, 1.66, 1)
        arc(screen, (0, 0, 0), [x - r - 0.45 * r, y - r + 0.45 * r, 2 * r, 2 * r], 0, 1.66, 1)
        arc(screen, (0, 0, 0), [x - r + 0.25 * r, y - r + 0.5 * r, 2 * r, 2 * r], 2, 3, 1)
        arc(screen, (0, 0, 0), [x - r + 0.41 * r, y - r + 0.65 * r, 2.1 * r, 2.1 * r], 2, 3, 1)
        arc(screen, (0, 0, 0), [x - r + 0.65 * r, y - r + 0.85 * r, 2 * r, 2 * r], 2, 3, 1)

    if orientation == 1:
        arc(screen, (0, 0, 0), [x - r + 0.17 * r, y - r + 0.25 * r, 1.9 * r, 1.9 * r], 1.7, 3.14, 1)
        arc(screen, (0, 0, 0), [x - r + 0.35 * r, y - r + 0.35 * r, 2 * r, 2 * r], 1.7, 3.14, 1)
        arc(screen, (0, 0, 0), [x - r + 0.45 * r, y - r + 0.45 * r, 2 * r, 2 * r], 1.7, 3.14, 1)
        arc(screen, (0, 0, 0), [x - r - 0.25 * r, y - r + 0.5 * r, 2 * r, 2 * r], 0.15, 1.15, 1)
        arc(screen, (0, 0, 0), [x - r - 0.41 * r, y - r + 0.65 * r, 2.1 * r, 2.1 * r], 0.15, 1.15, 1)
        arc(screen, (0, 0, 0), [x - r - 0.65 * r, y - r + 0.85 * r, 2 * r, 2 * r], 0.15, 1.15, 1)

    # thread tail

    if orientation == 0:
        arc(screen, (154, 154, 154), [x - 0.95 * r, y + 0.225 * r, 0.7 * r, 0.7 * r], 4.2, 5.24, 1)

        arc(screen, (154, 154, 154), [x - 0.95 * r - 0.35 * r, y + 0.225 * r + 0.61 * r, 0.7 * r, 0.7 * r], 1.05, 2.11, 1)

        arc(screen, (154, 154, 154), [x - 0.95 * r - 0.7 * r, y + 0.225 * r, 0.7 * r, 0.7 * r], 4.2, 5.24, 1)

        arc(screen, (154, 154, 154), [x - 0.95 * r - 1.05 * r, y + 0.225 * r + 0.61 * r, 0.7 * r, 0.7 * r], 1.05, 2.11, 1)

    if orientation == 1:
        arc(screen, (154, 154, 154), [x + 0.33 * r, y + 0.225 * r, 0.7 * r, 0.7 * r], 4.2, 5.24, 1)

        arc(screen, (154, 154, 154), [x + 0.33 * r + 0.35 * r, y + 0.225 * r + 0.606 * r, 0.7 * r, 0.7 * r], 1.05, 2.11, 1)

        arc(screen, (154, 154, 154), [x + 0.33 * r + 0.7 * r, y + 0.225 * r, 0.7 * r, 0.7 * r], 4.2, 5.236, 1)

        arc(screen, (154, 154, 154), [x + 0.33 * r + 1.05 * r, y + 0.225 * r + 0.61 * r, 0.7 * r, 0.7 * r], 1.05, 2.11, 1)


rect(screen, (128, 102, 0), (0, 400, 600, 400))
rect(screen, (85, 68, 0), (0, 0, 600, 400))

draw_window(400, 55, 180, 240)

draw_window(130, 55, 180, 240)

draw_window(-140, 55, 180, 240)

draw_a_cat(225, 560, 300, 100, 108, 93, 83, 42, 212, 255, 0)
draw_a_cat(150, 750, 100, 30, 108, 93, 83, 42, 212, 255, 0)
draw_a_cat(490, 750, 100, 30, 108, 93, 83, 42, 212, 255, 1)

draw_a_cat(300, 420, 300, 100, 200, 113, 55, 156, 208, 19, 1)
draw_a_cat(350, 680, 100, 30, 200, 113, 55, 156, 208, 19, 1)
draw_a_cat(120, 450, 100, 30, 200, 113, 55, 156, 208, 19, 0)
draw_a_cat(540, 590, 100, 30, 200, 113, 55, 156, 208, 19, 0)

ball(180, 455, 20, 0)
ball(150, 710, 18, 0)
ball(270, 730, 55, 0)
ball(415, 760, 18, 0)
ball(495, 700, 37, 1)
ball(380, 620, 37, 1)
ball(460, 575, 18, 1)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

screen.blit(S2, (50, 20))

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
