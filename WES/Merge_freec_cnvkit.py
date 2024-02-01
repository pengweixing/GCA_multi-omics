#################################################
#  File Name:Merge_freec_cnvkit.py
#  Author: Pengwei.Xing
#  Mail: xingwei421@qq.com,pengwei.xing@igp.uu.se,xpw1992@gmail.com
#  Created Time: Wed May 10 11:43:38 2023
#################################################

import sys
f1 = open(sys.argv[1],'r')## list

for line in f1:
    line = line.strip()
    line1 = line.split('\t')
    sample = line1[0]
    cnvkit = line1[1]
    freec = line1[2]
    f_cnvkit = open(cnvkit,'r')
    f_freec = open(freec,'r')
    f_cnvkit.readline()
    cnvkit_list = []
    f_out_all = open(sample+'cnv.all.txt','w')

    for each in f_cnvkit:
        each = each.strip()
        each2 = each.split()
        cnvkit_chr,cnvkit_start,cnvkit_end = each2[0:3]
        cnvkit_start = int(cnvkit_start)
        cnvkit_end = int(cnvkit_end)
        cnvkit_cn = int(each2[3])
        cnvkit_list.append([cnvkit_chr,cnvkit_start,cnvkit_end,cnvkit_cn])
    for each in f_freec:
        each = each.strip()
        each2 = each.split()
        freec_chr = each2[0]
        freec_start = int(each2[1])
        freec_end = int(each2[2])
        freec_cn = int(each2[3])
        if freec_start > freec_end:
            freec_start = int(each2[2])
            freec_end = int(each2[1])
        for bb in cnvkit_list:
            if bb[0] == freec_chr:
                if freec_start >= bb[1] and freec_start <= bb[2] and freec_end > bb[2]:
                    if freec_cn < 2 and bb[3] < 2:
                        cnv_start  = freec_start
                        cnv_end = bb[2]
                        cnv_cn = (freec_cn+bb[3])/2
                        cnv_type = 'loss'
                        print(freec_chr,cnv_start,cnv_end,cnv_cn,cnv_type,sample,sep="\t")
                        f_out_all.write("%s\t%s\t%s\t%s\n" % (freec_chr,cnv_start,cnv_end,cnv_cn))
                    elif freec_cn > 2 and bb[3] > 2:
                        cnv_start  = freec_start
                        cnv_end = bb[2]
                        cnv_cn = (freec_cn+bb[3])/2
                        cnv_type = 'gain'
                        print(freec_chr,cnv_start,cnv_end,cnv_cn,cnv_type,sample,sep="\t")
                        f_out_all.write("%s\t%s\t%s\t%s\n" % (freec_chr,cnv_start,cnv_end,cnv_cn))
                elif freec_start <= bb[1] and freec_end >= bb[1] and freec_end <= bb[2]:
                    if freec_cn < 2 and bb[3] < 2:
                        cnv_start  = bb[1]
                        cnv_end = freec_end
                        cnv_cn = (freec_cn+bb[3])/2
                        cnv_type = 'loss'
                        print(freec_chr,cnv_start,cnv_end,cnv_cn,cnv_type,sample,sep="\t")
                        f_out_all.write("%s\t%s\t%s\t%s\n" % (freec_chr,cnv_start,cnv_end,cnv_cn))
                    elif freec_cn > 2 and bb[3] > 2:
                        cnv_start  = bb[1]
                        cnv_end = freec_end
                        cnv_cn = (freec_cn+bb[3])/2
                        cnv_type = 'gain'
                        print(freec_chr,cnv_start,cnv_end,cnv_cn,cnv_type,sample,sep="\t")
                        f_out_all.write("%s\t%s\t%s\t%s\n" % (freec_chr,cnv_start,cnv_end,cnv_cn))
                elif freec_start <= bb[1] and freec_end >= bb[2]:
                    if freec_cn < 2 and bb[3] < 2:
                        cnv_start  = bb[1]
                        cnv_end = bb[2]
                        cnv_cn = (freec_cn+bb[3])/2
                        cnv_type = 'loss'
                        print(freec_chr,cnv_start,cnv_end,cnv_cn,cnv_type,sample,sep="\t")
                        f_out_all.write("%s\t%s\t%s\t%s\n" % (freec_chr,cnv_start,cnv_end,cnv_cn))
                    elif freec_cn > 2 and bb[3] > 2:
                        cnv_start  = bb[1]
                        cnv_end = bb[2]
                        cnv_cn = (freec_cn+bb[3])/2
                        cnv_type = 'gain'
                        print(freec_chr,cnv_start,cnv_end,cnv_cn,cnv_type,sample,sep="\t")
                        f_out_all.write("%s\t%s\t%s\t%s\n" % (freec_chr,cnv_start,cnv_end,cnv_cn))
                elif freec_start >= bb[1] and freec_end <= bb[2]:

                    if freec_cn < 2 and bb[3] < 2:
                        cnv_start  = freec_start
                        cnv_end = freec_end
                        cnv_cn = (freec_cn+bb[3])/2
                        cnv_type = 'loss'
                        print(freec_chr,cnv_start,cnv_end,cnv_cn,cnv_type,sample,sep="\t")
                        f_out_all.write("%s\t%s\t%s\t%s\n" % (freec_chr,cnv_start,cnv_end,cnv_cn))
                    elif freec_cn > 2 and bb[3] > 2:
                        cnv_start  = freec_start
                        cnv_end = freec_end
                        cnv_cn = (freec_cn+bb[3])/2
                        cnv_type = 'gain'
                        print(freec_chr,cnv_start,cnv_end,cnv_cn,cnv_type,sample,sep="\t")
                        f_out_all.write("%s\t%s\t%s\t%s\n" % (freec_chr,cnv_start,cnv_end,cnv_cn))
