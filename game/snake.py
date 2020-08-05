import pygame as pg
from math import sqrt
from time import sleep, time


class snake:
    snake_list = []
    counter = 0
    def load_snake(self, pos):
        snake.snake_list.append(pos)
    def bite_dist(self, chance_time):
        n_pos = self.chasper_pos
        while n_pos == self.chasper_pos and self.run:
            if time() - self.move_time >= chance_time:
                for p in snake.snake_list:
                    d = lambda pos: int(round(sqrt((n_pos[0]-pos[0])**2 + (n_pos[1]-pos[1])**2), 1)*10)
                    if d(p) <= 14:
                        # pg.draw.line(self.screen, pg.Color('black'), p, self.chasper_pos, 5)
                        # pg.display.update()
                        image = pg.image.load('res/green.jpeg')
                        image = pg.transform.scale(image, (self.box, self.box))
                        self.screen.blit(image, (p[0]*self.box, p[1]*self.box))
                        # sleep()
                        image = pg.image.load('res/chameleon.png')
                        image = pg.transform.scale(image, (self.box, self.box))
                        self.screen.blit(image, (p[0]*self.box, p[1]*self.box))
                        sleep(.5)
                        image = pg.image.load('res/snake.png')
                        image = pg.transform.scale(image, (self.box, self.box))
                        self.screen.blit(image, (p[0]*self.box, p[1]*self.box))
                        print('encounter..', snake.counter)
                        snake.counter += 1
                        n_pos = None


