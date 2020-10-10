# SSS ADCS Software
This is a repository containing the code for the projects that I have worked on as a part of the UC Davis Space and Satellite Systems Club ADCS Software Team. Below are descriptions of each of the folders included in this repository.

## Arduino
This folder contains the files used to interface with the Arduino for hardware testing. The MPU9250.h and MPU9250.cpp files were not written by me but are used for functions to access the accelerometer values from the MPU9250 IMU sensor. The unit_vec2.h and unit_vec2.cpp were written by another member of the SSS Club, and are used for functions to normalize the accelerometer vector. The TRIAD4.ino file was written by me to read accelerometer data from the MPU9250 IMU and print the normalized accelerometer vector.

## Attitude Determination
This folder contains the python files used for attitude determination. We are using the Triad method for attitude determination which requires a measured vector from two of our sensors as well as a reference vector for each measured vector as inputs. The output of Triad is a direction cosine matrix representation of the satellite's attitude, which is mapped to a quaternion using Sheppard's method. The triad_class_sheppard.py uses the Triad method to compute the attitude then uses Sheppard's method to map the attitude to a quaternion which is given as the output. The triad_class_test_sheppard.py file is used to test our Triad function by taking in an input attitude, using this attitude to generate the input vectors to the Triad function, and verifying that the Triad function outputs the same attitude. The triad_class_test_with_error.py file is also used to test the Triad function, but errors are added to the input vectors and the attitude error between the expected output and actual output is calculated. The sun_sensors_test_script.py file is used for hardware testing to calculate the attitude using data from sun sensors and an accelerometer sensor, as well as defined reference vectors.

## BDot Control
This folder contains the python code for the detumbling simulation of our satellite in orbit using the Bdot control method. This code was adapted from Carlos Jose Montavlo's ADCS Seminar Series MATLAB code which can be found here https://github.com/cmontalvo251/MATLAB/tree/master/ADCS_Seminar_Series. The main.py file runs the simulation of the satellite dynamics and Earth's magnetic field throughout several orbits under Bdot control. Based on the Bdot control law, the magnetorquer control torque is calculated using the satellite's angular velocity and body frame magnetic field vector at each timestep. At the end of the simulation, several quantities are plotted over time such as position, magnetic field, angular velocity, and power usage.

## Reference Frame Transformations
This folder contains the files for transforming vectors between reference frames. Currently, the only file in this folder is trajectoryTransform.py which is used to map a vector from the Earth-Centered-Inertial (ECI) Frame to a frame we call the Trajectory Frame (also called Local Vertical Local Horizon Frame). Our Trajectory Frame is defined such that we have a coordinate axis normal to the plane of our orbit, and a coordinate axis that points toward the center of Earth at every point in our orbit. As more files are developed for coordinate/reference frame transformations, they will be added here.

## Rotation Functions
This folder contains python files with useful functions relating to rotations of vectors.
