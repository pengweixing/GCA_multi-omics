#################################################
#  File Name:reorder.py
#  Author: Pengwei.Xing
#  Mail: xingwei421@qq.com,pengwei.xing@igp.uu.se,xpw1992@gmail.com
#  Created Time: Thu May 11 15:57:50 2023
#################################################

import sys

f1 = open(sys.argv[1],'r')

for line in f1:
    line = line.strip()
    line1 = line.split()
    ss = int(line1[1])
    ee = int(line1[2])
    if ss <= ee:
        print("chr"+line)
    if ss > ee:
        print("chr"+line1[0],ee,ss,*line1[3:],sep="\t")
