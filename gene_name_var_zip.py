import pandas as pd

var_data = pd.read_csv('./data/rna/gene_variability.csv', header=None, index_col=False)
var_ens = []
for row in var_data[0]:
    var_ens.append(row)
var = []
for row in var_data[1]:
    var.append(row)
var_dict = {}
for x, en in enumerate(var_ens):
    var_dict[en] = var[x]

sym_data = pd.read_csv('./data/rna/ensembl_symbols.csv', header=None, index_col=False)
sym_ens = []
for row in sym_data[0]:
    sym_ens.append(row)
sym = []
for row in sym_data[1]:
    sym.append(row)
sym_dict = {}
for x, en in enumerate(sym_ens):
    sym_dict[en] = sym[x]

export_data = []
for x, en in enumerate(var_ens):
    export_data.append([sym_dict[en], var_dict[en]])

export = pd.DataFrame(export_data)
export.to_csv('./data/rna/symb_var.tsv', sep='\t', header=False, index=False)



