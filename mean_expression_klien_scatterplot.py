import math
import matplotlib.pyplot as plt
import pylab

lines = []
with open('./data/rna/mean_expression_and_klien.csv', 'r') as input:
    lines = [line[:-1] for line in input.readlines()]

mean = []
klien = []
for line in lines:
    data = line.split(",")
    mean.append(data[1])
    klien.append(data[2])
fig = plt.figure()
plt.title("Mean gene expression vs Klien Score")
plt.ylabel("Klien Score")
plt.xlabel("Mean gene expression")
plt.scatter(mean, klien, s=1, color='purple')
fig.savefig('./data/rna/mean_expression_vs_klien.png')


