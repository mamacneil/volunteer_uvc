# Python data file for Holt et al. (2013) Comparing diversity data collected using a protocol designed for volunteers with results from a professional alternative: a case study with Caribbean fish assemblages. Methods in Ecology and Evolution xx:xxx-xxx

# M.A. MacNeil 12/12/12!!

import sys
import os
import pdb
import numpy as np

## Response
# Load observations
yitk = np.loadtxt("Yobs.csv",delimiter=",").astype(int)

## Covariates
nfg = 5
nloc = 6
nspp = 294
nsites = 3

Ifg,method,duration,visibility,Ii = np.loadtxt("X1.csv",delimiter=",",dtype=int)

Is,Il = np.loadtxt("X2.csv",delimiter=",",dtype=int)

nsamp = len(Il)

