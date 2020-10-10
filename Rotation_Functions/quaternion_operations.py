# File quaternion_operations.py
# Contains function definitions for quaternion operations

import numpy as np

# function definition for quaternion product
def quaternion_product(quat_1, quat_2):
    q1 = np.array(quat_1)
    q2 = np.array(quat_2)
    q1_v = np.array([q1[1], q1[2], q1[3]])
    q2_v = np.array([q2[1], q2[2], q2[3]])

    quat_prod1 = q1[0]*q2[0] - np.dot(q1_v, q2_v)
    quat_prod2 = q1[0]*q2_v + q2[0]*q1_v - np.cross(q1_v, q2_v)

    quat_product = np.array([quat_prod1, quat_prod2[0], quat_prod2[1], quat_prod2[2]])
    
    return quat_product

# function definition for inverse quaternion
def inverse_quaternion(quat):
    q = np.array(quat)
    inv_quat = np.array([q[0], -1*q[1], -1*q[2], -1*q[3]])

    return inv_quat