# force constant matrix generation code from ABINIT output
# Coded by Takuro TOKUNAGA
# Last modified: April 26 2020

import numpy as np
import cmath
import pandas as pd
import time
import scipy.io
import itertools

start = time.time()

def begin():
    print ("begin")

def comments():
    print ("splitting..")

def end():
    print ("end")

dof = 3            # degree of freedom, [-]
atom_num = 8       # number of atom's in the super cell, [-]
size= atom_num*dof # matrix size, [-]
galine = np.zeros(atom_num,dtype=np.int64) # generic atom lines

# comments
comments()

# main
begin()

f1 = open('au_4c.out', 'r')    # read mode

#for line1 in f1: # display si_4.out
#    print(str(line1))

lines = [line for line in f1]
# full line length
full_length = len(open('au_4c.out').readlines())
#print(str(full_length))

counter = 1
# extract force constant matrices
for i in lines:
    if 'generic atom number   '+str(counter) in i:
        galine[counter-1] = lines.index(i)
        #print(lines.index(i))
        counter += 1
    elif 'generic atom number  '+str(counter) in i:
        galine[counter-1] = lines.index(i)
        counter += 1

#print(str(galine))
# generic atom number 1~16

for i in range(0,atom_num):
    f2 = open("au_4c_"+str(i+1)+".txt","w")
    if i<atom_num-1:
        for line in itertools.islice(lines, int(galine[i]), int(galine[i+1])):
            f2.write(line)
    else:
        for line in itertools.islice(lines, int(galine[i]), int(full_length)):
            f2.write(line)

    f2.close()

# file close
f1.close()
f2.close()

# end
end()

# time display
elapsed_time = time.time()-start
print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")
