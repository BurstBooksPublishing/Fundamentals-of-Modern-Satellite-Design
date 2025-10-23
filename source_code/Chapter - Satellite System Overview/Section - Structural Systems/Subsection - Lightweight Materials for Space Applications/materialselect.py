import numpy as np

# Material database: [density(kg/m3), E(GPa), strength(MPa), alpha(1e-6/K), ao_resistance(0-1)]
materials = {
    'Al6061': [2700, 69, 310, 23.6, 0.6],
    'Ti6Al4V': [4430, 114, 900, 9.0, 0.9],
    'CFRP': [1600, 150, 1200, 0.0, 0.5],  # example orthotropic idealized
    'Sandwich': [1200, 60, 200, 10.0, 0.7],
}

weights = {'mass':0.4, 'stiffness':0.3, 'thermal':0.2, 'env':0.1}
scores = {}
for name, props in materials.items():
    rho, E, sig, alpha, ao = props
    S = E*1e9 / rho                        # specific stiffness (Pa/(kg/m3))
    mass_score = 1/(rho/2700)              # relative mass pref to Al6061
    stiff_score = S / (69e9/2700)          # normalize to Al6061 specific stiffness
    thermal_score = 1/(abs(alpha)/23.6+1e-6) # smaller alpha better
    env_score = ao                          # AO proxy
    total = (weights['mass']*mass_score +
             weights['stiffness']*stiff_score +
             weights['thermal']*thermal_score +
             weights['env']*env_score)
    scores[name] = total

print(scores)  # picks material with highest weighted score