#!/bin/bash

#SBATCH --job-name=post_Re300_ang0
#####SBATCH -p nodes
#SBATCH -o post_Re300_ang0.out
#SBATCH --partition=normal
#SBATCH --nodes=1 
#SBATCH --ntasks-per-node=24 
#SBATCH --export=ALL 
#SBATCH -t 5:00:00

mpirun /home/kyu/IBLGF/master/build/dist/bin/iblgf_post --out_dir outputs --post_dir post
