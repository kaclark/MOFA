#!/bin/bash

#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --cpus-per-task=8
#SBATCH --mail-type=ALL
#SBATCH --mail-user=kaclark@mit.edu
#SBATCH --job-name=pca

module load r/3.6.0
Rscript pagoda_pca.R
