# force constant matrix generation code from ABINIT output
# Coded by Takuro TOKUNAGA
# Last modified: April 26 2020

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

# comments
comments()

# main
begin()

# KC
for i in range(-1, 2, 1): # xloop
    for j in range(-1, 2, 1): # yloop

        KC = pd.read_csv("../abinit_gold_112/total_mat_au_C/KC_"+str(i)+str(j)+".txt", sep='\s+', header=None)
        KC = KC*ABINIT_LAMMPS # unit conversion
        row,col = KC.shape # get row & column of matorix

        f1 = open("../abinit_gold_112/total_mat_au_C/LAMMPS_unit/KC_"+str(i)+str(j)+".txt", 'w') # write mode
        for k in range(0, row): # 48
            for l in range(0, col): # 48
                f1.write(str(KC[l][k])) # l & k are flipped maybe due to pd.read specification
                f1.write(str(' '))
            f1.write('\n')

# V_CL
for i in range(-1, 2, 1): # xloop
    for j in range(-1, 2, 1): # yloop
        V_CL = pd.read_csv("../abinit_gold_112/total_mat_au_C/V_CL_"+str(i)+str(j)+".txt", sep='\s+', header=None)
        V_CL = V_CL*ABINIT_LAMMPS # unit conversion
        row,col = V_CL.shape # get row & column of matorix

        f2 = open("../abinit_gold_112/total_mat_au_C/LAMMPS_unit/V_CL_"+str(i)+str(j)+".txt", 'w') # write mode
        for k in range(0, row): # 48
            for l in range(0, col): # 24
                f2.write(str(V_CL[l][k])) # l & k are flipped maybe due to pd.read specification
                f2.write(str(' '))
            f2.write('\n')

# V_CR
for i in range(-1, 2, 1): # xloop
    for j in range(-1, 2, 1): # yloop
        V_CR = pd.read_csv("../abinit_gold_112/total_mat_au_C/V_CR_"+str(i)+str(j)+".txt", sep='\s+', header=None)
        V_CR = V_CR*ABINIT_LAMMPS # unit conversion
        row,col = V_CR.shape # get row & column of matorix

        f3 = open("../abinit_gold_112/total_mat_au_C/LAMMPS_unit/V_CR_"+str(i)+str(j)+".txt", 'w') # write mode
        for k in range(0, row): # 48
            for l in range(0, col): # 24
                f3.write(str(V_CR[l][k])) # l & k are flipped maybe due to pd.read specification
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
