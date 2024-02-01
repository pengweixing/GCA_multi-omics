#################################################
#  File Name:Count_overlaps_all_sample.py
#  Author: Pengwei.Xing
#  Mail: xingwei421@qq.com,pengwei.xing@igp.uu.se,xpw1992@gmail.com
#  Created Time: Wed Aug 31 17:25:35 2022
#################################################

## find the overlaps between all intervals from different samples and count the frequency of each overlaps

""" Input format
chr1	26886806	29533492	INV	S1
chr1	40187326	40190499	INV	S1
chr1	53256804	94127606	INV	S1
chr1	29533492	40187326	multi_hits	S1
chr1	40190499	53256804	multi_hits	S1
chr7	114183249	122525422	DUP	S1
chr8	8010621	15964044	INV	S1
chr8	119113284	120740434	INV	S1
chr8	136161748	136197835	DEL	S1

"""

import numpy as np
import sys

f = open(sys.argv[1],'r')
allline = [line.strip().split()[0:3] for line in f.readlines()]
all_chr = [line[0] for line in allline]
all_chr_unique = list(set(all_chr))
allline_np = np.array(allline)
all_chr_np = np.array(all_chr)

for each_chr in all_chr_unique:
    allline_each_chr = allline_np[np.where(all_chr_np==each_chr)]
    all_pos = [int(line[1]) for line in allline_each_chr] + [int(line[2]) for line in allline_each_chr]
    all_pos = sorted(all_pos)
    temp_interval = list(zip(all_pos[:-1],all_pos[1:]))

    for each_interval in temp_interval:
        if each_interval[0] != each_interval[1]:
            count = 0
            for each_line in allline_each_chr:
                if each_interval[0] >= int(each_line[1]) and each_interval[1] <= int(each_line[2]):
                    count += 1
            print(each_chr,*each_interval,each_interval[1]-each_interval[0],count,sep="\t")
