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

variability_and_expression_data = []
variability_data = []

for x, gn in enumerate(genes):
    if gn in express_dict.keys():
        variability_and_expression_data.append([gn, express_dict[gn], var[x]])
        variability_data.append([gn, var[x]])


variability_and_expression_data_df = pd.DataFrame(variability_and_expression_data)
variability_data_df = pd.DataFrame(variability_data)
variability_and_expression_data_df.to_csv("./data/rna/gene_expression_variability.csv", header=None, index=False)
variability_data_df.to_csv("./data/rna/gene_variability.csv", header=None, index=False)
