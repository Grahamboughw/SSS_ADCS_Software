## Make sure TRIAD4.ino is running on Arduino before running this script ##

import numpy as np
import serial
import time
import csv

# enable communication with Arduino
arduino_data = serial.Serial('COM4', 9600, timeout=1)

# define amount of time to collect data for (10 seconds)
end_time = time.time() + 10

# open csv file to write data
f = open("Testing7.csv", 'w', newline="")
w = csv.writer(f)

# create csv file headers for data
fields = ['x', 'y', 'z']
w.writerow(fields)

# read data from arduino
while time.time() < end_time:
    val = arduino_data.readline().decode('ascii')
    val_cleaned = val.replace("\r\n", "")
    val_split = val_cleaned.split(",")
    # if data is valid, convert to numpy array
    try:
        val_flt = np.array(val_split, dtype=np.float)
        print(val_flt)
        print()
        # create numpy array containing all output parameters
        outputs = val_flt
        # write TRIAD output to csv file
        w.writerow(outputs)
    except ValueError:
        pass
        print("Error or waiting for data.")
        print()