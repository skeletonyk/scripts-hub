#!/bin/bash
 
#SBATCH --job-name=Re550
#####SBATCH -p nodes
#SBATCH -o af_Re550.out
#SBATCH --partition=normal
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=24 
#SBATCH --export=ALL 
#SBATCH -t 23:00:00

mpirun  /home/kyu/IBLGF/master/build/dist/bin/iblgf_exe data.fdt ib_point_cloud.fdat ib_connectivity.fdat adapt_weight_waypoints.fdat
