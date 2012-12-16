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
gamma1 = Normal('gamma_method', mu=0.0, tau=0.01, value=0.0)
# Functional group average detection
gamma2 = Normal('gamma_fg', mu=0.0, tau=0.01, value=np.zeros(nfg))
# Detection model
gamma_mu = Lambda('gamma_mu', lambda g1=gamma1,g2=gamma2[Ifg]: g1*method+g2, trace=False)
# Logit detection
thetaij = Lambda('theta_ij', lambda mu=gamma_mu: invlogit(mu), trace=False)

## Occupancy ##
# Grand mean occupancy
beta0 = Normal('beta_int', mu=0.0, tau=0.01, value=0.0)
# Location-level average occupancy
beta1 = Normal('beta_loc', mu=beta0, tau=0.01, value=np.zeros(nloc))
# Logit occupancy
psi = Lambda('psi', lambda b1=beta1[Il]: invlogit(b1), trace=False)

#------------------------------------------------ Model
# Latent occupancy
zij = Bernoulli('z_ij', p=psi, value=np.ones(nsamp))
# Occupancy*detection
pi = Lambda('pi', lambda zij=zij[Ii],pij=thetaij: zij*pij, trace=False)

#------------------------------------------------ Likelihood
Yitk = Bernoulli('yitk', p=pi, value=yitk, observed=True)


