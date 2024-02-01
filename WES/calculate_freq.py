#################################################
#  File Name:calculate_freq.py
#  Author: Pengwei.Xing
#  Mail: xingwei421@qq.com,pengwei.xing@igp.uu.se,xpw1992@gmail.com
#  Created Time: Mon 09 Oct 2023 05:30:17 PM CEST
#################################################
import sys

f1 = open("/disk1/pengweixing/database/hg38/hg38.window1M.clean2.txt",'r')

f2 = open(sys.argv[1],'r')

all_line = [line.strip() for line in f2.readlines()]
all_line = all_line[1:]

samples = [line.strip().split()[5] for line in all_line]
number = len(set(samples))

for line in f1:
    line = line.strip()
    line1 = line.split()
    mychr = line1[0]
    ss = int(line1[1])
    ee = int(line1[2])
    overlaps = []
    for aa in all_line:
        aa1 = aa.split()
        if mychr == aa1[0]:
            ##  bin   ss --------ee
            ##  cnv --------------
            if ss >= int(aa1[1]) and ee <= int(aa1[2]):  
                overlaps.append(aa1[5]) 
                if mychr=="chr15" and ss==89000001:
                    print(aa1)

            ##  bin    ss--------ee
            ##  cnv --------
            elif ss > int(aa1[1]) and ss < int(aa1[2]):
                overlaps.append(aa1[5]) 
                if mychr=="chr15" and ss==89000001:
                    print(aa1)

            ##  bin    ss--------ee
            ##  cnv        ----
            elif ss <= int(aa1[1]) and ee >= int(aa1[2]):
                overlaps.append(aa1[5]) 
                if mychr=="chr15" and ss==89000001:
                    print(aa1)

            ##  bin    ss--------ee
            ##  cnv        -----------
            elif ss <= int(aa1[1]) and ee >= int(aa1[1]):
                overlaps.append(aa1[5]) 
                if mychr=="chr15" and ss==89000001:
                    print(aa1)
    overlaped_num = len(set(overlaps))
    freq = overlaped_num 
    #print(line,freq,sep="\t")
