# Extraction of coordinates by ABINIT
# Coded by Takuro TOKUNAGA
# Last modified: August 10 2020

import numpy as np
import pandas as pd
import time
import scipy.io

start = time.time()

def comments():
    print ("extracting coordinate..")

def begin():
    print ("begin")

def end():
    print ("end")

# main
comments()
begin()

# read files
f1 = open("au_4c.out", 'r')               # read mode
f2 = open("ABINIT_coordinates.txt", 'w') # write mode

#
lines = [line for line in f1]

# extract force constant matrices
s = ' with coordinates '
for line in lines:
    if s in line:
        #line.split(" ", 4)
        r1 = line.replace('   ', ' ')
        r2 = r1.replace('    ', ' ')
        r3 = r1.replace('  ', ' ')
        f2.write(r3.strip(s)) # do not remove this line.

# close
f1.close
f2.close

# end
end()

# time display
elapsed_time = time.time()-start
print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")
