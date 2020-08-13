import pickle
import matplotlib import pyplot as plt

with open('./met/met_data.pickle', 'rb') as pickle_in:
    met_data = pickle.load(pickle_in)
with open('./acc/acc_data.pickle', 'rb') as pickle_in:
    acc_data = pickle.load(pickle_in)

met_histo_data = [len(v) for (k,v) in met_data.items()]
acc_histo_data = [len(v) for (k,v) in acc_data.items()]

plt.hist(met_histo_data)
plt.title("Methylation Data")
plt.xlabel("Number of cpg sites within cell")
plt.ylabel("Freq of count")

plt.hist(acc_histo_data)
plt.title("Accessiblity Data")
plt.xlabel("Number of gpc sites within cell")
plt.ylabel("Freq of count")
