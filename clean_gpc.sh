#!/bin/bash
#SBATCH -N 1
#SBATCH -n 1
#SBATCH --mail-type=END
#SBATCH --mail-user=kaclark@mit.edu
#SBATCH --job-name=GpC
#SBATCH --output=/home/kaclark/results/gpc_cleaning/output_%A_%a.out
#SBATCH --error=/home/kaclark/results/gpc_cleaning/error_%A_%a.err
#SBATCH --array=1-1238

cd ~/data/acc/coll

echo $(sed -n "${SLURM_ARRAY_TASK_ID}p" index.txt)
ID=$(sed -n "${SLURM_ARRAY_TASK_ID}p" index.txt)

module load python3
python3 clean_gpc.py ${ID} > cleaned/${ID}
