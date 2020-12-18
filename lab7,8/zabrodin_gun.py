from random import randrange as rnd, choice
import tkinter as tk
import math
import time


root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)
POINTS = 0
BULLET = 0
FPS = 60


class ball:
    def __init__(self, x=40, y=450, vx=0, vy=0):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = vx
        self.vy = vy
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.life_time = 5

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def collusion(self):
        """Проверка на столкновение снаряда со стеной."""
        if self.x - self.r < 0 or self.x + self.r > 800:
            self.vx *= -1
        elif self.y - self.r < 0 or self.y + self.r > 600:
            self.vy *= -1

    def move(self):
        """Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.life_time -= 0.04 / FPS * 40
        self.x += self.vx
        self.y += self.vy + 0.1 * 60 / FPS
        self.vy += 0.1
        canv.move(self.id, self.vx, self.vy)
        self.collusion()

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        return ((obj.x - self.x) ** 2 + (obj.y - self.y) ** 2 < (self.r + obj.r) ** 2)

    def __del__(self):
        """Уничтожение снаряда."""
        canv.delete(self.id)


class Gun():
    def __init__(self, x=20, y=550, vx=0, vy=0, v=2):
        """Размещение пушки на экране."""
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.velocity = v
        self.f2_power = 1
        self.f2_on = 0
        self.angle = 1
        self.id = canv.create_line(self.x, self.y, self.x + 30, self.y - 30, width=7)
        self.rot = False

    def fire_start(self, event):
        """Функция, фиксирующая зажатие ЛКМ."""
        self.f2_on = 1

    def fire_end(self, event):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet, BULLET
        bullet += 1
        BULLET += 1
        new_ball = ball(self.x + max(self.f2_power * 5, 20) * math.cos(self.angle),
                    self.y + max(self.f2_power * 5, 20) * math.sin(self.angle))
        new_ball.r += 5
        self.angle = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.angle) + self.vx
        new_ball.vy = self.f2_power * math.sin(self.angle) + self.vy
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 1

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.angle = math.atan((event.y - self.y) / (event.x - self.x)) + math.pi * (math.copysign(1, event.x - self.x) - 1) / 2
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, self.x, self.y,
                    self.x + max(self.f2_power * 5, 20) * math.cos(self.angle),
                    self.y + max(self.f2_power * 5, 20) * math.sin(self.angle)
                    )

    def power_up(self):
        """Регулировка мощности выстрела.
        Увеличение начальной скорости снаряда при зажатие ЛКМ."""
        if self.f2_on:
            if self.f2_power < 20:
                self.f2_power += 0.2
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')

    def move(self, event=0):
        """Перемещение пушки по полю.
        Пушка двигается по вертикали в направлении курсора."""
        if not self.rot:
            self.vx = self.velocity * math.cos(self.angle)
            self.vy = self.velocity * math.sin(self.angle)
        canv.move(self.id, self.vx, self.vy)


class Target:
    def __init__(self):
        """ Инициализация новой цели. """
        self.x = rnd(520, 760)
        self.y = rnd(120, 530)
        self.Ax = self.x - 620
        self.Ay = self.y - 325
        self.time = time.time()
        self.r = rnd(2, 20)
        self.color = 'red'
        self.points = 0
        self.live = 1
        self.id = canv.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r)
        canv.coords(self.id, self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r)
        canv.itemconfig(self.id, fill=self.color)
        self.radius = 30
        self.angle = 0

    def hit(self, points=1):
        """Попадание шарика в цель."""
        global POINTS
        canv.coords(self.id, -10, -10, -10, -10)
        POINTS += points

    def move(self):
        """Перемещение цели по полю."""
        self.angle = (self.angle + math.pi / 30) % (2 * math.pi) 
        canv.move(self.id,
                  self.radius * math.cos(self.angle) + self.Ax * math.cos(time.time() - self.time) + 620 - self.x + 20 * math.sin(5 * (time.time() - self.time)),
                  self.radius * math.sin(self.angle) + self.Ay * math.cos(time.time() - self.time) + 325 - self.y + 20 * math.sin(5 * (time.time() - self.time)))
        self.x = self.radius * math.cos(self.angle) + self.Ax * math.cos(time.time() - self.time) + 620 + 20 * math.sin(5 * (time.time() - self.time))
        self.y = self.radius * math.sin(self.angle) + self.Ay * math.cos(time.time() - self.time) + 325 + 20 * math.sin(5 * (time.time() - self.time))


screen1 = canv.create_text(400, 300, text='', font='28')
gun = Gun()
bullet = 0
balls = []
screen2 = canv.create_text(60, 30, text='Выстрелов: ' + str(BULLET), font='28')
screen3 = canv.create_text(87, 60, text='Уничтожено целей: ' + str(POINTS), font='28')


def new_game(event=''):
    global gun, t1, screen1, balls, bullet, POINTS, BULLET
    target = Target()
    bullet = 0
    balls = []
    canv.bind('<Button-1>', gun.fire_start)
    canv.bind('<ButtonRelease-1>', gun.fire_end)
    canv.bind('<Motion>', gun.targetting)
    target.live = 1
    while target.live or balls:
        i = 0
        while i < len(balls):
            balls[i].move()
            if balls[i].hittest(target) and target.live:
                target.live = 0
                target.hit()
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
                canv.itemconfig(screen2, text='Выстрелов: ' + str(BULLET), font='28')
                canv.itemconfig(screen3, text='Уничтожено целей: ' + str(POINTS), font='28')
            if balls[i].life_time < 0:
                balls.pop(i)
            i += 1
        canv.update()
        time.sleep(1 / FPS)
        gun.targetting()
        gun.power_up()
        gun.move()
        target.move()
    canv.itemconfig(screen1, text='')
    canv.delete(gun)
    root.after(1, new_game)


new_game()

root.mainloop()