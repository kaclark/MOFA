import pandas as pd

mean_gene_exp_data = pd.read_csv("./data/rna/pme_t.csv", header=None, index_col=False)

means = []
for row in mean_gene_exp_data[1]:
    means.append(row)
genes = []
for row in mean_gene_exp_data[0]:
    genes.append(row)
data = {}
for x, mn in enumerate(means):
    data[mn] = genes[x]

means.sort(reverse=True)
clipped_sorted = means[39:]

export_data = []
for x, mn in enumerate(clipped_sorted):
    export_data.append([data[mn], mn])

export = pd.DataFrame(export_data)
export.to_csv("./data/rna/sorted_pme.csv", header=False, index=False)
