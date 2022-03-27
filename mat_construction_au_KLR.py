# force constant matrix generation code from ABINIT output
# Coded by Takuro TOKUNAGA
# Last modified: FebruarySeptember 11 2019

import numpy as np
import pandas as pd
import time
import scipy.io
#import itertools

start = time.time()

def comments():
    print ("merging..")

def begin():
    print ("begin")

def end():
    print ("end")

# comments
comments()

# main
begin()

dof = 3            # degree of freedom, [-]
atom_num = 8       # number of atom's in the supercell, [-]
size= atom_num*dof # matrix size
matrix1=np.zeros((dof,dof), dtype=np.float64) # 3 3
matrix2=np.zeros((dof,dof), dtype=np.float64) # 3 3
matrix3=np.zeros((dof,dof), dtype=np.float64) # 3 3
matrix4=np.zeros((dof,dof), dtype=np.float64) # 3 3
matrix5=np.zeros((dof,dof), dtype=np.float64) # 3 3
matrix6=np.zeros((dof,dof), dtype=np.float64) # 3 3
matrix7=np.zeros((dof,dof), dtype=np.float64) # 3 3
matrix8=np.zeros((dof,dof), dtype=np.float64) # 3 3
mat_tot=np.zeros((size,size), dtype=np.float64) # 24 24

# read files
for n in range(-1, 2, 1): # zloop
    for o in range(-1, 2, 1): # xloop
        for p in range(-1, 2, 1): # yloop
            # open file for output
            if n==-1:
                f1 = open("../abinit_gold_112/total_mat_au_L/K10L_"+str(o)+str(p)+".txt", 'w') # write mode
            elif n==0:
                f1 = open("../abinit_gold_112/total_mat_au_L/K00L_"+str(o)+str(p)+".txt", 'w') # write mode
            else: # n==1
                f1 = open("../abinit_gold_112/total_mat_au_L/K01L_"+str(o)+str(p)+".txt", 'w') # write mode

            for i in range(0, atom_num): # 0~7
                if n==-1:
                    mat1 = pd.read_csv("../abinit_gold_112/small_mat_center_au/au_4_SS"+str(i+1)+"_SS1_K10_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat1.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat2 = pd.read_csv("../abinit_gold_112/small_mat_center_au/au_4_SS"+str(i+1)+"_SS2_K10_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat2.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat3 = pd.read_csv("../abinit_gold_112/small_mat_center_au/au_4_SS"+str(i+1)+"_SS3_K10_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat3.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat4 = pd.read_csv("../abinit_gold_112/small_mat_center_au/au_4_SS"+str(i+1)+"_SS4_K10_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat4.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat5 = pd.read_csv("../abinit_gold_112/small_mat_center_au/au_4_SS"+str(i+1)+"_SS5_K10_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat5.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat6 = pd.read_csv("../abinit_gold_112/small_mat_center_au/au_4_SS"+str(i+1)+"_SS6_K10_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat6.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat7 = pd.read_csv("../abinit_gold_112/small_mat_center_au/au_4_SS"+str(i+1)+"_SS7_K10_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat7.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat8 = pd.read_csv("../abinit_gold_112/small_mat_center_au/au_4_SS"+str(i+1)+"_SS8_K10_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat8.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]

                elif n==0:
                    mat1 = pd.read_csv("../abinit_gold_112/small_mat_center_au/au_4_SS"+str(i+1)+"_SS1_K00_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat1.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat2 = pd.read_csv("../abinit_gold_112/small_mat_center_au/au_4_SS"+str(i+1)+"_SS2_K00_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat2.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat3 = pd.read_csv("../abinit_gold_112/small_mat_center_au/au_4_SS"+str(i+1)+"_SS3_K00_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat3.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat4 = pd.read_csv("../abinit_gold_112/small_mat_center_au/au_4_SS"+str(i+1)+"_SS4_K00_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat4.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat5 = pd.read_csv("../abinit_gold_112/small_mat_center_au/au_4_SS"+str(i+1)+"_SS5_K00_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat5.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat6 = pd.read_csv("../abinit_gold_112/small_mat_center_au/au_4_SS"+str(i+1)+"_SS6_K00_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat6.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat7 = pd.read_csv("../abinit_gold_112/small_mat_center_au/au_4_SS"+str(i+1)+"_SS7_K00_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat7.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat8 = pd.read_csv("../abinit_gold_112/small_mat_center_au/au_4_SS"+str(i+1)+"_SS8_K00_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat8.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]

                else: # n==-1
                    mat1 = pd.read_csv("../abinit_gold_112/small_mat_center_au/au_4_SS"+str(i+1)+"_SS1_K01_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat1.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat2 = pd.read_csv("../abinit_gold_112/small_mat_center_au/au_4_SS"+str(i+1)+"_SS2_K01_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat2.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat3 = pd.read_csv("../abinit_gold_112/small_mat_center_au/au_4_SS"+str(i+1)+"_SS3_K01_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat3.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat4 = pd.read_csv("../abinit_gold_112/small_mat_center_au/au_4_SS"+str(i+1)+"_SS4_K01_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat4.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat5 = pd.read_csv("../abinit_gold_112/small_mat_center_au/au_4_SS"+str(i+1)+"_SS5_K01_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat5.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat6 = pd.read_csv("../abinit_gold_112/small_mat_center_au/au_4_SS"+str(i+1)+"_SS6_K01_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat6.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat7 = pd.read_csv("../abinit_gold_112/small_mat_center_au/au_4_SS"+str(i+1)+"_SS7_K01_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat7.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]
                    mat8 = pd.read_csv("../abinit_gold_112/small_mat_center_au/au_4_SS"+str(i+1)+"_SS8_K01_"+str(o)+str(p)+".txt", sep='\s+', header=None)
                    mat8.columns = ["x", "y", "z", "x1", "y1", "z1", "x2", "y2", "z2"]

                row,col = mat1.shape # row (3) & column (9) of matorix

                for j in range(0, row):
                    for k in range(0, row):
                        matrix1[j][k] = mat1.iat[j,k]
                        matrix2[j][k] = mat2.iat[j,k]
                        matrix3[j][k] = mat3.iat[j,k]
                        matrix4[j][k] = mat4.iat[j,k]
                        matrix5[j][k] = mat5.iat[j,k]
                        matrix6[j][k] = mat6.iat[j,k]
                        matrix7[j][k] = mat7.iat[j,k]
                        matrix8[j][k] = mat8.iat[j,k]

                #print(matrix2)
                mat_tot_temp = np.concatenate([matrix1, matrix2, matrix3, matrix4,matrix5, matrix6, matrix7, matrix8], axis=1)
                #print(mat_tot)

                row,col = mat_tot_temp.shape # row (3) & column (24) of matorix
                #print(str(row))
                #print(str(col))

                # mat_tot: 48*24 matrix
                for l in range(0, dof): # 48
                    for m in range(0, size): # 3
                        mat_tot[dof*i+l][m] = mat_tot_temp[l][m] # 48*3

            # mat_tot: 48*48 matrix
            for l in range(0, size): # 48
                for m in range(0, size): # 48
                    f1.write(str(mat_tot[l][m]))
                    f1.write(str(' '))
                f1.write('\n')

        # close
        f1.close

# end
end()

# time display
elapsed_time = time.time()-start
print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")
