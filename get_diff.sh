#!/bin/bash

#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --mail-type=END
#SBATCH --mail-user=kaclark@mit.edu
#SBATCH --job-name=awk_diff
#SBATCH --output=/home/kaclark/results/get_diff.out

awk '{print $3 - $2}' w150.bed > diff_w150.txt
awk '{print $3 - $2}' w300.bed > diff_w300.txt
