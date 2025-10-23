# Simple trade: compute required area and specific power for given mission
G0 = 1361.0               # W/m^2
P_req = 500.0             # desired average power W
eta = 0.30                # cell+system efficiency
cos_theta = 0.95          # typical Sun incidence factor
f_e = 0.0                 # eclipse fraction (GEO example)
m_a_fixed = 8.0           # kg/m^2 fixed panel areal density
m_a_deploy = 3.0          # kg/m^2 deployable flexible array
m_mech = 50.0             # kg mechanical mass for deployable

# area required (from eq. 2)
A_req = P_req / (G0 * eta * cos_theta * (1.0 - f_e))
m_fixed = m_a_fixed * A_req                # fixed total mass
m_deploy = m_a_deploy * A_req + m_mech     # deployable total mass

# specific power metrics
sp_fixed = P_req / m_fixed
sp_deploy = P_req / m_deploy

print(f"A_req = {A_req:.2f} m^2, sp_fixed = {sp_fixed:.1f} W/kg, sp_deploy = {sp_deploy:.1f} W/kg")
# use results to inform decision threshold