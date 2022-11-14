# observational-data

Usage
=====
Set environment variables as follows
```
export OBSDATA_DIR=/absolute/path/to/this/directory
export PYTHONPATH=$OBSDATA_DIR:$PYTHONPATH
```

Example
=======
``` python
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
```
<img src="./example.png" width=500px>

The figure above is plotted with [this matplotlibrc](https://gist.github.com/YuriOku/964adda6649e0bbc76de1a8f9010fe1a)