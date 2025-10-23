import cmath, math

def reflection_coeff(Zl, Z0=50):  # complex impedances allowed
    return (Zl - Z0) / (Zl + Z0)

def vswr(Gamma):
    g = abs(Gamma)
    return (1 + g) / (1 - g) if g < 1 else float('inf')  # check

def l_network(Rs, Rl):  # narrowband real-resistance case
    if Rl == Rs:
        return None  # no matching needed
    if Rl > Rs:
        Q = math.sqrt(Rl/Rs - 1)
        Xs = Rs * Q          # series reactance
        Xp = Rl / Q          # shunt reactance (magnitude)
    else:
        Q = math.sqrt(Rs/Rl - 1)
        Xs = Rl * Q          # series reactance (alternate orientation)
        Xp = Rs / Q
    return Q, Xs, Xp

# example: antenna 38 - j6 ohm at 3.7 GHz
Zant = 38 - 1j*6
Z0 = 50
G = reflection_coeff(Zant, Z0)
print("Gamma", G)              # small inline comment
print("VSWR", vswr(G))
print("Delivered fraction", 1 - abs(G)**2)
print("L-net for Rs=50, Rl=38:", l_network(50, 38))