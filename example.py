# %%
import matplotlib.pyplot as plt
import load_obsdata as obs

cmap = plt.get_cmap("tab10")
linecolors = [cmap(i) for i in range(10)]
linestyles = ["solid", "dashed", "dotted", "dashdot"]
def lcol(i):
  return linecolors[i % len(linecolors)]
def lsty(i):
  return linestyles[i % len(linestyles)]

d = obs.load_obsdata("SMF", 4, 6)

plt.figure(facecolor="white")
for i in range(len(d)):
  di = d[i]
  plt.plot(di["x"], di["y"], color=lcol(i), linestyle=lsty(i), label=di["label"])
  plt.fill_between(di["x"], di["y1"], di["y2"], color=lcol(i), alpha=0.3)
plt.xlabel(r"log M$_*$ [M$_\odot$]")
plt.ylabel(r"log $\Phi$ [dex$^{-1}$ Mpc$^{-3}$]")
plt.legend()
plt.savefig("example.png")
plt.close()
# %%
