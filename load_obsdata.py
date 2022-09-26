import numpy as np
import subprocess
import os

def load_obsdata(tag, z1, z2):
  """
  returns observational data points

  Parameters
  ----------
  tag: string
    which statistics to load
  z1: double
    minimum redshift of data to load
  z2: double
    maximum redshift of data to load
  
  Returns
  -------
  out: list of dictionary
    list of dictionaries containing data points and labels
    out[i]["x"]: x-axis
    out[i]["y"]: y-axis (average)
    out[i]["y1"]: y-axis (average - sigma)
    out[i]["y2"]: y-axis (average + sigma)
    out[i]["label"]: label in format of e.g., Oku+ 21 (z=0)
    out[i]["author"]: author
    out[i]["z"]: redshift
    out[i]["year"]: published year
  
  Examples
  --------
  >>> load_obsdata("SMF", 0, 2)
  """

  out = []
  rootdir = os.getenv("OBSDATA_DIR")
  if rootdir == None:
    print("ERROR: environment variable OBSDATA_DIR is not set")
    exit()
  cmd = "ls -U1 "+rootdir+"/data/"+tag+"/*.csv"
  cp = subprocess.run(cmd, capture_output=True, text=True, shell=True)
  fname = cp.stdout.split("\n")
  for f in fname:
    if f == "":
      continue
    print("\nReading "+f)
    x = [] # x-axis
    y = [] # y-axis
    sm = [] # sigma minus
    sp = [] # sigma plus

    with open(f, "r") as fp:
      while 1:
        line = fp.readline()
        if not line:
          break # EOF
        line.rstrip(os.linesep)

        word = [w.strip() for w in line.split(",")]
        if word[0] == "#REF":
          ref = word[1]
        if word[0] == "#AUTHOR":
          author = word[1]
        if word[0] == "#YEAR":
          year = word[1]
        if word[0] == "#REDSHIFT":
          z = word[1]
        if word[0] == "#COLUMN1":
          xaxis = word[1]
        if word[0] == "#COLUMN2":
          yaxis = word[1]
        if word[0] == "#NOTE":
          note = line.lstrip("#")
        
        # skip header
        if word[0][0] == "#":
          continue
        
        x.append(float(word[0]))
        y.append(float(word[1]))
        sm.append(float(word[2]))
        sp.append(float(word[3]))
    # file reading done
    
    # skip data if out of redshift range
    if float(z) < z1 or float(z) > z2:
      print("Out of redshift range. skipping...")
      continue
    
    print("Loading data of "+author.replace("+", " et al.")+" ("+year+") at z="+z)
    print("X-axis: "+xaxis+", Y-axis: "+yaxis)
    print("Reference: "+ref)
    print(note)
    data = {
      "x" : np.array(x),
      "y" : np.array(y),
      "y1" : np.array(y) - np.array(sm),
      "y2" : np.array(y) + np.array(sp),
      "label": author+" "+year[-2:]+" (z="+z+")",
      "author": author,
      "z" : z,
      "year" : year,
    }

    out.append(data)
  # end loop over files

  return out
