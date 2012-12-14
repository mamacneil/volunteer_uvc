# PyMC MCMC file for Holt et al. (2013) Comparing diversity data collected using a protocol designed for volunteers with results from a professional alternative: a case study with Caribbean fish assemblages. Methods in Ecology and Evolution xx:xxx-xxx

# M.A. MacNeil 12/12/12

import sys
import os
import pdb
import numpy as np

from pymc import *
import occu
from data import *

M = MCMC(occu)

M.isample(100000, 60000, thin=100, verbose=2)

try:
    os.mkdir('Outputs')
except OSError:
    pass
os.chdir('Outputs')
M.write_csv("occupancy_results.csv")
Matplot.plot(M)
