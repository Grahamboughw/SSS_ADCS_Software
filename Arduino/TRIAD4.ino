#include "MPU9250.h"  // Copyright (c) 2017 Bolder Flight Systems
#include "unit_vec2.h"

// declare MPU9250 object
MPU9250 IMU(Wire,0x68);
int status;

void setup() {
  // begin serial connection to display data
  Serial.begin(9600);
  while(!Serial) {}

  // check status of connection with MPU9250 sensor
  status = IMU.begin();
}

void loop() {
  // delay between measurements
  delay(500);

  // read data from accelerometer
  IMU.readSensor();

  float ax, ay, az;
  ax = IMU.getAccelX_mss();
  ay = IMU.getAccelY_mss();
  az = IMU.getAccelZ_mss(); // take +z axis to be when top of sensor is facing toward ground

  // declare general unit vector
  Uvec unit_accel;

  // display accelerometer data
  gen_unit_vec(ax, ay, az, &unit_accel);
  //Serial.print(",");
  print_unit_vec_x(unit_accel);
  Serial.print(",");
  print_unit_vec_y(unit_accel);
  Serial.print(",");
  print_unit_vec_z(unit_accel);
}
