import math
# candidate data: E (Pa), density (kg/m^3), yield (Pa)
materials = {
  'CFRP_tape': {'E':70e9,'rho':1600,'sigma_y':600e6},
  'Ti6Al4V':  {'E':114e9,'rho':4430,'sigma_y':880e6},
  'Al7075_T6':{'E':71.7e9,'rho':2810,'sigma_y':505e6},
  'SME_NiTi':  {'E':28e9,'rho':6450,'sigma_y':900e6}
}
L=5.0       # free length meter
K=1.0       # pinned-pinned conservative
I=1e-6      # moment of inertia m^4 (example thin-wall tube)
for name,prop in materials.items():
    Pcr = math.pi**2 * prop['E'] * I / (K*L)**2
    m_per_m = prop['rho'] * (math.pi* (0.02**2)/4) # approx tube area for screening
    print(f"{name}: Pcr={Pcr/1e3:.1f} kN, m/m={m_per_m:.2f} kg/m")
# Inline comments show purpose: quick screening results for structural trade.