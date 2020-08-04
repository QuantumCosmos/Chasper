from math import sqrt

def adjust_pos(pos, bx_s):
    return tuple([int((int((i-bx_s/2)/bx_s))*bx_s)
                for i in list(pos)])

def c_pos(pos, bx_s):
    return tuple(int(i+bx_s/2) for i in pos)

def dist_calc(p1, p2, bs):
    a = int(round(sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2), 1)*10)
    print(a)
    return a