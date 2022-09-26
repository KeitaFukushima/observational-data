# %%
import numpy as np
import math

file = "data/SHMR/stefanon2021_z10.csv"

d = np.loadtxt(file)

for line in d:
  c1 = line[0]
  c2 = math.log10(line[1]*1e-3)
  c3 = c2 - math.log10((line[1]-line[2])*1e-3)
  c4 = math.log10((line[1]+line[3])*1e-3) - c2
  print("{:.3f}, {:.3f}, {:.3f}, {:.3f}".format(c1, c2, c3, c4))
# %%
