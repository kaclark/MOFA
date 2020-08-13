import sys
from pathlib import Path
import pandas as pd
import pickle

directory = sys.argv[1]
pathlist = Path(directory).glob("*.tsv")

meth_data = {}
for pre_path in pathlist:
    path = str(pre_path)
    pre_name = path.split('.tsv')[0]
    name = pre_name.split('/')[-1]
    tsv_data = pd.read_csv(path, sep = '\t', header=None, index_col=False)
    tsv_data = tsv_data.iloc[1:]
    chrom = [row for row in tsv_data[0]]
    position = [row for row in tsv_data[1]]
    rate = [row for row in tsv_data[4]]
    data = list(zip(chrom, position, rate))
    present = [meth for meth in data if meth[2] == 1]
    meth_data[name] = present

with open('./data/chip/meth_data.pickle', 'wb') as pickle_out:
    pickle.dump(meth_data, pickle_out)
