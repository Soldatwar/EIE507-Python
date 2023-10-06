#include <Wire.h>

#define SLAVE_ADDRESS 0x08
int number = 0;

void setup() {
  Wire.begin(SLAVE_ADDRESS);
  Wire.onReceive(receiveData);
  Serial.begin(9600);
}

void loop() {
  delay(100);
}

void receiveData(int byteCount){
  while(Wire.available()) {
    number = Wire.read();
    if (number >= 0 && number <= 5) {
      Serial.println("Hola Arduino");
    } else if (number >= 6 && number <= 10) {
      Serial.println("Adiós Tía Pati");
    }
  }
}
