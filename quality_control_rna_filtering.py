import pandas as pd
print("Loaded pandas")
rna_data = pd.read_csv('./data/rna/counts.txt', sep='\t')
print("Loaded RNA data")
rna_data.head()
qc_data = pd.DataFrame()
counter = 0
genes = rna_data['ens_id'].tolist()
for (columnName, columnData) in rna_data.iteritems():
    #rest of columns need to be cells and read counts
    if counter > 0:
        total = 0
        expressed = 0
        #add up the read counts
        for val in columnData.values:
            total += int(val)
            if val > 0:
                expressed += 1
        #if read count total matches quality control, add to export dataframe
        if total >= 100000 and expressed > 500:
            qc_data[columnName] = columnData.values
    #first column needs to be genes
    else:
        qc_data['ens_id'] = genes
    counter += 1
print("Quality Control complete")
#once the qc_data dataframe has been popualted, export
qc_data.to_csv("./data/rna/qc_counts.txt", sep='\t', index=False)
print("Data exported")


