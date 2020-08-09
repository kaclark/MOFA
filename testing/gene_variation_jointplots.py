import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import math

cv_data = pd.read_csv('./data/rna/coef_var_filtered.txt', sep='\t', header=None, index_col=False)
genes = []
for row in cv_data[0]:
    genes.append(row)
cv = []
for row in cv_data[1]:
    cv.append(row)
mean = []
for row in cv_data[2]:
    mean.append(math.log10(row))
scaled_cv = []
for val in cv:
    scaled_cv.append(math.log10(val ** 2))

x = mean
y = scaled_cv

sns.jointplot(x=x, y=y, kind='hex')
plt.show()


rank_norm_data = pd.read_csv('./data/rna/raw_pagoda.csv', header=None, index_col=False)
mean_express = []
for row in rank_norm_data[0]:
    mean_express.append(math.log10(row))
var = []
for row in rank_norm_data[1]:
    var.append(row)

x = mean_express
y = var

sns.jointplot(x=x, y=y, kind='hex')
plt.show()

rank_norm_data = pd.read_csv('./data/rna/rank_normalization_filtered.csv', header=None, index_col=False)
mean_express_rank = []
for row in rank_norm_data[0]:
    mean_express_rank.append(math.log(row))
var_rank = []
for row in rank_norm_data[1]:
    var_rank.append(row)

x = mean_express_rank
y = var_rank

sns.jointplot(x=x, y=y, kind='hex')
plt.show()
