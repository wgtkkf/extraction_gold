# Coded by Takuro TOKUNAGA
# Last modified: April 26, 2020

import numpy as np
import cmath
import time
import sys
import copy
sys.path.append('../abinit_gold_112/')
from fcmat_au_c_GA1_function import GA1   # import function
from fcmat_au_c_GA2_function import GA2   # import function
from fcmat_au_c_GA3_function import GA3   # import function
from fcmat_au_c_GA4_function import GA4   # import function
from fcmat_au_c_GA5_function import GA5   # import function
from fcmat_au_c_GA6_function import GA6   # import function
from fcmat_au_c_GA7_function import GA7   # import function
from fcmat_au_c_GA8_function import GA8   # import function
from coordinate_adjustment import adjustment # import function
from coordinate_shift import shift           # import function

start = time.time()

def begin():
    print ("begin")

def comments():
    print ("extracting..")

def end():
    print ("end")

# unit conversion
ucangs = 1.0*np.power(10.,-10) # [m]
ucbohr = 0.529177249*np.power(10.,-10) # [m]

# gold parameters (do not change)
dof = 3                      # [-], dgree of freedom
lcau = 4.065*ucangs          # [m]
lcau_bohr = lcau/ucbohr      # [bohr]

# read generic coordinates from ABINIT input
generic_coordinates_input=[list(map(np.float64,line.rstrip().split(" "))) for line in open("ABINIT_generic_atoms_coordinates_input.txt").readlines()]
# read generic coordinates from ABINIT output
generic_coordinates_output=[list(map(np.float64,line.rstrip().split(" "))) for line in open("ABINIT_generic_atoms_coordinates_output.txt").readlines()]

# primitive cell atom's coordinates
coordinate1 = np.zeros(dof, dtype='float64')
coordinate2 = np.zeros(dof, dtype='float64')
coordinate3 = np.zeros(dof, dtype='float64')
coordinate4 = np.zeros(dof, dtype='float64')
coordinate5 = np.zeros(dof, dtype='float64')
coordinate6 = np.zeros(dof, dtype='float64')
coordinate7 = np.zeros(dof, dtype='float64')
coordinate8 = np.zeros(dof, dtype='float64')

# primitive cell atom's coordinates by ABNINIT output
ab_coordinate1 = np.zeros(dof, dtype='float64')
ab_coordinate2 = np.zeros(dof, dtype='float64')
ab_coordinate3 = np.zeros(dof, dtype='float64')
ab_coordinate4 = np.zeros(dof, dtype='float64')
ab_coordinate5 = np.zeros(dof, dtype='float64')
ab_coordinate6 = np.zeros(dof, dtype='float64')
ab_coordinate7 = np.zeros(dof, dtype='float64')
ab_coordinate8 = np.zeros(dof, dtype='float64')

# comments
comments()

# main
begin()

# initialization of generic coordinates
for i in range(0, dof):
    # input for ABINIT
    coordinate1[i] = generic_coordinates_input[0][i] # 1
    coordinate2[i] = generic_coordinates_input[1][i] # 2
    coordinate3[i] = generic_coordinates_input[2][i] # 3
    coordinate4[i] = generic_coordinates_input[3][i] # 4

    coordinate5[i] = generic_coordinates_input[4][i] # 5
    coordinate6[i] = generic_coordinates_input[5][i] # 6
    coordinate7[i] = generic_coordinates_input[6][i] # 7
    coordinate8[i] = generic_coordinates_input[7][i] # 8

    # output by ABINIT
    ab_coordinate1[i] = generic_coordinates_output[0][i] # 1
    ab_coordinate2[i] = generic_coordinates_output[1][i] # 2
    ab_coordinate3[i] = generic_coordinates_output[2][i] # 3
    ab_coordinate4[i] = generic_coordinates_output[3][i] # 4

    ab_coordinate5[i] = generic_coordinates_output[4][i] # 5
    ab_coordinate6[i] = generic_coordinates_output[5][i] # 6
    ab_coordinate7[i] = generic_coordinates_output[6][i] # 7
    ab_coordinate8[i] = generic_coordinates_output[7][i] # 8

