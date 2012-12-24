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
gamma_1 = Normal('gamma_method', mu=0.0, tau=0.01, value=0.0)
# Functional group average detection
gamma_2 = Normal('gamma_fg', mu=0.0, tau=0.01, value=np.zeros(nfg))
# Detection model
gamma_mu = Lambda('gamma_mu', lambda g1=gamma_1,g2=gamma_2[Ifg]: g1*method+g2, trace=False)
# Logit detection
theta_ij = Lambda('theta_ij', lambda mu=gamma_mu: invlogit(mu), trace=False)

## Occupancy ##
# Grand mean occupancy
beta_0 = Normal('beta_int', mu=0.0, tau=0.01, value=0.0)
# Location-level average occupancy
beta_1 = Normal('beta_loc', mu=beta_0, tau=0.01, value=np.zeros(nloc))
# Logit occupancy
psi_ij = Lambda('psi_ij', lambda b1=beta_1[Il]: invlogit(b1), trace=False)


### Latent-state implementation
#------------------------------------------------ Model
# Latent occupancy
z_ij = Bernoulli('z_ij', p=psi_ij, value=np.ones(nsamp))
# Occupancy*detection
p_ij = Lambda('p_ij', lambda z_ij=z_ij[Ii],p_ij=theta_ij: z_ij*p_ij, trace=False)

#------------------------------------------------ Likelihood
Y_ij = Bernoulli('y_ij', p=p_ij, value=y_ij, observed=True)






