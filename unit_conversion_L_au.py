# force constant matrix generation code from ABINIT output
# Coded by Takuro TOKUNAGA
# Last modified: April 25 2020

import numpy as np
import pandas as pd
import time
#import itertools

start = time.time()

# Unit conversion: atomic unit
hartree = 27.2113961 # [eV]
bohr = 0.529177249 # [angs]

# ABINIT to LAMMPS
ABINIT_LAMMPS = hartree/np.power(bohr,2.0) # eV/Angs

def comments():
    print ("unit converting..")

def begin():
    print ("begin")

def end():
    print ("end")

comments()

# main
begin()

# K00L
for i in range(-1, 2, 1): # xloop
    for j in range(-1, 2, 1): # yloop

        K00L = pd.read_csv("../abinit_gold_112/total_mat_au_L/K00L_"+str(i)+str(j)+".txt", sep='\s+', header=None)
        K00L = K00L*ABINIT_LAMMPS # unit conversion
        row,col = K00L.shape # get row & column of matorix

        f1 = open("../abinit_gold_112/total_mat_au_L/LAMMPS_unit/K00L_"+str(i)+str(j)+".txt", 'w') # write mode
        for k in range(0, row): # 48
            for l in range(0, col): # 48
                f1.write(str(K00L[l][k])) # l & k are flipped maybe due to pd.read specification
                f1.write(str(' '))
            f1.write('\n')

# K01L
for i in range(-1, 2, 1): # xloop
    for j in range(-1, 2, 1): # yloop
        K01L = pd.read_csv("../abinit_gold_112/total_mat_au_L/K01L_"+str(i)+str(j)+".txt", sep='\s+', header=None)
        K01L = K01L*ABINIT_LAMMPS # unit conversion
        row,col = K01L.shape # get row & column of matorix

        f2 = open("../abinit_gold_112/total_mat_au_L/LAMMPS_unit/K01L_"+str(i)+str(j)+".txt", 'w') # write mode
        for k in range(0, row): # 48
            for l in range(0, col): # 48
                f2.write(str(K01L[l][k])) # l & k are flipped maybe due to pd.read specification
                f2.write(str(' '))
            f2.write('\n')

# K10L
for i in range(-1, 2, 1): # xloop
    for j in range(-1, 2, 1): # yloop
        K10L = pd.read_csv("../abinit_gold_112/total_mat_au_L/K10L_"+str(i)+str(j)+".txt", sep='\s+', header=None)
        K10L = K10L*ABINIT_LAMMPS # unit conversion
        row,col = K10L.shape # get row & column of matorix

        f3 = open("../abinit_gold_112/total_mat_au_L/LAMMPS_unit/K10L_"+str(i)+str(j)+".txt", 'w') # write mode
        for k in range(0, row): # 48
            for l in range(0, col): # 48
                f3.write(str(K10L[l][k])) # l & k are flipped maybe due to pd.read specification
                f3.write(str(' '))
            f3.write('\n')

# end
f1.close
f2.close
f3.close
end()

# time display
elapsed_time = time.time()-start
print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")
