# force constant matrix extract & generation code from ABINIT output
# Coded by Takuro TOKUNAGA
# Last modified: April 26 2020

import numpy as np
import time
import scipy.io
import itertools

start = time.time()

def GA7(argi,argj,argk,arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8):

    dof = 3         # degree of freedom, [-]
    atom_num = 8    # number of atom's in the primitive cell, [-]
    size= atom_num*dof

    coord1 = arg1   # generic atom 1's coordinate
    coord2 = arg2   # generic atom 2's coordinate
    coord3 = arg3   # generic atom 3's coordinate
    coord4 = arg4   # generic atom 4's coordinate
    coord5 = arg5   # generic atom 5's coordinate
    coord6 = arg6   # generic atom 6's coordinate
    coord7 = arg7   # generic atom 7's coordinate
    coord8 = arg8   # generic atom 8's coordinate

    # file open, GA: Generic Atom, SS: Shiga Sensei
    if argk==-1:
        f1 =  open("../abinit_gold_112/small_mat_center_au/au_4_SS7_SS1_K10_"+str(argi)+str(argj)+".txt", 'w') # write mode
        f2 =  open("../abinit_gold_112/small_mat_center_au/au_4_SS7_SS2_K10_"+str(argi)+str(argj)+".txt", 'w') # write mode
        f3 =  open("../abinit_gold_112/small_mat_center_au/au_4_SS7_SS3_K10_"+str(argi)+str(argj)+".txt", 'w') # write mode
        f4 =  open("../abinit_gold_112/small_mat_center_au/au_4_SS7_SS4_K10_"+str(argi)+str(argj)+".txt", 'w') # write mode
        f5 =  open("../abinit_gold_112/small_mat_center_au/au_4_SS7_SS5_K10_"+str(argi)+str(argj)+".txt", 'w') # write mode
        f6 =  open("../abinit_gold_112/small_mat_center_au/au_4_SS7_SS6_K10_"+str(argi)+str(argj)+".txt", 'w') # write mode
        f7 =  open("../abinit_gold_112/small_mat_center_au/au_4_SS7_SS7_K10_"+str(argi)+str(argj)+".txt", 'w') # write mode
        f8 =  open("../abinit_gold_112/small_mat_center_au/au_4_SS7_SS8_K10_"+str(argi)+str(argj)+".txt", 'w') # write mode

    elif argk==0:
        f1 =  open("../abinit_gold_112/small_mat_center_au/au_4_SS7_SS1_K00_"+str(argi)+str(argj)+".txt", 'w') # write mode
        f2 =  open("../abinit_gold_112/small_mat_center_au/au_4_SS7_SS2_K00_"+str(argi)+str(argj)+".txt", 'w') # write mode
        f3 =  open("../abinit_gold_112/small_mat_center_au/au_4_SS7_SS3_K00_"+str(argi)+str(argj)+".txt", 'w') # write mode
        f4 =  open("../abinit_gold_112/small_mat_center_au/au_4_SS7_SS4_K00_"+str(argi)+str(argj)+".txt", 'w') # write mode
        f5 =  open("../abinit_gold_112/small_mat_center_au/au_4_SS7_SS5_K00_"+str(argi)+str(argj)+".txt", 'w') # write mode
        f6 =  open("../abinit_gold_112/small_mat_center_au/au_4_SS7_SS6_K00_"+str(argi)+str(argj)+".txt", 'w') # write mode
        f7 =  open("../abinit_gold_112/small_mat_center_au/au_4_SS7_SS7_K00_"+str(argi)+str(argj)+".txt", 'w') # write mode
        f8 =  open("../abinit_gold_112/small_mat_center_au/au_4_SS7_SS8_K00_"+str(argi)+str(argj)+".txt", 'w') # write mode

    elif argk==1:
        f1  = open("../abinit_gold_112/small_mat_center_au/au_4_SS7_SS1_K01_"+str(argi)+str(argj)+".txt", 'w') # write mode
        f2  = open("../abinit_gold_112/small_mat_center_au/au_4_SS7_SS2_K01_"+str(argi)+str(argj)+".txt", 'w') # write mode
        f3  = open("../abinit_gold_112/small_mat_center_au/au_4_SS7_SS3_K01_"+str(argi)+str(argj)+".txt", 'w') # write mode
        f4  = open("../abinit_gold_112/small_mat_center_au/au_4_SS7_SS4_K01_"+str(argi)+str(argj)+".txt", 'w') # write mode
        f5  = open("../abinit_gold_112/small_mat_center_au/au_4_SS7_SS5_K01_"+str(argi)+str(argj)+".txt", 'w') # write mode
        f6  = open("../abinit_gold_112/small_mat_center_au/au_4_SS7_SS6_K01_"+str(argi)+str(argj)+".txt", 'w') # write mode
        f7  = open("../abinit_gold_112/small_mat_center_au/au_4_SS7_SS7_K01_"+str(argi)+str(argj)+".txt", 'w') # write mode
        f8  = open("../abinit_gold_112/small_mat_center_au/au_4_SS7_SS8_K01_"+str(argi)+str(argj)+".txt", 'w') # write mode

    else:
        print(str('error'))

    # open
    f0 = open('au_4c_7.txt', 'r') # read mode
    # lines
    lines0 = [line for line in f0]

    # generic atom number 1
    moji1 = 'with coordinates'
    if coord1[0] >= 0:
        moji2 = '     ' # 5 space
        moji3 = "{:.6E}".format(round(coord1[0],6)) # atom1 x
    elif coord1[0] < 0:
        moji2 = '    ' # 4 space
        moji3 = "{:.6E}".format(round(coord1[0],6)) # atom1 x

    if coord1[1] >= 0:
        moji4 = '    ' # 4 space
        moji5 = "{:.6E}".format(round(coord1[1],6)) # atom1 y
    elif coord1[1] < 0:
        moji4 = '   ' # 3 space
        moji5 = "{:.6E}".format(round(coord1[1],6)) # atom1 y

    if coord1[2] >= 0:
        moji6 = '    ' # 4 space
        moji7 = "{:.6E}".format(round(coord1[2],6)) # atom1 z
    elif coord1[2] < 0:
        moji6 = '   ' # 3 space
        moji7 = "{:.6E}".format(round(coord1[2],6)) # atom1 z

    moji = moji1 + moji2 + moji3 + moji4 + moji5 + moji6 + moji7
    moji = str(moji)
    #print(moji)

    for i in lines0:
        if moji in i: # 1
            #print(lines0.index(i))
            for line in itertools.islice(lines0, int(lines0.index(i)+2), int(lines0.index(i)+5)):
                f1.write(line)
                #print(str(line))

    # generic atom number 2
    moji1 = 'with coordinates'
    if coord2[0] >= 0:
        moji2 = '     ' # 5 space
        moji3 = "{:.6E}".format(round(coord2[0],6)) # atom1 x
    elif coord2[0] < 0:
        moji2 = '    ' # 4 space
        moji3 = "{:.6E}".format(round(coord2[0],6)) # atom1 x

    if coord2[1] >= 0:
        moji4 = '    ' # 4 space
        moji5 = "{:.6E}".format(round(coord2[1],6)) # atom1 y
    elif coord2[1] < 0:
        moji4 = '   ' # 3 space
        moji5 = "{:.6E}".format(round(coord2[1],6)) # atom1 y

    if coord2[2] >= 0:
        moji6 = '    ' # 4 space
        moji7 = "{:.6E}".format(round(coord2[2],6)) # atom1 z

    elif coord2[2] < 0:
        moji6 = '   ' # 3 space
        moji7 = "{:.6E}".format(round(coord2[2],6)) # atom1 z

    moji = moji1 + moji2 + moji3 + moji4 + moji5 + moji6 + moji7
    moji = str(moji)

    # debug
    #if argi==0 and argj==0 and argk==1: # x y z
    #    print(moji)

    for i in lines0:
        if moji in i: # 2
            #print(lines0.index(i))
            for line in itertools.islice(lines0, int(lines0.index(i)+2), int(lines0.index(i)+5)):
                f2.write(line)
                #if argi==0 and argj==0 and argk==1: # x y z
                #    print(line)

    # generic atom number 3
    moji1 = 'with coordinates'
    if coord3[0] >= 0:
        moji2 = '     ' # 5 space
        moji3 = "{:.6E}".format(round(coord3[0],6)) # atom1 x
    elif coord3[0] < 0:
        moji2 = '    ' # 4 space
        moji3 = "{:.6E}".format(round(coord3[0],6)) # atom1 x

    if coord3[1] >= 0:
        moji4 = '    ' # 4 space
        moji5 = "{:.6E}".format(round(coord3[1],6)) # atom1 y
    elif coord3[1] < 0:
        moji4 = '   ' # 3 space
        moji5 = "{:.6E}".format(round(coord3[1],6)) # atom1 y

    if coord3[2] >= 0:
        moji6 = '    ' # 4 space
        moji7 = "{:.6E}".format(round(coord3[2],6)) # atom1 z
    elif coord3[2] < 0:
        moji6 = '   ' # 3 space
        moji7 = "{:.6E}".format(round(coord3[2],6)) # atom1 z

    moji = moji1 + moji2 + moji3 + moji4 + moji5 + moji6 + moji7
    moji = str(moji)
    #print(str(moji))

    for i in lines0:
        if moji in i: # 3
            #print(lines0.index(i))
            for line in itertools.islice(lines0, int(lines0.index(i)+2), int(lines0.index(i)+5)):
                f3.write(line)

    # generic atom number 4
    moji1 = 'with coordinates'
    if coord4[0] >= 0:
        moji2 = '     ' # 5 space
        moji3 = "{:.6E}".format(round(coord4[0],6)) # atom1 x
    elif coord4[0] < 0:
        moji2 = '    ' # 4 space
        moji3 = "{:.6E}".format(round(coord4[0],6)) # atom1 x

    if coord4[1] >= 0:
        moji4 = '    ' # 4 space
        moji5 = "{:.6E}".format(round(coord4[1],6)) # atom1 y
    elif coord4[1] < 0:
        moji4 = '   ' # 3 space
        moji5 = "{:.6E}".format(round(coord4[1],6)) # atom1 y

    if coord4[2] >= 0:
        moji6 = '    ' # 4 space
        moji7 = "{:.6E}".format(round(coord4[2],6)) # atom1 z

    elif coord4[2] < 0:
        moji6 = '   ' # 3 space
        moji7 = "{:.6E}".format(round(coord4[2],6)) # atom1 z

    moji = moji1 + moji2 + moji3 + moji4 + moji5 + moji6 + moji7
    moji = str(moji)

    # debug
    #if argi==0 and argj==0 and argk==1: # x y z
    #    print(moji)

    for i in lines0:
        if moji in i:
            #print(lines0.index(i))
            for line in itertools.islice(lines0, int(lines0.index(i)+2), int(lines0.index(i)+5)):
                f4.write(line)

                #if argi==0 and argj==0 and argk==1: # x y z
                #    print(line)

    # generic atom number 5
    moji1 = 'with coordinates'
    if coord5[0] >= 0:
        moji2 = '     ' # 5 space
        moji3 = "{:.6E}".format(round(coord5[0],6)) # atom1 x
    elif coord5[0] < 0:
        moji2 = '    ' # 4 space
        moji3 = "{:.6E}".format(round(coord5[0],6)) # atom1 x

    if coord5[1] >= 0:
        moji4 = '    ' # 4 space
        moji5 = "{:.6E}".format(round(coord5[1],6)) # atom1 y
    elif coord5[1] < 0:
        moji4 = '   ' # 3 space
        moji5 = "{:.6E}".format(round(coord5[1],6)) # atom1 y
    if coord5[2] >= 0:
        moji6 = '    ' # 4 space
        moji7 = "{:.6E}".format(round(coord5[2],6)) # atom1 z
    elif coord5[2] < 0:
        moji6 = '   ' # 3 space
        moji7 = "{:.6E}".format(round(coord5[2],6)) # atom1 z

    moji = moji1 + moji2 + moji3 + moji4 + moji5 + moji6 + moji7
    moji = str(moji)

    for i in lines0:
        if moji in i: # 5
            #print(lines0.index(i))
            for line in itertools.islice(lines0, int(lines0.index(i)+2), int(lines0.index(i)+5)):
                f5.write(line)

    # generic atom number 6
    moji1 = 'with coordinates'
    if coord6[0] >= 0:
        moji2 = '     ' # 5 space
        moji3 = "{:.6E}".format(round(coord6[0],6)) # atom1 x
    elif coord6[0] < 0:
        moji2 = '    ' # 4 space
        moji3 = "{:.6E}".format(round(coord6[0],6)) # atom1 x

    if coord6[1] >= 0:
        moji4 = '    ' # 4 space
        moji5 = "{:.6E}".format(round(coord6[1],6)) # atom1 y
    elif coord6[1] < 0:
        moji4 = '   ' # 3 space
        moji5 = "{:.6E}".format(round(coord6[1],6)) # atom1 y

    if coord6[2] >= 0:
        moji6 = '    ' # 4 space
        moji7 = "{:.6E}".format(round(coord6[2],6)) # atom1 z
    elif coord6[2] < 0:
        moji6 = '   ' # 3 space
        moji7 = "{:.6E}".format(round(coord6[2],6)) # atom1 z

    moji = moji1 + moji2 + moji3 + moji4 + moji5 + moji6 + moji7
    moji = str(moji)

    for i in lines0: # generic atom number 5, ABINIT
        if moji in i: # 6
            #print(lines0.index(i))
            for line in itertools.islice(lines0, int(lines0.index(i)+2), int(lines0.index(i)+5)):
                f6.write(line)

    # generic atom number 7
    moji1 = 'with coordinates'
    if coord7[0] >= 0:
        moji2 = '     ' # 5 space
        moji3 = "{:.6E}".format(round(coord7[0],6)) # atom1 x
    elif coord7[0] < 0:
        moji2 = '    ' # 4 space
        moji3 = "{:.6E}".format(round(coord7[0],6)) # atom1 x

    if coord7[1] >= 0:
        moji4 = '    ' # 4 space
        moji5 = "{:.6E}".format(round(coord7[1],6)) # atom1 y
    elif coord7[1] < 0:
        moji4 = '   ' # 3 space
        moji5 = "{:.6E}".format(round(coord7[1],6)) # atom1 y

    if coord7[2] >= 0:
        moji6 = '    ' # 4 space
        moji7 = "{:.6E}".format(round(coord7[2],6)) # atom1 z
    elif coord7[2] < 0:
        moji6 = '   ' # 3 space
        moji7 = "{:.6E}".format(round(coord7[2],6)) # atom1 z

    moji = moji1 + moji2 + moji3 + moji4 + moji5 + moji6 + moji7
    moji = str(moji)

    for i in lines0:
        if moji in i: # 7
            #print(lines0.index(i))
            for line in itertools.islice(lines0, int(lines0.index(i)+2), int(lines0.index(i)+5)):
                f7.write(line)

    # generic atom number 8
    moji1 = 'with coordinates'
    if coord8[0] >= 0:
        moji2 = '     ' # 5 space
        moji3 = "{:.6E}".format(round(coord8[0],6)) # atom1 x
    elif coord8[0] < 0:
        moji2 = '    ' # 4 space
        moji3 = "{:.6E}".format(round(coord8[0],6)) # atom1 x

    if coord8[1] >= 0:
        moji4 = '    ' # 4 space
        moji5 = "{:.6E}".format(round(coord8[1],6)) # atom1 y
    elif coord8[1] < 0:
        moji4 = '   ' # 3 space
        moji5 = "{:.6E}".format(round(coord8[1],6)) # atom1 y

    if coord8[2] >= 0:
        moji6 = '    ' # 4 space
        moji7 = "{:.6E}".format(round(coord8[2],6)) # atom1 z
    elif coord8[2] < 0:
        moji6 = '   ' # 3 space
        moji7 = "{:.6E}".format(round(coord8[2],6)) # atom1 z

    moji = moji1 + moji2 + moji3 + moji4 + moji5 + moji6 + moji7
    moji = str(moji)

    # debug
    #if argi==1 and argj==1 and argk==1: # x y z
    #    print(moji)

    for i in lines0: # generic atom number 8, ABINIT (Not 1to1 relation, rotation?)
        if moji in i: # 8
            #print(lines0.index(i))
            for line in itertools.islice(lines0, int(lines0.index(i)+2), int(lines0.index(i)+5)):
                f8.write(line)

                #if argi==1 and argj==1 and argk==1: # x y z
                #    print(line)

    # file close
    f0.close()
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()
    f6.close()
    f7.close()
    f8.close()

    return 0

# time display
elapsed_time = time.time()-start
#print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")
