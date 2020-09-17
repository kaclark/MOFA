import matplotlib.pyplot as plt
data = []
with open('./data/acc/acc_closest_distances.bed', 'r') as f:
    for line in iter(f):
        data.append(int(line))

fig = plt.figure()
plt.boxplot(data, showfliers=False)
plt.title('GpC Nearest distance to other GpC')
fig.savefig('./data/acc/gpc_distances.png')

