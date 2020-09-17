m_lines = []
with open('./data/rna/mean_expression.csv', 'r') as mean_expression:
    m_lines = [line[:-1] for line in mean_expression.readlines()]

m_pairs = []
for line in m_lines:
    m_pairs.append(line.split(','))

mean_expression = {}
for pair in m_pairs:
    mean_expression[pair[0]] = pair[1]

k_lines = []
with open('./data/rna/klein_scores.csv', 'r') as klien:
    k_lines = [line[:-1] for line in klien.readlines()]

k_pairs = []
for line in k_lines:
    k_pairs.append(line.split(','))

klien = {}
for pair in k_pairs:
    klien[pair[0]] = pair[1]

shorter = None
longer = None
if len(klien.keys()) > len(mean_expression.keys()):
    shorter = mean_expression
    longer = klien
else:
    shorter = klien
    longer = mean_expression

data = []
for gene in shorter.keys():
    if gene in longer.keys():
        data.append(str(gene) + "," + str(mean_expression[gene]) + "," +  str(klien[gene]))

export = '\n'.join(data)
with open("./data/rna/mean_expression_and_klien.csv", 'w') as out:
    out.write(export)

