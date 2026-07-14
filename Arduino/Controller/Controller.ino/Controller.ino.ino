/**
 *
 * HX711 library for Arduino - example file
 * https://github.com/bogde/HX711
 *
 * MIT License
 * (c) 2018 Bogdan Necula
 *
**/
#include "HX711.h"

const int LEFT_DOUT_PIN = 26;
const int LEFT_SCK_PIN = 27;

const int RIGHT_DOUT_PIN = 18;
const int RIGHT_SCK_PIN = 19;


HX711 left;
HX711 right;

long leftVal = 0;
long rightVal = 0;

void setup() {
  Serial.begin(921600);
  Serial.println("Cuddle Pong Controller");

  Serial.println("Initializing scales");

  // Initialize library with data output pin, clock input pin and gain factor.
  // Channel selection is made by passing the appropriate gain:
  // - With a gain factor of 64 or 128, channel A is selected
  // - With a gain factor of 32, channel B is selected
  // By omitting the gain factor parameter, the library
  // default "128" (Channel A) is used here.
  left.begin(LEFT_DOUT_PIN, LEFT_SCK_PIN);
  right.begin(RIGHT_DOUT_PIN, RIGHT_SCK_PIN);
						// by the SCALE parameter (not set yet)

  //scale.set_scale(2280.f);                      // this value is obtained by calibrating the scale with known weights; see the README for details
  //scale.tare();				        // reset the scale to 0

}

void loop() {
  leftVal = left.read();
  rightVal = right.read();
  Serial.print(leftVal);
  Serial.print(",");
  Serial.println(rightVal);
}
