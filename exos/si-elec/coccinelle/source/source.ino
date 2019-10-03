#include <Servo.h>

// définition des variables
Servo servo1;
int sensorPin = A0;
int sensorVal = 0;
int servo1Pin = 9;
int servo1Val = 0;

void setup() {
    Serial.begin(9600);
    servo1.attach(servo1Pin);
}

void loop() {
    sensorVal = analogRead(sensorPin);
    Serial.print("sensorVal = ");
    Serial.println(sensorVal);

    if (sensorVal < 400) {
        servo1.write(random(181));
    }
    delay(200);
}