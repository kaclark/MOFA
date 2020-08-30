#!/bin/bash

#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --mail-type=END
#SBATCH --mail-user=kaclark@mit.edu
#SBATCH --job-name=merge
#SBATCH --output=/home/kaclark/results/merge.out


module load bedtools
#sed '/mt/d' acc_windows_150.bed > w150.bed
bedtools sort -i w150.bed > s150.bed
bedtools merge -i s150.bed > m150.bed

#sed '/mt/d' acc_windows_300.bed > w300.bed
bedtools sort -i w300.bed > s300.bed
bedtools merge -i s300.bed > m150.bed
