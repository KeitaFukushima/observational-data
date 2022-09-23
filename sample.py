# %%
import matplotlib.pyplot as plt
import load_obsdata as obs

cmap = plt.get_cmap("tab10")
lcol = [cmap(i) for i in range(10)]
lsty = ["solid", "dashed", "dotted", "dashdot"]
ncol = len(lcol)
nsty = len(lsty)

d = obs.load_obsdata("SMF", 4, 6)

plt.figure(facecolor="white")
for i in range(len(d)):
  plt.plot(d[i]["x"], d[i]["y"], color=lcol[i%ncol], linestyle=lsty[i%nsty], label=d[i]["label"])
  plt.fill_between(d[i]["x"], d[i]["y1"], d[i]["y2"], color=lcol[i%ncol], alpha=0.3)
plt.xlabel(r"log M$_*$ [M$_\odot$]")
plt.ylabel(r"log $\Phi$ [dex$^{-1}$ Mpc$^{-3}$]")
plt.legend()
plt.show()
# %%
