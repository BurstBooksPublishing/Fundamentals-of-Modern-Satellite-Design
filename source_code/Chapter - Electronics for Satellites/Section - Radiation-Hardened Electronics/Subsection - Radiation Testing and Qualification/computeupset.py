import numpy as np
# flux [particles/cm2/s/MeV] and sigma [cm2] arrays binned over energy
flux = np.loadtxt('flux_spectrum.csv')   # columns: E_mid, dPhi_dE
sigma = np.loadtxt('sigma_curve.csv')    # columns: E_mid, sigma(E)
dE = np.diff(np.hstack(([0], (flux[1:,0]+flux[:-1,0])/2, [flux[-1,0]]))) # bin widths
# discrete upset rate (per second)
R = np.sum(flux[:,1] * sigma[:,1] * dE)  # integrate eq. (1)
# mission upsets for mission_time seconds
mission_time = 5*365*24*3600.0  # 5 years
N_mission = R * mission_time
# zero-event upper bound on sigma at 95% confidence
C = 0.95
fluence_test = 1e8  # particles/cm2 applied in test
sigma_max = -np.log(1-C) / fluence_test  # if zero upsets seen
print('Rate (s^-1)=', R, 'Expected mission upsets=', N_mission, 'sigma_max=', sigma_max)