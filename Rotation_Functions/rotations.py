# File rotations.py
# Contains function definitions for single-axis rotations about x,y,z axes

import numpy as np

# Define function for x-axis rotation matrix
def rot_x(r):
    s = np.sin(r)
    c = np.cos(r)
    return np.array([
        [1, 0, 0],
        [0, c, -s],
        [0, s, c]
        ])

# Define function for y-axis rotation matrix
def rot_y(p):
    s = np.sin(p)
    c = np.cos(p)
    return np.array([
        [c, 0, s],
        [0, 1, 0],
        [-s, 0, c]
    ])

# Define function for z-axis rotation matrix
def rot_z(y):
    s = np.sin(y)
    c = np.cos(y)
    return np.array([
        [c, -s, 0],
        [s, c, 0],
        [0, 0, 1]
    ])
