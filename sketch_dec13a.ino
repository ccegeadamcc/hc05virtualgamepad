#include <SoftwareSerial.h>

int VRx = A0;
int VRy = A1;
int SW = 10;
int xPosition = 0;
int yPosition = 0;
int SW_state = 0;
int mapX = 0;
int mapY = 0;

SoftwareSerial _bt(8, 9);


void setup() {
  _bt.begin(9600);
    
  pinMode(VRx, INPUT);
  pinMode(VRy, INPUT);
  pinMode(SW, INPUT_PULLUP); 
  
  // put your setup code here, to run once:

}

void loop() {
  xPosition = analogRead(VRx);
  yPosition = analogRead(VRy);
  SW_state = digitalRead(SW);
  mapX = map(xPosition, 0, 1023, -512, 512);
  mapY = map(yPosition, 0, 1023, -512, 512);

  Writer(String(mapX) + "_" + String(mapY) + "_" + String(SW_state));
}

void Writer(String dat) {
   _bt.println(dat);
}
