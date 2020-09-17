#load ens -> symbol conversions
c_lines = []
with open('./data/rna/ensembl_symbols.csv', 'r') as conversions:
    c_lines = [line[:-1] for line in conversions.readlines()]
pairs = []
for line in c_lines:
    pairs.append(line.split(','))

conversion = {}
for pair in pairs:
    conversion[pair[0]] = pair[1]

lines = []
with open('./data/rna/klein_scores_ens.txt', 'r') as klein: 
    lines = [line[:-1] for line in klein.readlines()]

converted_data = []
first_line = True
for line in lines:
    if first_line:
        first_line = False
        continue
    data = line.split(",")
    ens = data[0][1:-1]
    score = data[1]
    symb = conversion[ens]
    converted_data.append(symb + "," + str(score))

export_data = '\n'.join(converted_data)
with open("./data/rna/klein_scores.csv", 'w') as out:
    out.write(export_data)
