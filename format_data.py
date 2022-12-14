# %%
import numpy as np
import math

file = "data/SFMS/salmon2015_z6.csv"

d = np.loadtxt(file)

ncol = len(d[0])

for i in range(ncol):
  c1 = d[0][i]
  c2 = d[1][i]
  c3 = d[2][i]
  c4 = d[2][i]
  print("{:.3f}, {:.3f}, {:.3f}, {:.3f}".format(c1, c2, c3, c4))

# for line in d:
#     c1 = line[0]
#     c2 = math.log10(line[16])
#     c3 = c2 - math.log10(line[16] - line[18])
#     c4 = math.log10(line[16] + line[17]) - c2
#     print("{:.3f}, {:.3f}, {:.3f}, {:.3f}".format(c1, c2, c3, c4))
# %%
