import os
import numpy as np

XRES, YRES = os.get_terminal_size()

NUMCOLS = 7

COLOURS = ["\033[3" + str(i) + "m" for i in range(NUMCOLS + 1)]

ITERS = 32

XMIN = -2
XMAX = 1
YMIN = -1.5
YMAX = 1.5

#Generate the matrix of complex numbers
A = (np.reshape(np.linspace(YMAX, YMIN, YRES), (YRES, 1)) * 1j + np.linspace(XMIN, XMAX, XRES))

def inSet(p):
    i = 0
    p0 = p
    while i < ITERS:
        p = p*p + p0
        if(abs(p) > 4):
            return i
        i += 1
    return i

v = np.vectorize(inSet)

#Test to see which points are in the set, storing their final iteration count and then mapping that to a bin index
B = np.digitize(v(A), [i * ITERS/NUMCOLS for i in range(0, NUMCOLS)])

#Print
for i in B:
    for j in i:
        if j == 1:
            print(' ', end='')
        else:
            print(COLOURS[j] + "#", end='')
