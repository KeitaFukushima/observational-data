import numpy as np
import subprocess
import os

def load_obsdata(key, z1, z2, IMF="Chabrier", verbose=False):
    """
    returns observational data points

    Parameters
    ----------
    key: string
      which data to load
    z1: double
      minimum redshift of data to load
    z2: double
      maximum redshift of data to load
    IMF: string
      correct stellar mass for the IMF

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

    def pprint(txt):
        if verbose == True:
            print(txt)
        else:
            pass

    if IMF != "Chabrier" and IMF != "Salpeter":
        raise ValueError("Choose IMF from Chabrier or Salpeter")

    out = []
    rootdir = os.getenv("OBSDATA_DIR")
    if rootdir == None:
        raise Exception("ERROR: environment variable OBSDATA_DIR is not set")
    cmd = "ls -v1 "+rootdir+"/data/"+key+"/*.csv"
    cp = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    fname = cp.stdout.split("\n")
    for f in fname:
        if f == "":
            continue
        pprint("\nReading "+f)
        x = []  # x-axis
        y = []  # y-axis
        sm = []  # sigma minus
        sp = []  # sigma plus

        with open(f, "r") as fp:
            while 1:
                line = fp.readline()
                if not line:
                    break  # EOF
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
                if word[0] == "#IMF":
                    data_imf = word[1]

                # skip header
                if word[0][0] == "#":
                    continue

                for i in range(4):
                    if word[i] == "inf":
                        word[i] = np.inf
                    else:
                        word[i] = float(word[i])

                x.append(word[0])
                y.append(word[1])
                sm.append(word[2])
                sp.append(word[3])
            # end while
        # end file open

        # skip data if out of redshift range
        if float(z) < z1 or float(z) > z2:
            pprint("Out of redshift range. skipping...")
            continue

        # IMF correction
        convert_chabrier_to_salpeter = np.log10(1.7)
        if key == "SMF":
            if data_imf != "Chabrier" and data_imf != "Salpeter":
                raise Exception("IMF not found in the header")
            if IMF == "Salpeter" and data_imf == "Chabrier":
                x += convert_chabrier_to_salpeter
            elif IMF == "Chabrier" and data_imf == "Salpeter":
                x -= convert_chabrier_to_salpeter
        elif key == "SHMR":
            if data_imf != "Chabrier" and data_imf != "Salpeter":
                raise Exception("IMF not found in the header")
            if IMF == "Salpeter" and data_imf == "Chabrier":
                y += convert_chabrier_to_salpeter
            elif IMF == "Chabrier" and data_imf == "Salpeter":
                y -= convert_chabrier_to_salpeter
        elif key == "SFRF":
            if data_imf != "Chabrier" and data_imf != "Salpeter":
                raise Exception("IMF not found in the header")
            if IMF == "Salpeter" and data_imf == "Chabrier":
                x += convert_chabrier_to_salpeter
            elif IMF == "Chabrier" and data_imf == "Salpeter":
                x -= convert_chabrier_to_salpeter

        pprint("Loading data of "+author.replace("+",
              " et al.")+" ("+year+") at z="+z)
        pprint("X-axis: "+xaxis+", Y-axis: "+yaxis)
        pprint("Reference: "+ref)
        pprint(note)
        data = {
            "x": np.array(x),
            "y": np.array(y),
            "y1": np.array(y) - np.array(sm),
            "y2": np.array(y) + np.array(sp),
            "label": author+" "+year[-2:]+" (z="+z+")",
            "author": author,
            "z": z,
            "year": year,
        }

        out.append(data)
    # end loop over files

    return out
