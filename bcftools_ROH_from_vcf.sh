#PBS -S /bin/bash
#PBS -V
#PBS -l nodes=2:ppn=32
#PBS -N /home/uramakri/anubhabk/RTR_data/bcftools_ROH
#PBS -m be
#PBS -M anubhabk@ncbs.res.in
#PBS -l mem=300G

/softwares/bcftools-1.3/./bcftools roh -G 30 -s BEN_SA1 /home/uramakri/anubhabk/RTR_data/RTR_SNPs_q30_gq30_dp10_hwe0001_min1Mb_autosomal_scaf_7indiv.recode.vcf -e - > /home/uramakri/anubhabk/RTR_data/BEN_SA1_ROH.txt
/softwares/bcftools-1.3/./bcftools roh -G 30 -s BEN_SA2 /home/uramakri/anubhabk/RTR_data/RTR_SNPs_q30_gq30_dp10_hwe0001_min1Mb_autosomal_scaf_7indiv.recode.vcf -e - > /home/uramakri/anubhabk/RTR_data/BEN_SA2_ROH.txt
/softwares/bcftools-1.3/./bcftools roh -G 30 -s	BEN_SA3 /home/uramakri/anubhabk/RTR_data/RTR_SNPs_q30_gq30_dp10_hwe0001_min1Mb_autosomal_scaf_7indiv.recode.vcf -e - >	/home/uramakri/anubhabk/RTR_data/BEN_SA3_ROH.txt
/softwares/bcftools-1.3/./bcftools roh -G 30 -s BEN_SA4 /home/uramakri/anubhabk/RTR_data/RTR_SNPs_q30_gq30_dp10_hwe0001_min1Mb_autosomal_scaf_7indiv.recode.vcf -e - > /home/uramakri/anubhabk/RTR_data/BEN_SA4_ROH.txt
/softwares/bcftools-1.3/./bcftools roh -G 30 -s "/home/uramakri/anubhabk/RTR_BAMs/sorted_T28_bowtie.bam" /home/uramakri/anubhabk/RTR_data/RTR_SNPs_q30_gq30_dp10_hwe0001_min1Mb_autosomal_scaf_7indiv.recode.vcf -e - > /home/uramakri/anubhabk/RTR_data/T28_ROH.txt
/softwares/bcftools-1.3/./bcftools roh -G 30 -s "/home/uramakri/anubhabk/RTR_BAMs/sorted_T16_bowtie.bam" /home/uramakri/anubhabk/RTR_data/RTR_SNPs_q30_gq30_dp10_hwe0001_min1Mb_autosomal_scaf_7indiv.recode.vcf -e - > /home/uramakri/anubhabk/RTR_data/T16_ROH.txt
/softwares/bcftools-1.3/./bcftools roh -G 30 -s "/home/uramakri/anubhabk/RTR_BAMs/sorted_T91_bowtie.bam" /home/uramakri/anubhabk/RTR_data/RTR_SNPs_q30_gq30_dp10_hwe0001_min1Mb_autosomal_scaf_7indiv.recode.vcf -e - > /home/uramakri/anubhabk/RTR_data/T91_ROH.txt
