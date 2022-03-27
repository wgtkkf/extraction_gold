# force constant matrix generation code from ABINIT output
# Coded by Takuro TOKUNAGA
# Last modified: April 25 2020

import numpy as np
import shutil
import os
import time

start = time.time()

def begin():
    print ("begin")

def comments():
    print ("copy & rename..")

def end():
    print ("end")

# comments
comments()

# main
begin()

for i in range(-1, 2, 1): # zloop
    for j in range(-1, 2, 1): # xloop
        for k in range(-1, 2, 1): # yloop
            if i==-1:
                shutil.copy("../abinit_gold_112/total_mat_au_L/K10L_"+str(j)+str(k)+".txt",\
                "../abinit_gold_112/total_mat_au_R/K10R_"+str(j)+str(k)+".txt")   # from to
            elif i==0:
                shutil.copy("../abinit_gold_112/total_mat_au_L/K00L_"+str(j)+str(k)+".txt",\
                "../abinit_gold_112/total_mat_au_R/K00R_"+str(j)+str(k)+".txt")   # from to
            else:
                shutil.copy("../abinit_gold_112/total_mat_au_L/K01L_"+str(j)+str(k)+".txt",\
                "../abinit_gold_112/total_mat_au_R/K01R_"+str(j)+str(k)+".txt")   # from to

# end
end()

# time display
elapsed_time = time.time()-start
print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")
