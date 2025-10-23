import numpy as np

# material properties: [E (Pa), rho (kg/m3)]
materials = {
    'CFRP': (150e9, 1600),
    'Al7075': (71.7e9, 2810)
}

# required bending stiffness parameter (E*I) target (arbitrary reference)
target_EI = 1.0e6  # N*m^2 for demonstration

for name,(E,rho) in materials.items():
    # compute required I to meet target_EI
    I_req = target_EI / E
    # assume panel area A = 1 m2 and approximate mass ~ rho * thickness
    # approximate thickness from I ~ b*t^3/12 for monolithic plate, b=1
    t_req = (12*I_req)**(1/3)
    mass_est = rho * t_req * 1.0  # kg/m2
    S = E/rho
    print(f"{name}: S={S:.2e} m2/s2, t_req={t_req*1e3:.2f} mm, mass={mass_est:.2f} kg/m2")
# Inline comments explain simplifications.