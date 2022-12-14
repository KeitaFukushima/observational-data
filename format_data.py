# %%
import numpy as np
import math

file = "data/MZR/N_O/andrews2013_z0.1.csv"

d = np.loadtxt(file)

# ncol = len(d[0])
# for i in range(ncol):
#   c1 = d[0][i]
#   c2 = d[1][i]
#   c3 = d[2][i]
#   c4 = d[2][i]
#   print("{:.3f}, {:.3f}, {:.3f}, {:.3f}".format(c1, c2, c3, c4))

for line in d:
    c1 = (line[0] + line[1]) / 2
    c2 = line[2]
    c3 = line[3]
    c4 = line[3]
    print("{:.3f}, {:.3f}, {:.3f}, {:.3f}".format(c1, c2, c3, c4))
# %%
