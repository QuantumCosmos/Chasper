import threading
import pygame as pg
from time import sleep, time

from snake import snake


class chasper(snake):
    move_delay = 0.1

    def time_thrd(self):
        try:
            t.join()
        except NameError:
            pass
        self.move_time = time()
        t = threading.Thread(target=snake.bite_dist, args=(self, chasper.move_delay, ))
        t.start()


    def build_chasper(self, pos, box_size, M='R', N='1'):
        self.chasper_pos = pos
        image = pg.image.load('res/move/'+M+'/'+M+N+'.png')
        image = pg.transform.scale(image, (self.box, self.box))
        self.screen.blit(image, (pos[0]*box_size, pos[1]*box_size))


    def move_chasper(self, m_x, m_y, f):
        if m_x == 1:
            M = 'R'
        elif m_x == -1:
            M = 'L'
        elif m_y == 1:
            M = 'F'
        elif m_y == -1:
            M = 'B'
        if self.grid[int(self.chasper_pos[0]+m_x)][int(self.chasper_pos[1]+m_y)] == '0':
            for i in range(f):

                t = 0.05
                self.map_build(int(self.chasper_pos[0]), int(self.chasper_pos[1]), self.grid)
                self.map_build(int(self.chasper_pos[0]+abs(m_x)), int(self.chasper_pos[1]+abs(m_y)), self.grid)

                if f==1:
                    (M, i) = ('L', 3)
                    if m_x == -1:
                        M = 'R'
                pos = (round(self.chasper_pos[0]+m_x/f, 2), round(self.chasper_pos[1]+m_y/f, 2))
                d = round(pos[0], 2) - int(self.grid_limit/2 + m_x)
                d_2 = round(pos[1], 2) - int(self.grid_limit/2 +m_y)
                l1 = lambda move,const: -bool(move+2)*(move+abs(const))
                
                p = l1(m_x, m_y)
                q = l1(m_y, m_x)
                l2 = lambda move: bool(p+q)*move + 1
                gx = l2(m_x)
                gy = l2(m_y)
                b1 = (self.map_maxima == self.sub[1]+2*m_x) if m_x>0 else (0 == self.sub[0])
                b2 = (self.map_maxima_2 == self.sub_2[1]+2*m_y) if m_y>0 else (0 == self.sub_2[0])
                
                # if (-3/4 == m_x*d and (not b1)) or (-3/4 == m_y*d_2 and (not b2)):
                #     pos = self.chasper_pos
                    

                #     self.grid_build(self.out_grid, m_x*(p-abs(m_x)*(i+1)/4), m_y*(q-abs(m_y)*(i+1)/4), gx, gy, m_x, m_y)

                #     if i==3:
                #         self.sub = (self.sub[0]+m_x, self.sub[1]+m_x)
                #         self.sub_2 = (self.sub_2[0]+m_y, self.sub_2[1]+m_y)
                #         self.set_grids()
                    
                chasper.build_chasper(self, pos, self.box, M, str(i))
                pg.display.update()
                sleep(chasper.move_delay)
            chasper.time_thrd(self)
        return False

        

