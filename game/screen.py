'''
hahaha
'''
# import threading
import pygame as pg

from chasper import chasper
from snake import snake
from time import time

# global move_time
# move_time = 0


class scrn(chasper, snake):

    '''
    hahaha just a class for screen
    '''
    
    pg.init()
    Color_set = [pg.image.load('res/green.jpeg'), pg.image.load('res/snake.png'), pg.image.load('res/green.jpeg'), pg.image.load('res/green.jpeg'), pg.image.load('res/rock.png')]


    def __init__(self, grid, disp, box):
        self.move_time = time()
        self.disp = disp
        self.box = box
        self.grid_limit = int(disp[0]/box)

        self.all_map = grid

        self.map_maxima = len(grid)
        self.map_maxima_2 = len(grid[0])

        self.sub = (0, self.grid_limit)
        self.sub_2 = (0, self.grid_limit)


        self.set_grids()

        self.chasper_pos = ()
        self.screen = pg.display.set_mode(disp)
        scrn.grid_build(self, self.grid)
        chasper.build_chasper(self, (4, 4), box)
        self.stand_by()

    def set_grids(self):
        self.grid = list(self.all_map[self.sub[0]+1:self.sub[1]+1, self.sub_2[0]+1:self.sub_2[1]+1])
        self.out_grid = list(self.all_map[self.sub[0]:self.sub[1]+2, self.sub_2[0]:self.sub_2[1]+2])



    def grid_build(self, grd, h_x=0, h_y=0, a=0, b=0, mx=0, my=0):
        for i in range(self.grid_limit+a):
            for j in range(self.grid_limit+b):
                scrn.map_build(self, i+h_x, j+h_y, grd, a, b, mx, my)
                

    def map_build(self, i, j, grd, a=0, b=0, mx=0, my=0):
        l = i
        k = j
        if grd == self.out_grid:
            l += a
            k += b
            if -1 in (mx, my):
                if my<0 and j == int(j):
                    k -= 1
                if mx<0 and i == int(i):
                    l -= 1

        if i >= self.grid_limit or j >= self.grid_limit:
            return
        if not grd[int(l)][int(k)] == '#':
            if not grd[int(l)][int(k)] == '0':
                image = scrn.Color_set[0] 
                image = pg.transform.scale(image, (self.box, self.box))
                self.screen.blit(image, (i*self.box, j*self.box))
                if grd[int(l)][int(k)] == '1':
                    snake.load_snake(self, (int(l), int(k)))

            image = scrn.Color_set[int(grd[int(l)][int(k)])] 
        else:
            return

        image = pg.transform.scale(image, (self.box, self.box))
        self.screen.blit(image, (i*self.box, j*self.box))

    def event_monitor(self, keys, move_time):
        # move_time = time()
        if(keys[pg.K_UP] and self.chasper_pos[1] > 0):
            chasper.move_chasper(self, 0, -1, 4)
            move = time() - move_time
            # print(move)
            if move < 1:
                snake.bite_dist(self)
            self.move_time = time()
            

        elif(keys[pg.K_DOWN] and self.chasper_pos[1] < disp[1]/self.box-1):
            chasper.move_chasper(self, 0, 1, 4)
            move = time() - move_time
            # print(move)
            if move < 1:
                snake.bite_dist(self)
            self.move_time = time()

        elif(keys[pg.K_RIGHT] and self.chasper_pos[0] < disp[0]/self.box-1):
            chasper.move_chasper(self, 1, 0, 4) 
            move = time() - move_time
            # print(move)
            if move < 1:
                snake.bite_dist(self)
            self.move_time = time()

        elif(keys[pg.K_LEFT] and self.chasper_pos[0] > 0):
            chasper.move_chasper(self, -1, 0, 4)
            move = time() - move_time
            # print(move)
            if move < 1:
                snake.bite_dist(self)
            self.move_time = time()

    def stand_by(self):
        game_exit = False
        self.e = dict()
        while not game_exit:
            keys = pg.key.get_pressed() 

            if pg.QUIT in [e.type for e in pg.event.get()]:
                game_exit = True
                
            elif keys[pg.K_SPACE]:
                for i in self.out_grid:
                    print(i)

            elif keys[pg.K_p]:
                print(self.chasper_pos)

            elif pg.MOUSEBUTTONUP in [e.type for e in pg.event.get()]:
                print([int(i/50) for i in pg.mouse.get_pos()])

            elif keys[pg.K_q]:
                game_exit = True

            self.event_monitor(keys, self.move_time)

            for _ in pg.event.get():
                pass
            pg.display.flip()
        pg.quit()


disp = tuple([500]*2)
box = 50


from home_layout import home

grid = home()

s = scrn(grid, disp, box)