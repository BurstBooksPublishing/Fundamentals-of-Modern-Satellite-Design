import numpy as np
# Very small, illustrative example; use real FEA library for production.
nelx, nely = 60, 20                 # elements in x,y
volfrac, penal = 0.2, 3.0
# Initialize density field
rho = volfrac * np.ones((nely, nelx))
# Stiffness assembly placeholder (user replaces with FEA)
def assemble_K(rho):
    # returns global stiffness K and force vector F, solves Ku=F
    # Here: mock compliance decreasing with rho for demonstration.
    K_eff = np.sum(rho**penal)
    # Return dummy displacement and compliance
    u = 1.0/K_eff
    compliance = np.dot(rho.flatten(), rho.flatten())/K_eff
    return u, compliance
# Optimization loop (very small iteration count)
for it in range(80):
    u, c = assemble_K(rho)
    # Sensitivity: dc/drho ~ -penal*rho^(penal-1)*u^2 (mock)
    dc = -penal * rho**(penal-1) * u**2
    # Optimality update with volume constraint via simple bisection
    l1, l2 = -1e9, 1e9
    while (l2-l1)>1e-4:
        lmid = 0.5*(l1+l2)
        rho_new = np.maximum(0.001, np.minimum(1.0, np.sqrt(-dc/lmid))) # heuristic
        if rho_new.mean() - volfrac > 0:
            l1 = lmid
        else:
            l2 = lmid
    rho = rho_new
# Export optimized density field (map to lattice or printable geometry)
np.savetxt('topopt_density.csv', rho, delimiter=',')  # post-process externally