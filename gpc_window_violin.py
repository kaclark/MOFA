import matplotlib.pyplot as plt
import seaborn as sns
data_150 = []
with open('./data/acc/diff_m150.txt', 'r') as f:
    for line in iter(f):
        data_150.append(int(line))
fig = plt.figure()
sns.set(style="whitegrid")
ax = sns.violinplot(x=data_150)
plt.title('GpC Window size from 150')
fig.savefig('./data/acc/acc_windows_150.png')

data_300 = []
with open('./data/acc/diff_m300.txt', 'r') as f:
    for line in iter(f):
        data_300.append(int(line))
fig = plt.figure()
sns.set(style="whitegrid")
ax = sns.violinplot(x=data_300)
plt.title('GpC Window size from 300')
fig.savefig('./data/acc/acc_windows_300.png')
