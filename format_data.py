# %%
import numpy as np
import math

file = "data/SHMR/behroozi2019_z10.csv"

d = np.loadtxt(file)

for line in d:
  if line[15] != 0:
    c1 = line[0]
    c2 = line[4]
    c3 = line[6]
    c4 = line[5]
    print("{:.3f}, {:.3f}, {:.3f}, {:.3f}".format(c1, c2, c3, c4))
# %%
