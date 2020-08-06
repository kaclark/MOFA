import pandas as pd
print("Loaded pandas")
rna_data = pd.read_csv('./data/rna/counts.txt', sep='\t')
print("Loaded RNA data")
genes = rna_data['ens_id'].tolist()
qc_data = pd.DataFrame(genes)
qc_data.to_csv("./data/rna/ensembl.txt", sep='\t', index=False, header=False)
print("Data exported")


