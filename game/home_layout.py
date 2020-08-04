import numpy as np
from random import randint

def home():
    a = '#'
    gridnp = np.array([
                        [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
                        [a, 0, 4, 4, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, a],
                        [a, 0, 4, 4, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, a],
                        [a, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, a],
                        [a, 0, 0, 0, 4, 0, 0, 0, 1, 0, 0, 0, 0, 0, a],
                        [a, 4, 4, 4, 0, 0, 4, 0, 0, 0, 0, 4, 0, 0, a],
                        [a, 4, 0, 0, 4, 0, 4, 0, 0, 0, 4, 0, 0, 0, a],
                        [a, 4, 0, 4, 0, 0, 4, 0, 0, 0, 4, 0, 0, 4, a],
                        [a, 4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, a],
                        [a, 4, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, a],
                        [a, 4, 0, 0, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0, a],
                        # [a, 4, 0, 4,, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, a],
                        # [a, 4, 0, 0, 0, 0, 4, 0, 0, 0, 4,, 0, 0, 0, a],
                        [a, 0, 4, 4, 4, 0, 4, 0, 0, 0, 4, 0, 0, 0, a],
                        # [a, 0, 4, 4, 4, 0, 4, 0, 0, 0, 4,, 0, 0, 0, a],
                        [a, 4, 4, 4, 4, 0, 4, 0, 0, 0, 4, 0, 0, 0, a],
                        # [a, 0, 4, 4, 4, 0, 4, 0, 0, 0, 4,, 0, 0, 0, a],
                        # [a, 0, 4, 4, 4, 0, 4, 0, 0, 0, 4,, 0, 0, 0, a],
                        # [a, 0, 4, 4, 4, 0, 4, 0, 0, 0, 4,, 0, 0, 0, a],
                        # [a, 0, 4, 4, 4, 0, 4, 0, 0, 0, 4,, 0, 0, 0, a],
                        # [a, 0, 4, 4, 4, 0, 4, 0, 0, 0, 4,, 0, 0, 0, a],
                        [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
                    ]).T
    # gridnp = np.array([[0]*43 for i in range(43)]).T
    # for i in range(len(gridnp)):
    #     for j in range(len(gridnp[i])):
    #         gridnp[i][j] = randint(0, 5)%5
    # for i in gridnp
    # gridnp = list(gridnp)
    # for i in range(len(gridnp)):
    #     gridnp[i] = list(gridnp[i])
    
    # gridnp.insert(0, ['a']*len(gridnp[0]))
    # gridnp.insert(len(gridnp), ['a']*len(gridnp[0]))

    # for i in gridnp:
    #     i.insert(0, 'a')
    #     i.insert(len(i), 'a')
    #     print(i)
    # print(gridnp)
    return gridnp

# home()