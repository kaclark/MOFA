import pandas as pd

var_data = pd.read_csv('./data/rna/parvs_t.csv', header=None, index_col=False)

genes = []
for row in var_data[0]:
    genes.append(row)

var_vals = []
for row in var_data[1]:
    var_vals.append(row)

norm_vars = []

for x, varr in enumerate(var_vals):
    if x < 50:
        window = var_vals[0:x+(100-(x+1))]
    else:
        window = var_vals[x-50:x+49]
    max_val = 0
    min_val = 100
    for y, val in enumerate(window):
        if val > max_val:
            max_val = val
        if val < min_val:
            min_val = val
        
    try:
        norm_var = (varr - min_val) / (max_val - min_val)
    except ZeroDivisionError:
        norm_var = 0
    norm_vars.append([genes[x], norm_var])

export_data = pd.DataFrame(norm_vars)
export_data.to_csv("./data/rna/pagoda_window_norm.csv", index=False, header=False)
