from math import sqrt
from time import sleep

class snake:
    snake_list = []
    counter = 0
    def load_snake(self, pos):
        snake.snake_list.append(pos)
    def bite_dist(self):
        for p in snake.snake_list:
            d = lambda pos: int(round(sqrt((self.chasper_pos[0]-pos[0])**2 + (self.chasper_pos[1]-pos[1])**2), 1)*10)
            if d(p) <= 14:
                # sleep(.5)
                print('encounter..', snake.counter)
                snake.counter += 1


