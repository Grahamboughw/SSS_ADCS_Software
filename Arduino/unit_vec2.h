#include <math.h>
#include <stdio.h>
#include <Arduino.h>

#ifndef UNIT_VEC_H
#define UNIT_VEC_H

typedef struct
{
  float x;
  float y;
  float z;
} Uvec;

void gen_unit_vec(float x, float y, float z, Uvec* vec_in);
void print_unit_vec_x(Uvec vec_in);
void print_unit_vec_y(Uvec vec_in);
void print_unit_vec_z(Uvec vec_in);

#endif
