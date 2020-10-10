# Python script for testing Triad software with sun sensors and accelerometer data #
import numpy as np
from triad_class_sheppard import TRIAD
from quaternion_operations import quaternion_product, inverse_quaternion
from EulerAngles2Quaternions import EulerAngles2Quaternions
from YZXEuler2Quat import euler2quat

# input Euler angle rotations
roll = np.radians(0)
pitch = np.radians(90)
yaw = np.radians(-90)
angles = np.array([roll,pitch,yaw])
print("Woodsat Euler Angles (roll-pitch-yaw): ", np.degrees(angles))

# expected quaternion
#q_expected = EulerAngles2Quaternions(angles)
q_expected = euler2quat(roll, pitch, yaw)
print("Expected Quaternion: ", q_expected)

# reference vectors
sun_ref = np.array([-1.0, 0.0, 0.0])
acc_ref = np.array([0.0, 0.0, 1.0])

# measured vectors
sun_meas = np.array([-0.1799, 2.2422, 1.4484])
acc_meas = np.array([0.02, -0.98, 0.19])

# compute attitude
triad_object = TRIAD(sun_meas, acc_meas, sun_ref, acc_ref)
rot_triad = triad_object.triad()
print("Attitude Output: ", rot_triad)

# compute error quaternion and error angle
error_quat = quaternion_product(q_expected, inverse_quaternion(rot_triad))
theta_error = np.degrees(2*np.arccos(error_quat[0]))
print("Error Angle: ", theta_error)