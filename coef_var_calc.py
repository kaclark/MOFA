import pandas as pd
rna_data = pd.read_csv('./data/rna/qc_counts.txt', sep='\t')
cv_data = []
for x in range(rna_data.shape[1]):
    gene = rna_data.iloc[x].tolist()[0]
    counts = rna_data.iloc[x].tolist()[1:]
    mean = sum(counts) / len(counts) 
    variance = sum([((x - mean) ** 2) for x in counts]) / len(counts) 
    res = variance ** 0.5
    if mean != 0:
        pre_cv = res/mean
        cv = pre_cv * 100
    else:
        cv = -1
    cv_data.append([gene, cv, mean])

export_data = pd.DataFrame(cv_data)
export_data.to_csv('./data/rna/coef_var.txt', sep='\t', index=False, header=False)
