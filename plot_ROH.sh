#PBS -S /bin/bash
#PBS -V
#PBS -N /home/uramakri/anubhabk/RTR_data/plot_ROH
#PBS -m be
#PBS -M anubhabk@ncbs.res.in
#PBS -l mem=300G
#PBS -l nodes=2:ppn=32

export DISPLAY=:0.0

python ./plot_roh.py ./ROH_files
