#include "unit_vec2.h"

void gen_unit_vec(float x, float y, float z, Uvec* vec_in)
{
  float magnitude = sqrt(square(x) + square(y) + square(z));
  vec_in->x = x / magnitude;
  vec_in->y = y / magnitude;
  vec_in->z = z / magnitude;
}

void print_unit_vec_x(Uvec vec_in)
{

	char f1[8], print_str[16];
	dtostrf(vec_in.x, 5, 2, f1);
	sprintf(print_str, "%s", f1);

	Serial.print(print_str);
}

void print_unit_vec_y(Uvec vec_in)
{

	char f2[8], print_str[16];
	dtostrf(vec_in.y, 5, 2, f2);
	sprintf(print_str, "%s", f2);

	Serial.print(print_str);
}

void print_unit_vec_z(Uvec vec_in)
{

	char f3[8], print_str[16];
	dtostrf(vec_in.z, 5, 2, f3);
	sprintf(print_str, "%s", f3);

	Serial.println(print_str);
}


