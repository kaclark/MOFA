import pandas as pd

with open('./data/rna/symbols_raw.txt') as file:
    ensembl = []
    symbol = []
    for cnt, line in enumerate(file):
        #don't add linebreaks '
        if line != '\n':
            #format ensembl
            line = line.replace('\n', '')
            if '$' in line:
                line = line.replace('$', '')
                ensembl.append(line)
            else:
                line = line.replace('[1] ', '')
                line = line.replace('"', '')
                symbol.append(line)
    export_data = zip(ensembl, symbol)

export = pd.DataFrame(export_data)
export.to_csv("./data/rna/ensembl_symbols.csv", header=False, index=False)
