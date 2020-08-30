import matplotlib.pyplot as plt
import seaborn as sns
import sys
from pathlib import Path

directory = sys.argv[1]
pathlist = Path(directory).glob('*.tsv')

gpc_counts = []
for pre_path in pathlist:
    path = str(pre_path)
    with open(path, 'r') as fl:
        gpc_counts.append(sum(1 for _ in fl))

fig = plt.figure()
sns.set(style="whitegrid")
ax = sns.violinplot(x=gpc_counts)
plt.title("GpC counts per cell")
fig.savefig('./data/acc/acc_violin.png')
