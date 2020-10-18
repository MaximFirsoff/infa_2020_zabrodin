import pygame
from pygame.draw import *
from random import randint

pygame.init()
pygame.mixer.init()


def main():
    button_width, button_height = 300, 100 # Start button width and height
    started_already = False
    font = pygame.font.Font(None, 50)
    score = 0
    w, h = 1200, 900 # Screen width and height
    FPS = 60
    TIME = 30  # Time of game in seconds
    time_out_begin = TIME * FPS
    time_out = time_out_begin
    screen = pygame.display.set_mode((w, h))
    ticks = 0 # Frames (Uses to change SuperBall speed every 'ticks' frames)
    finished = False
    max_leaders = 10 # Number of leaders

    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    MAGENTA = (255, 0, 255)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

    def highscore(score):
        '''
        Function make "Enter your name" field when time is out and music is changing to VIKA.mp3
        :param score:
        :return: None
        '''
        file = 'VIKA.mp3'
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(-1)
        font = pygame.font.Font(None, 50)
        clock = pygame.time.Clock()
        input_box = pygame.Rect((w - button_width) / 2 + 15, h / 2 - 10, button_width - 15, 50)
        color_inactive = (100, 100, 100)
        color_active = (0, 0, 0)
        color = color_inactive
        active = False
        text = ''
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            with open('highscores.txt', 'a') as f:
                                print(text + ': ' + str(score) + '\n', file=f)
                            # Sorting highscores
                            highscores_file = open('highscores.txt', 'r')
                            leader_name = [line.strip() for line in highscores_file]
                            del leader_name[-1]
                            scores = [int(name.split()[-1]) for name in leader_name]
                            end_number = 0
                            for m in range(len(scores)):
                                if scores[-1] > scores[- m - 1]:
                                    end_number += 1
                            for i in range(end_number):
                                change_buffer = leader_name[len(scores) - 1 - i]
                                leader_name[len(scores) - i - 1] = leader_name[len(scores) - i - 2]
                                leader_name[len(scores) - i - 2] = change_buffer

                            with open('highscores.txt', 'w') as f:
                                element = 0
                                for line in leader_name:
                                    if element < max_leaders:
                                        print(line, file=f)
                                        element += 1
                                f.truncate()
                            return
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode
            screen.fill((0, 0, 0))
            rect(screen, (255, 218, 158),
                 ((w - button_width) / 2, (h - button_height) / 2, button_width, button_height))
            name_text = font.render('Enter your name ', 1, (99, 128, 255))
            screen.blit(name_text, ((w - button_width) / 2 + 11, (h - button_height) / 2 + 3))
            txt_surface = font.render(text, True, color)
            width = button_width - 30
            input_box.w = width
            screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
            pygame.draw.rect(screen, color, input_box, 2)
            pygame.display.flip()
            clock.tick(30)

    def create_new_ball():
        '''
        Function create ball
        :return: vx, vy (x_velocity, y_velocity) x, y, color (ball_coordinates, ball_colour)
        '''
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
        '''
        The same function as ball, but it creates super_ball
        :return:
        '''
        x = randint(100, 1100)
        y = randint(100, 900)
        vx = randint(-10, 10)
        vy = randint(-10, 10)
        r = randint(20, 30)
        color = COLORS[randint(0, 5)]
        for i in range(r):
            super_red, super_green, super_blue = color
            circle(screen, ((super_red - i) % 255, (super_green - i) % 255, super_blue % 255), (x, y), r)
        return {
            'vx': vx,
            'vy': vy,
            'x': x,
            'y': y,
            'r': r,
            'color': color
        }

    balls = [create_new_ball() for i in range(10)]
    super_balls = [create_super_ball() for i in range(2)]
    pygame.display.update()
    clock = pygame.time.Clock()
    screen.fill(BLACK)

    while not finished:
        clock.tick(FPS)
        for ball in balls:
            # Changing ball coordinates and velocity
            circle(screen, ball['color'], (ball['x'], ball['y']), ball['r'])
            ball['x'] += ball['vx']
            ball['y'] += ball['vy']
            if ball['x'] >= w or ball['x'] <= 0:
                ball['vx'] *= -1
            if ball['y'] >= h or ball['y'] <= 0:
                ball['vy'] *= -1

        for super_ball in super_balls:
            for i in range(super_ball['r']):
                # Making super_ball 'rainbow' colour.
                red, green, blue = super_ball['color']
                circle(screen, ((red - i * 40) % 255, (green - i * 20) % 255, blue % 255),
                       (super_ball['x'], super_ball['y']), super_ball['r'] - i)
            super_ball['x'] += super_ball['vx']
            super_ball['y'] += super_ball['vy']
            ticks += 1
            # Changing super_ball velocity every 0.5 seconds.
            if ticks > FPS / 2:
                super_ball['vx'] = randint(-10, 10)
                super_ball['vy'] = randint(-10, 10)
                ticks = 0
            # Super_ball hits the wall.
            if super_ball['x'] >= w or super_ball['x'] <= 0:
                super_ball['vx'] *= -1
            if super_ball['y'] >= h or super_ball['y'] <= 0:
                super_ball['vy'] *= -1

        if not started_already:
            # Start screen (with start button)
            screen.fill(BLACK)
            clicked = False
            file = 'morgen.mp3'
            pygame.mixer.music.load(file)
            pygame.mixer.music.play(-1)
            while not clicked:
                rect(screen, (255, 218, 158),
                     ((w - button_width) / 2, (h - button_height) / 2, button_width, button_height))
                text = font.render('START', 1, (99, 128, 255))
                screen.blit(text, (w / 2 - 53, h / 2 - 13))
                pygame.display.update()
                # Highscores in top left angle
                text = font.render('Highscores:', 1, (255, 255, 255))
                screen.blit(text, (5, 5))
                f = open('highscores.txt', 'r')
                leader_names = [line.strip() for line in f]
                number_of_leader = 0
                for name in leader_names:
                    if number_of_leader < max_leaders:
                        text = font.render(str(name), 1, (255, 255, 255))
                        screen.blit(text, (15,  50 + 35 * number_of_leader))
                    number_of_leader += 1
                # Clicking on start button
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = event.pos
                        if mouse_x <= (w + button_width) / 2 and mouse_x >= (w - button_width) / 2 and mouse_y <= (
                                h + button_height) / 2 and mouse_y >= (h - button_height) / 2:
                            clicked = True
                            started_already = True
                            file = 'central.mp3'
                            pygame.mixer.music.load(file)
                            pygame.mixer.music.play(-1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Give scores and destroy ball when it's clicked
                mouse_x, mouse_y = event.pos
                for i, ball in enumerate(balls):
                    if (ball['x'] - mouse_x) ** 2 + (ball['y'] - mouse_y) ** 2 <= ball['r'] ** 2:
                        balls[i] = create_new_ball()
                        score += 1
                for i, super_ball in enumerate(super_balls):
                    if (super_ball['x'] - mouse_x) ** 2 + (super_ball['y'] - mouse_y) ** 2 <= super_ball['r'] ** 2:
                        super_balls[i] = create_super_ball()
                        score += 5

        # Time and score in top left angle
        text = font.render('Score: ' + str(score), 1, (255, 255, 255))
        screen.blit(text, (0, 30))
        text = font.render('Time: ' + str(int(time_out / FPS * 10) / 10), 1, (255, 255, 255))
        screen.blit(text, (0, 0))
        time_out -= 1
        if time_out > 0:
            pygame.display.update()
            screen.fill(BLACK)
        else:
            highscore(score)
            return
    pygame.quit()

while True:
    main()
