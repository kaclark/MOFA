#!/bin/bash

#SBATCH -N 1
#SBATCH -n 1
#SBATCH --mail-type=END
#SBATCH --mail-user=kaclark@mit.edu
#SBATCH --job-name=acc_data

module load python3
python3 gather_acc_data.py data/scmnt/acc/gpc_level/
