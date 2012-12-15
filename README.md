volunteer_uvc
=============

Occupancy example for Holt et al. (2013) Methods in Ecology and Evolution xx:xxx-xxx.

PyMC code is provided to implement a simple latent-state occupancy model to estimate reef fish species richness at dive locations in the Turks and Cacos, given various covariates for detection and occupancy. Specifically interest was in identifying differences in detection between belt transects and roving diver surveys. The models used follow from those of Dorazio et al. (2006), whereby a fixed species list of potential local inhabitants (n=295) is used to fix the dimensionality of the model. 


Dorazio, R.M. and Royle, J.A. and Söderström, B. and Gilmskär (2006) Estimating species richness and accumulation by modelling species occurrence and detectability. Ecology 87(4):842-854.



# = = = = DATA = = = = #

yitk: observation array, indicating the observation of species i (n=295) on transect t (n=24) at site k (n=6)

nfg: number of reef fish functional groups for hierarchy

nloc: number of sites (n=3) by season (n=2) combinations

nspp: number of species

nsites: number of sites

Ifg: functional group indexing array

method: dummy variable for belt transect (1) or roving diver (0) survey

duration: observation time (min)

visibility: underwater visability (ft)

Ii: detection indexing for occupancy 

Is: site indexing array

Il: location indexing array





