import matplotlib.pyplot as plt
import seaborn as sns

with open('./data/met/met_data.pickle','rb') as pickle_in:
    data = pickle.load(pickle_in)

fig = plt.figure()
sns.set(sytle="whitegrid")
ax = sns.violinplot(x=data)
fig.savefig('./data/met/met_violin.png')
