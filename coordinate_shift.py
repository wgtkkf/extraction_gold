# Last modified: May 12 2020
# Last updated: September 24 2020
# Coded by Takuro TOKUNAGA

import numpy as np
import time
import linecache
import pandas as pd
start = time.time()

# functions for begin & finish
def shift(arg_coord_input, arg_coord_output):
    dof = 3        # degree of freedom
    criteria = 0.3 # criteria [bohr]
    difference = np.zeros(dof, dtype='float64')
    s_factor = np.zeros(dof, dtype='float64')

    difference = arg_coord_output - arg_coord_input

    for i in range(0, dof):
        if abs(difference[i]) < criteria:
            s_factor[i] = 0
        else:
            s_factor[i] = difference[i]

    # show
    #print(s_factor)

    return s_factor # shift factor

# coordinate

# time display
elapsed_time = time.time()-start
#print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")
