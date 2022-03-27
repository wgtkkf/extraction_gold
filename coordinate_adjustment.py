# atomic coordinates for lead & scattering region
# Si conventional lattice
# Last modified: May 10 2020
# Coded by Takuro TOKUNAGA

import numpy as np
import time
import linecache
import pandas as pd
start = time.time()

# functions for begin & finish
def adjustment(arg_coord):
    dof = 3        # degree of freedom
#    criteria = 0.3 # criteria [bohr]
#    criteria = 1.0 # criteria [bohr]
    criteria = 0.9 # criteria [bohr]
    adjusted = np.zeros(dof, dtype='float64')

    # read ABINIT coordinate
    ABINIT_coord = pd.read_csv("ABINIT_coordinates.txt", sep=" ", header=None)
    #print(ABINIT_coord)
    ABINIT_coord.columns = ["x", "y", "z"] # from .txt data
    row, col = ABINIT_coord.shape          # row & column of matorix
    #print(row)

    x = np.zeros(row, dtype='float64')
    y = np.zeros(row, dtype='float64')
    z = np.zeros(row, dtype='float64')

    # counter
    #counter = 0

    for i in range(0, row):
        x[i] = ABINIT_coord.iat[i,0] # x line, ABINIT x coordinate
        y[i] = ABINIT_coord.iat[i,1] # y line, ABINIT y coordinate
        z[i] = ABINIT_coord.iat[i,2] # z line, ABINIT z coordinate

        dif_x = abs(arg_coord[0]-x[i])
        dif_y = abs(arg_coord[1]-y[i])
        dif_z = abs(arg_coord[2]-z[i])

        if dif_x < criteria and dif_y < criteria and dif_z < criteria:
            adjusted[0] = x[i]
            adjusted[1] = y[i]
            adjusted[2] = z[i]

        #counter += 1
        #if counter > row:
        #    break

    return adjusted

# coordinate

# time display
elapsed_time = time.time()-start
#print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")
