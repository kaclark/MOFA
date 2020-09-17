lines = []
with open("./data/rna/klein_scores.csv", 'r') as scores:
    lines = [line[:-1] for line in scores.readlines()]

data = []
for line in lines:
    pre_data = line.split(',')
    score = float(pre_data[1])
    data.append([pre_data[0], score])

print(sorted(data, key=lambda x: x[1]))
