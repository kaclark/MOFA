import pandas as pd

with open('./gini_cor_mean.txt', 'r') as file:
    lines = []
    for cnt, line in enumerate(file):
        #don't add linebreaks '
        if line != '\n':
            #format ensembl
            line = line.replace('\n', '')
            line = line.replace('c(', '')
            line = line.replace(' ', '')
            line = line.replace(')', '')
            line = line.replace('=', ',')
            lines.append(line)

export = open('./gini_cm_clean.txt', 'w')
data = '\n'.join(lines)
export.write(data)
export.close()

