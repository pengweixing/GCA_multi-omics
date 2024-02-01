#################################################
#  File Name:split_maf_to_each_type.py
#  Author: Pengwei.Xing
#  Mail: xingwei421@qq.com,pengwei.xing@igp.uu.se,xpw1992@gmail.com
#  Created Time: Wed Sep 14 15:11:25 2022
#################################################


import pandas as pd
import numpy as np
import sys
maf = pd.read_csv(sys.argv[1],sep="\t")##anno.maf
maf_snp = maf[maf['Variant_Type']!="SNP"]
snp_protein_coding = maf_snp[maf_snp['BIOTYPE']=="protein_coding"]
lncRNA = maf_snp[maf_snp['BIOTYPE']=="lncRNA"]
BIOTYPE_type_stat = maf_snp['BIOTYPE'].value_counts()
Variant_Classification_type_stat = maf_snp['Variant_Classification'].value_counts()
Variant_Classification_type_lncRNA_stat = lncRNA['Variant_Classification'].value_counts()
snp_mutation = snp_protein_coding[(snp_protein_coding['Variant_Classification']=="Missense_Mutation")|
                                  (snp_protein_coding['Variant_Classification']=="Splice_Site")|
                                 (snp_protein_coding['Variant_Classification']=="Nonstop_Mutation")|
                                (snp_protein_coding['Variant_Classification']=="Nonsense_Mutation")|
                                 (snp_protein_coding['Variant_Classification']=="Translation_Start_Site")|
                                 (snp_protein_coding['Variant_Classification']=="Frame_Shift_Del")|
                                 (snp_protein_coding['Variant_Classification']=="Frame_Shift_Ins")|
                                 (snp_protein_coding['Variant_Classification']=="In_Frame_Del")|
                                 (snp_protein_coding['Variant_Classification']=="In_Frame_Ins")|
                                 (snp_protein_coding['Variant_Classification']=="bidirectional_gene_fusion")|
                                 (snp_protein_coding['Variant_Classification']=="gene_fusion")]

snp_pro_cod_updownstream = snp_protein_coding[(snp_protein_coding['Variant_Classification']=="upstream_gene_variant")|(snp_protein_coding['Variant_Classification']=="downstream_gene_variant")]
snp_pro_cod_upstream = snp_protein_coding[snp_protein_coding['Variant_Classification']=="upstream_gene_variant"]
snp_pro_cod_downstream = snp_protein_coding[snp_protein_coding['Variant_Classification']=="downstream_gene_variant"]
snp_lnc_coding_exon_split = lncRNA[(lncRNA['Variant_Classification']=="non_coding_transcript_exon_variant")|(lncRNA['Variant_Classification']=="Splice_Site")]
snp_lnc_cod_upstream = lncRNA[lncRNA['Variant_Classification']=="upstream_gene_variant"]
snp_pro_cod_UTR = snp_protein_coding[(snp_protein_coding['Variant_Classification']=="3_prime_UTR_variant") |(snp_protein_coding['Variant_Classification']=="5_prime_UTR_variant")]

def gener_matrix(snp_pro_cod_upstream):
    snp_pro_cod_upstream_matrix = pd.DataFrame(data = 0,index=list(set(snp_pro_cod_upstream['Hugo_Symbol'])), columns=list(set(snp_pro_cod_upstream['Tumor_Sample_Barcode'])))
    for index, row in snp_pro_cod_upstream.iterrows():
        gene = row['Hugo_Symbol']
        sample = row['Tumor_Sample_Barcode']
        mytype = row['Variant_Classification']
        if snp_pro_cod_upstream_matrix.loc[gene,sample] == mytype:
            snp_pro_cod_upstream_matrix.loc[gene,sample] = "multi_hits"
        else:
            snp_pro_cod_upstream_matrix.loc[gene,sample] = mytype
    a = snp_pro_cod_upstream_matrix==0
    a.replace({False: 1, True: 0}, inplace=True)
    c = a.sum('columns').sort_values(ascending=False)
    snp_pro_cod_upstream_matrix2 = snp_pro_cod_upstream_matrix.loc[c.index,:]
    snp_pro_cod_upstream_matrix2[snp_pro_cod_upstream_matrix2==0]=np.nan
    return snp_pro_cod_upstream_matrix2

snp_pro_cod_UTR_matrix = gener_matrix(snp_pro_cod_UTR)
snp_pro_cod_updownstream_matrix = gener_matrix(snp_pro_cod_updownstream)
snp_pro_cod_upstream_matrix = gener_matrix(snp_pro_cod_upstream)
snp_pro_cod_downstream_matrix = gener_matrix(snp_pro_cod_downstream)
snp_lnc_cod_upstream_matrix = gener_matrix(snp_lnc_cod_upstream)
snp_lnc_coding_exon_split_matrix = gener_matrix(snp_lnc_coding_exon_split)
snp_mutation_matrix = gener_matrix(snp_mutation)

snp_pro_cod_UTR_matrix.to_csv('indel_pro_cod_UTR_matrix.indel.txt', sep='\t')
#snp_pro_cod_updownstream_matrix.to_csv('snp_pro_cod_updownstream_matrix.txt', sep='\t')
snp_pro_cod_upstream_matrix.to_csv('indel_pro_cod_upstream_matrix.txt', sep='\t')
snp_pro_cod_downstream_matrix.to_csv('indel_pro_cod_downstream_matrix.txt', sep='\t')
#snp_lnc_cod_upstream_matrix.to_csv('snp_lnc_cod_upstream_matrix.txt', sep='\t')
#snp_lnc_coding_exon_split_matrix.to_csv('snp_lnc_coding_exon_split_matrix.txt', sep='\t')
snp_mutation_matrix.to_csv('indel_mutation_matrix.txt', sep='\t')
