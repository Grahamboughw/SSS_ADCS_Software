# Function to transform from YZX Euler Angles to Quaternion Representation #
# File created to be used for testing with Woodsat #
import numpy as np

def euler2quat(phi, theta, psi):

    cp = np.cos(phi/2)
    sp = np.sin(phi/2)
    ct = np.cos(theta/2)
    st = np.sin(theta/2)
    cs = np.cos(psi/2)
    ss = np.sin(psi/2)

    q1 = -st*ss*sp + ct*cs*cp
    q2 = st*ss*cp + sp*ct*cs
    q3 = st*cs*cp + ss*sp*ct
    q4 = -st*sp*cs + ss*ct*cp

    q = np.array([q1, q2, q3, q4])

    return q