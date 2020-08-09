import pandas as pd

var_data = pd.read_csv("./data/rna/pagoda_window_norm.csv", header=None, index_col=False)
genes = []
for row in var_data[0]:
    genes.append(row)
var = []
for row in var_data[1]:
    var.append(row)

express_data = pd.read_csv("./data/rna/sorted_pme.csv", header=None, index_col=False)
exp_genes = []
for row in express_data[0]:
    exp_genes.append(row.strip("'"))
exps = []
for row in express_data[1]:
    exps.append(row)

express_dict = {}
for x, gn in enumerate(exp_genes):
    express_dict[gn] = exps[x]

export_data = []
for x, gn in enumerate(genes):
    if gn in express_dict.keys():
        export_data.append([express_dict[gn], var[x]])

export = pd.DataFrame(export_data)
export.to_csv('./data/rna/rank_normalization_filtered.csv', header=None, index=False)


