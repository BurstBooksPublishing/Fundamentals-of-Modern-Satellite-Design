def battery_sizing(P_load_W, t_eclipse_h, DoD, eta_disch, R_EOL, E_density_Whkg):
    # compute usable energy needed (Wh)
    E_usable = P_load_W * t_eclipse_h
    # compute BOL capacity needed (Wh)
    C_BOL = E_usable / (DoD * eta_disch * R_EOL)
    # mass estimate (kg)
    mass = C_BOL / E_density_Whkg
    return C_BOL, mass

# Example inputs for a 3U EO CubeSat
P_load = 30.0          # W
t_eclipse = 35.0/60.0 # h
DoD = 0.6
eta = 0.95
R_EOL = 0.8
E_density = 150.0     # Wh/kg packaged

C, m = battery_sizing(P_load, t_eclipse, DoD, eta, R_EOL, E_density)
print(f"BOL capacity: {C:.1f} Wh  Estimated mass: {m:.3f} kg") # quick result