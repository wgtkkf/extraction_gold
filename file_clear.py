# Coded by Takuro TOKUNAGA
# Last modified: March 11, 2020

import time
import os
import glob

start = time.time()

def comments():
    print ("Removing old files..")

def comments_input():
    print ("Input >> how many au_4c_## files? (0,4,8,..)")

def begin():
    print ("begin")

def end():
    print ("end")

path_abinit = "/Users/Takuro/codes/enfht/abinit_gold_112/"

# main
comments_input()
file_num_keyboard = input()
file_num = int(file_num_keyboard) # number of atom's in the primitive cell

comments()
begin()


for file in glob.glob(path_abinit + 'small_mat_center_au/*.txt', recursive=True):
    os.remove(file)

for file in glob.glob(path_abinit + 'total_mat_au_L/*.txt', recursive=True):
    os.remove(file)

for file in glob.glob(path_abinit + 'total_mat_au_R/*.txt', recursive=True):
    os.remove(file)

for file in glob.glob(path_abinit + 'total_mat_au_C/*.txt', recursive=True):
    os.remove(file)

# LAMMPS unit folder
for file in glob.glob(path_abinit + 'total_mat_au_L/LAMMPS_unit/*.txt', recursive=True):
    os.remove(file)

for file in glob.glob(path_abinit + 'total_mat_au_R/LAMMPS_unit/*.txt', recursive=True):
    os.remove(file)

for file in glob.glob(path_abinit + 'total_mat_au_C/LAMMPS_unit/*.txt', recursive=True):
    os.remove(file)

if file_num!=0:
    for i in range(0,file_num):
        os.remove(path_abinit + "au_4c_"+str(i+1)+".txt")
elif file_num==0:
    exit

# end
end()

# time display
elapsed_time = time.time()-start
print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")
