import pandas as pd
import math
import matplotlib.pyplot as plt
import pylab

rank_norm_data = pd.read_csv('./data/rna/rank_normalization_filtered.csv', header=None, index_col=False)
mean_express = []
for row in rank_norm_data[0]:
    mean_express.append(math.log(row))
var = []
for row in rank_norm_data[1]:
    var.append(row)

plt.title("Rank Normalilzed using sliding window")
plt.ylabel("Relative Noise")
plt.xlabel("Mean gene expression")
plt.scatter(mean_express, var, s=1, color='purple')
plt.show()

