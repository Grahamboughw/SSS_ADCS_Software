# File trajectoryTransform.py #

import numpy as np
import math
import rotations

# Function to transform from ECI to trajectory (LVLH) frame
# omega = right ascension of ascending node, i = inclination, w = argument of periapsis, f = true anomaly
def ECI_to_trajectory(omega, i, w, f, ECI_vector):
    # Reference vector in ECI frame
    vector = np.asmatrix(ECI_vector)

    # Construct rotation matrix from ECI to trajectory frame
    rot_temp = np.dot(rotations.rot_z(np.pi+w+f), rotations.rot_x(i))
    rot = np.dot(rot_temp, rotations.rot_z(omega))

    # Map ECI vector to trajectory frame
    LVLH_vector = np.dot(rot, vector)

    # Output trajectory frame vector
    return LVLH_vector