# shift factor by ABINIT
sf1 = shift(coordinate1, ab_coordinate1) # shift factor for atom 1
sf2 = shift(coordinate2, ab_coordinate2) # shift factor for atom 2
sf3 = shift(coordinate3, ab_coordinate3) # shift factor for atom 3
sf4 = shift(coordinate4, ab_coordinate4) # shift factor for atom 4
sf5 = shift(coordinate5, ab_coordinate5) # shift factor for atom 5
sf6 = shift(coordinate6, ab_coordinate6) # shift factor for atom 6
sf7 = shift(coordinate7, ab_coordinate7) # shift factor for atom 7
sf8 = shift(coordinate8, ab_coordinate8) # shift factor for atom 8

# s_: shift
s_coordinate1 = np.zeros(dof, dtype='float64')
s_coordinate2 = np.zeros(dof, dtype='float64')
s_coordinate3 = np.zeros(dof, dtype='float64')
s_coordinate4 = np.zeros(dof, dtype='float64')
s_coordinate5 = np.zeros(dof, dtype='float64')
s_coordinate6 = np.zeros(dof, dtype='float64')
s_coordinate7 = np.zeros(dof, dtype='float64')
s_coordinate8 = np.zeros(dof, dtype='float64')

for k in range(-1, 2, 1): # zloop (-1 -> 0 -> +1)
    #print(str(k))
    #print(str(coordinate1))
    s_coordinate1[2] = coordinate1[2] + (2*k)*lcau_bohr
    s_coordinate2[2] = coordinate2[2] + (2*k)*lcau_bohr
    s_coordinate3[2] = coordinate3[2] + (2*k)*lcau_bohr
    s_coordinate4[2] = coordinate4[2] + (2*k)*lcau_bohr
    s_coordinate5[2] = coordinate5[2] + (2*k)*lcau_bohr
    s_coordinate6[2] = coordinate6[2] + (2*k)*lcau_bohr
    s_coordinate7[2] = coordinate7[2] + (2*k)*lcau_bohr
    s_coordinate8[2] = coordinate8[2] + (2*k)*lcau_bohr

    for i in range(-1, 2, 1): # xloop (-1 -> 0 -> +1)
        s_coordinate1[0] = coordinate1[0] + i*lcau_bohr
        s_coordinate2[0] = coordinate2[0] + i*lcau_bohr
        s_coordinate3[0] = coordinate3[0] + i*lcau_bohr
        s_coordinate4[0] = coordinate4[0] + i*lcau_bohr
        s_coordinate5[0] = coordinate5[0] + i*lcau_bohr
        s_coordinate6[0] = coordinate6[0] + i*lcau_bohr
        s_coordinate7[0] = coordinate7[0] + i*lcau_bohr
        s_coordinate8[0] = coordinate8[0] + i*lcau_bohr

        for j in range(-1, 2, 1): # yloop (-1 -> 0 -> +1)
            s_coordinate1[1] = coordinate1[1] + j*lcau_bohr
            s_coordinate2[1] = coordinate2[1] + j*lcau_bohr
            s_coordinate3[1] = coordinate3[1] + j*lcau_bohr
            s_coordinate4[1] = coordinate4[1] + j*lcau_bohr
            s_coordinate5[1] = coordinate5[1] + j*lcau_bohr
            s_coordinate6[1] = coordinate6[1] + j*lcau_bohr
            s_coordinate7[1] = coordinate7[1] + j*lcau_bohr
            s_coordinate8[1] = coordinate8[1] + j*lcau_bohr

            # GA1
            GA1(i,j,k,adjustment(s_coordinate1+sf1),adjustment(s_coordinate2+sf1),\
            adjustment(s_coordinate3+sf1),adjustment(s_coordinate4+sf1),adjustment(s_coordinate5+sf1),\
            adjustment(s_coordinate6+sf1),adjustment(s_coordinate7+sf1),adjustment(s_coordinate8+sf1))

            # GA2
            GA2(i,j,k, adjustment(s_coordinate1+sf2),adjustment(s_coordinate2+sf2),\
            adjustment(s_coordinate3+sf2),adjustment(s_coordinate4+sf2),adjustment(s_coordinate5+sf2),\
            adjustment(s_coordinate6+sf2),adjustment(s_coordinate7+sf2),adjustment(s_coordinate8+sf2))

            # GA3
            GA3(i,j,k, adjustment(s_coordinate1+sf3),adjustment(s_coordinate2+sf3),\
            adjustment(s_coordinate3+sf3),adjustment(s_coordinate4+sf3),adjustment(s_coordinate5+sf3),\
            adjustment(s_coordinate6+sf3),adjustment(s_coordinate7+sf3),adjustment(s_coordinate8+sf3))

            # GA4
            GA4(i,j,k, adjustment(s_coordinate1+sf4),adjustment(s_coordinate2+sf4),\
            adjustment(s_coordinate3+sf4),adjustment(s_coordinate4+sf4),adjustment(s_coordinate5+sf4),\
            adjustment(s_coordinate6+sf4),adjustment(s_coordinate7+sf4),adjustment(s_coordinate8+sf4))

            # GA5
            GA5(i,j,k, adjustment(s_coordinate1+sf5),adjustment(s_coordinate2+sf5),\
            adjustment(s_coordinate3+sf5),adjustment(s_coordinate4+sf5),adjustment(s_coordinate5+sf5),\
            adjustment(s_coordinate6+sf5),adjustment(s_coordinate7+sf5),adjustment(s_coordinate8+sf5))

            # GA6
            GA6(i,j,k, adjustment(s_coordinate1+sf6),adjustment(s_coordinate2+sf6),\
            adjustment(s_coordinate3+sf6),adjustment(s_coordinate4+sf6),adjustment(s_coordinate5+sf6),\
            adjustment(s_coordinate6+sf6),adjustment(s_coordinate7+sf6),adjustment(s_coordinate8+sf6))

            # GA7
            GA7(i,j,k, adjustment(s_coordinate1+sf7),adjustment(s_coordinate2+sf7),\
            adjustment(s_coordinate3+sf7),adjustment(s_coordinate4+sf7),adjustment(s_coordinate5+sf7),\
            adjustment(s_coordinate6+sf7),adjustment(s_coordinate7+sf7),adjustment(s_coordinate8+sf7))

            # GA8
            GA8(i,j,k, adjustment(s_coordinate1+sf8),adjustment(s_coordinate2+sf8),\
            adjustment(s_coordinate3+sf8),adjustment(s_coordinate4+sf8),adjustment(s_coordinate5+sf8),\
            adjustment(s_coordinate6+sf8),adjustment(s_coordinate7+sf8),adjustment(s_coordinate8+sf8))

            # initialize to primitive cell coordinate, y direction
            for l in range(0, dof): # yloop
                if l==1:
                    s_coordinate1[l] = coordinate1[l]
                    s_coordinate2[l] = coordinate2[l]
                    s_coordinate3[l] = coordinate3[l]
                    s_coordinate4[l] = coordinate4[l]
                    s_coordinate5[l] = coordinate5[l]
                    s_coordinate6[l] = coordinate6[l]
                    s_coordinate7[l] = coordinate7[l]
                    s_coordinate8[l] = coordinate8[l]

        # initialize to primitive cell coordinate, x & y direction
        for m in range(0, dof): # x & y loop
            if m==0 or m==1:
                s_coordinate1[m] = coordinate1[m]
                s_coordinate2[m] = coordinate2[m]
                s_coordinate3[m] = coordinate3[m]
                s_coordinate4[m] = coordinate4[m]
                s_coordinate5[m] = coordinate5[m]
                s_coordinate6[m] = coordinate6[m]
                s_coordinate7[m] = coordinate7[m]
                s_coordinate8[m] = coordinate8[m]

    # initialize to primitive cell coordinate, x y z direction
    for n in range(0, dof): # x, y & z loop
        s_coordinate1[n] = coordinate1[n]
        s_coordinate2[n] = coordinate2[n]
        s_coordinate3[n] = coordinate3[n]
        s_coordinate4[n] = coordinate4[n]
        s_coordinate5[n] = coordinate5[n]
        s_coordinate6[n] = coordinate6[n]
        s_coordinate7[n] = coordinate7[n]
        s_coordinate8[n] = coordinate8[n]

# end
end()

# time display
elapsed_time = time.time()-start
print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")
