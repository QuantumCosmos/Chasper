import pygame as pg
from math import sqrt
from time import sleep, time


class snake:
    snake_list = []
    counter = 1
    def set_image(self, image_name, pos, a=0, b=0):
        image = pg.image.load(image_name)
        image = pg.transform.scale(image, (self.box, self.box))
        for i in range(a, b+1):
            for j in range(a, b+1):
                self.screen.blit(image, ((pos[0]+i)*self.box, (pos[1]+j)*self.box))

    def load_snake(self, pos):
        snake.snake_list.append(pos)
    def bite_dist(self, chance_time):
        n_pos = self.chasper_pos
        while n_pos == self.chasper_pos and self.run:
            if time() - self.move_time >= chance_time:
                for p in snake.snake_list:
                    d = lambda pos: int(round(sqrt((n_pos[0]-pos[0])**2 + (n_pos[1]-pos[1])**2), 1)*10)
                    if d(p) <= 14:
                        
                        snake.set_image(self, 'res/snake2.png', p)

                        pg.draw.line(self.screen, pg.Color(213,6,6), (p[0]*self.box+21.5,p[1]*self.box+15), tuple([i*self.box+25 for i in self.chasper_pos]), 5)
                        pg.display.update()

                        sleep(.1)

                        snake.set_image(self, 'res/green.jpeg', p, -1, 1)
                        
                        snake.set_image(self, 'res/snake.png', p)
                        snake.set_image(self, 'res/move/'+self.chasper[0]+'/'+self.chasper+'.png', self.chasper_pos)

                        print('encounter..', snake.counter)
                        snake.counter += 1
                        
                    n_pos = None
                    break



