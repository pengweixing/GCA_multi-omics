#################################################
#  File Name:get_gene_cp_fromcnvkit.py
#  Author: Pengwei.Xing
#  Mail: xingwei421@qq.com,pengwei.xing@igp.uu.se,xpw1992@gmail.com
#  Created Time: Thu Feb 24 13:25:32 2022
#################################################


import sys
import pickle
import pandas as pd
import numpy as np
import argparse

parser = argparse.ArgumentParser(usage="python get_gene_cp_fromcnvkit.py -l list -n 3 -o outname")
parser.add_argument('-l',"--list",help="the list of .call.cns file ", required=True)
parser.add_argument('-n',"--number",help="sort by frequency of genes which >= n", default=3,type=int)
parser.add_argument('-o',"--out",help="the name of output ", required=True)
args = parser.parse_args()



def parser_list(f1):
    thedict = {}
    for line in f1:
        line = line.strip()
        line1 = line.split()
        thedict[line1[0]] =  line1[1]
    return thedict

def get_all_genes(thedict):
    all_files = thedict.values()
    all_gene = []
    for each in all_files:
        with open(each,'r') as f:
            temp = f.readline()
            for line in f:
                line = line.strip()
                line1 = line.split()
                if line1[0] != 'chrX' and line1[0] !='chrY':
                    genes = line1[3]
                    genes2 = genes.split(',')
                    all_gene.extend(genes2)
    return list(set(all_gene))

def parse_each_file(cnv,all_gene):

    cn_dict = dict((i, [],) for i in all_gene)
    with open(cnv,'r') as f:
        f.readline()
        for each_line in f:
            each_line = each_line.strip()
            each_line = each_line.split()
            genes = each_line[3].split(',')
            copynumber = float(each_line[4])
            if each_line[0] != 'chrX' and each_line[0] != 'chrY':
                for each_gene in genes:
                    cn_dict[each_gene].append(copynumber)

        for key,value in cn_dict.items():
            if len(value)>1:
                avg_value = round(sum(value)/len(value),2)
                cn_dict[key] = avg_value
            elif len(value) == 1:
                cn_dict[key] = value[0]
            else:
                cn_dict[key] = ''
    return cn_dict


def main():
    f1 = open(args.list,'r')
    mydict = parser_list(f1)
    all_name = list(mydict.keys())
    all_gene = get_all_genes(mydict)
    
    data = pd.DataFrame(index=all_gene,columns=all_name)

    for key,value in mydict.items():
        cn_dict = parse_each_file(value,all_gene)
        print(key)
        for each_gene,copynumber in cn_dict.items():
            data[key][each_gene] = copynumber
    
    all_data2 = data.replace('',np.nan)
    all_data3 = all_data2.dropna() 
    all_data4 = all_data3.where(all_data3>=args.number)
    sorted_index = all_data4.isnull().sum(1).sort_values(ascending=True).index
    all_data_NaN = all_data4.loc[sorted_index]
    all_data3_sorted = all_data3.loc[sorted_index]
    all_data3_sorted.to_csv(args.out+".all.number.txt",sep="\t")
    all_data_NaN.to_csv(args.out+".only.amp.txt",sep="\t")
if "__name__" == main():
    main()
