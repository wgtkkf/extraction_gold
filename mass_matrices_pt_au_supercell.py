# Mass matrices (ML/MC/MR)
# Coded by Takuro TOKUNAGA
# Last modified: April 26 2020

import numpy as np
import pandas as pd
import time
import scipy.io
#import itertools

start = time.time()

def comments():
    print ("mass matrices..")

def begin():
    print ("begin")

def end():
    print ("end")

# comments
comments()

# main
begin()

dof = 3                 # degree of freedom, [-]
atom_num = 4            # number of atom's in the primitive cell
size= atom_num*dof      # matrix size, [-]
atom_num2 = atom_num*2  # number of atom's in the super cell
size2= atom_num2*dof    # matrix size, [-]
gold_mass = 196.96657   # [amu]
platinum_mass = 195.084 # [amu]

mass1=np.zeros((size2,size2), dtype=np.float64) # 24 24
mass2=np.zeros((size2,size2), dtype=np.float64) # 48 48

f1 = open("../abinit_gold_112/ML_au.txt", 'w') # write mode
f2 = open("../abinit_gold_112/MR_au.txt", 'w') # write mode
f3 = open("../abinit_gold_112/MC_au.txt", 'w') # write mode

# initialization
# ML & MR
for i in range(0, size2):
    for j in range(0, size2):
        if i==j:
            mass1[i][j] = platinum_mass
            mass2[i][j] = gold_mass

# output (ML & MR)
for i in range(0, size2): # 48
    for j in range(0, size2): # 48
        f1.write(str(mass1[i][j]))
        f1.write(str(' '))

        f2.write(str(mass2[i][j]))
        f2.write(str(' '))

    f1.write('\n')
    f2.write('\n')

# initialization
# MC
# Pt/Au anti-symmetric system
for i in range(0, size2):
    for j in range(0, size2):
        if i<int(size2*0.5) and i==j:
            mass2[i][j] = platinum_mass
        elif i==j:
            mass2[i][j] = gold_mass

# output (MC)
for i in range(0, size2): # 48
    for j in range(0, size2): # 48
        f3.write(str(mass2[i][j]))
        f3.write(str(' '))
    f3.write('\n')

# close
f1.close
f2.close
f3.close

# end
end()

# time display
elapsed_time = time.time()-start
print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")
