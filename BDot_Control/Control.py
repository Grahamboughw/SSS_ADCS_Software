import numpy as np

def Control(BB, pqr):
    k = 476200
    current = k*np.cross(pqr, BB)
    # current saturation if > 0.04 amps
    if np.sum(np.abs(current)) > 0.158:
        current = current/np.linalg.norm(current)*0.04
    return current
