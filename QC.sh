#!/bin/bash
#PBS -l nodes=1:ppn=32,mem=300GB
#PBS -M anubhabk@ncbs.res.in
#PBS -m be
#PBS -N /home/uramakri/anubhabk/RTR_data/QC

/softwares/qualimap_v2.2.1/qualimap bamqc -bam /home/uramakri/anubhabk/RTR_data/sorted_T24_bowtie.bam
