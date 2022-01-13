import pygame as pg
import random


vec2 = pg.math.Vector2

RES = WIDTH, HEIGHT = 1600, 900
NUM_STARS = 200

COLORS = [(0, 255, 0), (0, 80, 0)]

ALPHA = 35


class Block:
    def __init__(self, app):
        self.screen = app.screen
        self.pos2d = self.get_pos2d()
        self.vel = random.uniform(0.05, 0.25)
        self.color = random.choice(COLORS)
        self.screen_pos = vec2(0, 0)
        self.size = 20

        self.speed = random.randrange(7, 10)


    def get_pos2d(self):

        count_col = int(WIDTH / 20)
        col = [i for i in range(count_col)]
        x = col[random.randrange(len(col))] * 20
        y = random.randrange(0, 700)
        return vec2(x, y)

    def update(self):
        mouse_pos = pg.mouse.get_pos()


        self.pos2d = self.get_pos2d() if self.pos2d.y > HEIGHT else self.pos2d



        self.pos2d.y = self.pos2d.y + self.speed
        self.screen_pos = vec2(self.pos2d.x, self.pos2d.y)

    def draw(self):
        s = self.size
        if (-s < self.screen_pos.x < WIDTH + s) and (-s < self.screen_pos.y < HEIGHT + s):
            pg.draw.rect(self.screen, self.color, (*self.screen_pos, self.size, self.size))


class Blockfield:
    def __init__(self, app):
        self.stars = [Block(app) for i in range(NUM_STARS)]

    def run(self):
        [star.update() for star in self.stars]

        [star.draw() for star in self.stars]


class App:
    def __init__(self):
        self.screen = pg.display.set_mode(RES)

        self.alpha_surface = pg.Surface(RES)

        self.alpha_surface.set_alpha(ALPHA)
        self.clock = pg.time.Clock()
        self.starfield = Blockfield(self)

    def run(self):
        while True:


            self.screen.blit(self.alpha_surface, (0, 0))
            self.starfield.run()

            pg.display.flip()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            self.clock.tick(60)


if __name__ == '__main__':
    app = App()
    app.run()
