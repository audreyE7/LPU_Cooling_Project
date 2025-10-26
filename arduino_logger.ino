// Simple dual-thermocouple logger (MAX6675) for inlet/outlet measurements.
// Hardware: Two MAX6675 boards + Type-K probes.
// NOTE: If you use MAX31855 instead, change the library and read calls accordingly.

#include "max6675.h"

// Thermocouple 1 (Inlet)
int thermoDO1  = 4;
int thermoCS1  = 5;
int thermoCLK1 = 6;

// Thermocouple 2 (Outlet)
int thermoDO2  = 7;
int thermoCS2  = 8;
int thermoCLK2 = 9;

MAX6675 tc_in(thermoCLK1, thermoCS1, thermoDO1);
MAX6675 tc_out(thermoCLK2, thermoCS2, thermoDO2);

// Optional: Hall-effect flow sensor on D2 (uncomment to use)
// volatile unsigned long pulseCount = 0;
// void ISR_flow() { pulseCount++; }

unsigned long t0;

void setup() {
  Serial.begin(9600);
  // attachInterrupt(digitalPinToInterrupt(2), ISR_flow, RISING);
  t0 = millis();
  Serial.println("time_s,T_in_C,T_out_C,deltaT_C");
}

void loop() {
  float Tin  = tc_in.readCelsius();
  float Tout = tc_out.readCelsius();
  float dT   = Tout - Tin;

  unsigned long t = (millis() - t0) / 1000UL;

  Serial.print(t); Serial.print(",");
  Serial.print(Tin, 2); Serial.print(",");
  Serial.print(Tout, 2); Serial.print(",");
  Serial.println(dT, 2);

  delay(2000);
}
