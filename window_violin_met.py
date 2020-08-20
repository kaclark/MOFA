import matplotlib.pyplot as plt
import seaborn as sns
data = []
with open('./data/met/diff_met.bed', 'r') as f:
    for line in iter(f):
        data.append(int(line))
fig = plt.figure()
sns.set(style="whitegrid")
ax = sns.violinplot(x=data)
fig.savefig('./data/met/met_windows.png')
