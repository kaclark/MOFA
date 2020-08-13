#!/bin/bash

#SBATCH -N 1
#SBATCH -n 1
#SBATCH --mail-type=END
#SBATCH --mail-user=kaclark@mit.edu
#SBATCH --job-name=met_data

module load python3
python3 gather_met_data.py data/scmnt/met/cpg_level/
