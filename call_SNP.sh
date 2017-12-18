#calling SNPs for 6 RTR individuals

#PBS -S /bin/bash
#PBS -V
#PBS -l nodes=2:ppn=32
#PBS -N /home/uramakri/anubhabk/RTR_data/call_SNP
#PBS -m be
#PBS -M anubhabk@ncbs.res.in
#PBS -l mem=300G
export LD_LIBRARY_PATH=/softwares/samtools-1.4/lib:/softwares/xz-5.2.2/lib/:$LD_LIBRARY_PATH
export PATH=$PATH:/softwares/samtools-1.4/bin

/softwares/samtools-1.4/bin/samtools mpileup -uf /home/uramakri/anubhabk/RTR_data/panthera-10x-170301.fasta /home/uramakri/anubhabk/RTR_data/sorted_BEN_SA1_bowtie.bam /home/uramakri/anubhabk/RTR_data/sorted_BEN_SA2_bowtie.bam /home/uramakri/anubhabk/RTR_data/sorted_BEN_SA3_bowtie.bam /home/uramakri/anubhabk/RTR_data/sorted_BEN_SA4_bowtie.bam /home/uramakri/anubhabk/RTR_data/sorted_T28_bowtie_md.bam /home/uramakri/anubhabk/RTR_data/sorted_T16_bowtie.bam /home/uramakri/anubhabk/RTR_data/sorted_T91_bowtie.bam | /softwares/bcftools-1.3/./bcftools view -vcg - > /home/uramakri/anubhabk/RTR_data/RTR_var.raw.vcf
#/softwares/bcftools-1.3/./bcftools view /home/uramakri/anubhabk/RTR_data/RTR_var.raw.bcf | /softwares/bcftools-1.3/vcfutils.pl varFilter -d 10 > /home/uramakri/anubhabk/RTR_data/RTR_var_dpeth_10.vcf
