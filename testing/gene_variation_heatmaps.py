import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pandas as pd
import math

def data_coord2view_coord(p, vlen, pmin, pmax):
    dp = pmax - pmin
    dv = (p - pmin) / dp * vlen
    return dv


def nearest_neighbours(xs, ys, reso, n_neighbours):
    im = np.zeros([reso, reso])
    extent = [np.min(xs), np.max(xs), np.min(ys), np.max(ys)]

    xv = data_coord2view_coord(xs, reso, extent[0], extent[1])
    yv = data_coord2view_coord(ys, reso, extent[2], extent[3])
    for x in range(reso):
        for y in range(reso):
            xp = (xv - x)
            yp = (yv - y)

            d = np.sqrt(xp**2 + yp**2)

            im[y][x] = 1 / np.sum(d[np.argpartition(d.ravel(), n_neighbours)[:n_neighbours]])

    return im, extent

n = 1000


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

xs = mean
ys = scaled_cv
resolution = 250

neighbours = 16
if neighbours == 0:
    plt.plot(xs, ys, 'k.', markersize=2)
    plt.set_aspect('equal')
    plt.title("Scatter Plot")
else:
    im, extent = nearest_neighbours(xs, ys, resolution, neighbours)
    plt.imshow(im, origin='lower', extent=extent, cmap=cm.bone)
    plt.title("Raw Transcript counts from single-cells")
    plt.xlim(extent[0], extent[1])
    plt.ylim(extent[2], extent[3])
plt.show()


rank_norm_data = pd.read_csv('./data/rna/raw_pagoda.csv', header=None, index_col=False)
mean_express = []
for row in rank_norm_data[0]:
    mean_express.append(math.log10(row))
var = []
for row in rank_norm_data[1]:
    var.append(row)
xs = mean_express
ys = var
resolution = 250

neighbours = 16
if neighbours == 0:
    plt.plot(xs, ys, 'k.', markersize=2)
    plt.set_aspect('equal')
    plt.title("Scatter Plot")
else:
    im, extent = nearest_neighbours(xs, ys, resolution, neighbours)
    plt.imshow(im, origin='lower', extent=extent, cmap=cm.bone)
    plt.title("PAGODA")
    plt.xlim(extent[0], extent[1])
    plt.ylim(extent[2], extent[3])
plt.show()


rank_norm_data = pd.read_csv('./data/rna/rank_normalization_filtered.csv', header=None, index_col=False)
mean_express_rank = []
for row in rank_norm_data[0]:
    mean_express_rank.append(math.log(row))
var_rank = []
for row in rank_norm_data[1]:
    var_rank.append(row)
xs = mean_express_rank
ys = var_rank
resolution = 250

neighbours = 16
if neighbours == 0:
    plt.plot(xs, ys, 'k.', markersize=2)
    plt.set_aspect('equal')
    plt.title("Scatter Plot")
else:
    im, extent = nearest_neighbours(xs, ys, resolution, neighbours)
    plt.imshow(im, origin='lower', extent=extent, cmap=cm.bone)
    plt.title("Rank Normalized")
    plt.xlim(extent[0], extent[1])
    plt.ylim(extent[2], extent[3])
plt.show()
