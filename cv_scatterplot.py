import pandas as pd
import math
import matplotlib.pyplot as plt
import pylab

cv_data = pd.read_csv('./data/rna/coef_var_filtered.txt', sep='\t', header=None, index_col=False)
genes = []
for row in cv_data[0]:
    genes.append(row)
cv = []
for row in cv_data[1]:
    cv.append(row)
mean = []
for row in cv_data[2]:
    mean.append(row)
#norm_mean = [float(i)/max(mean) for i in mean]
scaled_cv = []
for val in cv:
    scaled_cv.append(math.log10(val ** 2))
#norm_cv = [float(i)/max(pre_norm_cv) for i in pre_norm_cv]

plt.title("Raw Transcript counts from single-cells")
plt.ylabel("Noise in transript counts log(CV^2)")
plt.xlabel("Average transcript counts")
plt.scatter(mean, scaled_cv, s=1, color='purple')
plt.show()


plt.title("Raw Transcript counts from single-cells")
plt.ylabel("Noise in transript counts log(CV^2)")
plt.xlabel("Average transcript counts")
plt.xlim(-5,500)
plt.scatter(mean, scaled_cv, s=1, color='purple')
plt.show()

plt.title("Raw Transcript counts from single-cells")
plt.ylabel("Noise in transript counts log(CV^2)")
plt.xlabel("Average transcript counts")
plt.xlim(-5,150)
plt.scatter(mean, scaled_cv, s=1, color='purple')
plt.show()

plt.title("Raw Transcript counts from single-cells")
plt.ylabel("Noise in transript counts log(CV^2)")
plt.xlabel("Average transcript counts")
plt.xlim(-5,60)
plt.scatter(mean, scaled_cv, s=1, color='purple')
plt.show()

