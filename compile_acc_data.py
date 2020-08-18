import sys
from pathlib import Path
import pandas as pd
import pickle

directory = sys.argv[1]
pathlist = Path(directory).glob("*.tsv")

acc_data = {}
for pre_path in pathlist:
    path = str(pre_path)
    pre_name = path.split('.tsv')[0]
    name = pre_name.split('/')[-1]

    raw_data = []
    with open(path, 'r') as file:
        for cnt, line in enumerate(file):
            if cnt > 1 and line != '\n':
                line = line.replace('\n','')
                raw = line.split('\t')
                raw_data.append(raw)

    acc = [[dt[0],dt[1]] for dt in raw_data if int(dt[4]) == 1]
    acc_data[name] = acc

with open('./data/chip/acc_data.pickle', 'wb') as pickle_out:
    pickle.dump(acc_data, pickle_out)
