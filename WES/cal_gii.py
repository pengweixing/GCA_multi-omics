#################################################
#  File Name:cal_gii.py
#  Author: Pengwei.Xing
#  Mail: xingwei421@qq.com,pengwei.xing@igp.uu.se,xpw1992@gmail.com
#  Created Time: Mon 09 Oct 2023 03:09:10 PM CEST
#################################################
import sys
f = open(sys.argv[1],'r')
f.readline()

sum_len = 0
for line in f:
    line = line.strip()
    line1 = line.split()
    ss = int(line1[1])
    ee = int(line1[2])
    log = float(line1[4])
    if log >= 0.7 or log<=-0.4:
        sum_len = sum_len + (ee - ss)

all_len = 3060453665
gii = sum_len/all_len
print("%.2f" % gii)
