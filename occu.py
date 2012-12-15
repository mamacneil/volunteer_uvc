# PyMC model file for Holt et al. (2013) Comparing diversity data collected using a protocol designed for volunteers with results from a professional alternative: a case study with Caribbean fish assemblages. Methods in Ecology and Evolution xx:xxx-xxx

# M.A. MacNeil 12/12/12

import sys
import os
import pdb
import numpy as np

from pymc import *

from data import *

#------------------------------------------------ Priors
## Detection ##
# Method effect on detection
beta1 = Normal('p_method', mu=0.0, tau=0.01, value=0.0)
# Functional group average detection
beta2 = Normal('p_fg', mu=0.0, tau=0.01, value=np.zeros(nfg))
# Detection model
p_mu = Lambda('p_mu', lambda b1=beta1,b2=beta2[Ifg]: b1*method+b2, trace=False)
# Logit detection
pj = Lambda('pj', lambda mu=p_mu: invlogit(mu), trace=False)

## Occupancy ##
# Grand mean occupancy
theta0 = Normal('psi_gint', mu=0.0, tau=0.01, value=0.0)
# Location-level average occupancy
theta1 = Normal('psi_loc', mu=theta0, tau=0.01, value=np.zeros(nloc))
# Logit occupancy
psi = Lambda('psi', lambda t1=theta1[Il]: invlogit(t1), trace=False)

#------------------------------------------------ Model
# Latent occupancy
xi = Bernoulli('xi', p=psi, value=np.ones(nsamp))
# Occupancy*detection
pi = Lambda('pi', lambda xi=xi[Ii],pj=pj: xi*pj, trace=False)

#------------------------------------------------ Likelihood
Yitk = Bernoulli('yitk', p=pi, value=yitk, observed=True)


