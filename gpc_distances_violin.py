import matplotlib.pyplot as plt
import seaborn as sns
data = []
with open('./data/acc/acc_closest_distances.bed', 'r') as f:
    for line in iter(f):
        data.append(int(line))
fig = plt.figure()
sns.set(style="whitegrid")
ax = sns.violinplot(x=data)
plt.title('GpC Nearest distance to other GpC')
fig.savefig('./data/acc/gpc_distances.png')

