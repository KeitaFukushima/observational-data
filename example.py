# %%
import matplotlib.pyplot as plt
import load_obsdata as obs

d = obs.load_obsdata("SMF", 5, 6)

plt.figure(facecolor="white")
for i in range(len(d)):
  di = d[i]
  plt.plot(di["x"], di["y"], label=di["label"], ms=3)
  plt.fill_between(di["x"], di["y1"], di["y2"], alpha=0.3)
plt.xlabel(r"log M$_*$ [M$_\odot$]")
plt.ylabel(r"log $\Phi$ [dex$^{-1}$ Mpc$^{-3}$]")
plt.legend()
plt.savefig("example.png")
plt.close()
# %%
