# %%
import numpy as np
import math
import re

file = "data/BH/mcconnel-2.txt"

# d = np.loadtxt(file)

# open file
f = open(file, "r")
# read the whole file into a single variable, which is a list of every row of the file.
lines = f.readlines()
f.close()
# initialize some variable to be lists:
x = []
y = []
z = []
# scan the rows of the file stored in lines, and put the values into some variables:
for line in lines:
    p = re.split('\t| ', line) #line.split("\t")
    # print(p)
    if float(p[13]) <= 0:
        continue
    c1 = math.log10(float(p[13]))
    c2 = math.log10(float(p[2]))
    c3 = math.log10(float(p[2])) - math.log10(float(p[3]))
    c4 = math.log10(float(p[4])) - math.log10(float(p[2]))
    print("{:.3f}, {:.3f}, {:.3f}, {:.3f}".format(c1, c2, c3, c4))

# ncol = len(d[0])
# for i in range(ncol):
#   c1 = d[0][i]
#   c2 = d[1][i]
#   c3 = d[2][i]
#   c4 = d[2][i]
#   print("{:.3f}, {:.3f}, {:.3f}, {:.3f}".format(c1, c2, c3, c4))

# for line in d:
#     c1 = line[13]
#     c2 = line[2]
#     c3 = line[2] - line[3]
#     c4 = line[4] - line[2]
    # print("{:.3f}, {:.3f}, {:.3f}, {:.3f}".format(c1, c2, c3, c4))
# %%
