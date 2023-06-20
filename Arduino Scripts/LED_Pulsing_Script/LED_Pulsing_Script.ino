//Script to pulse LED whenever a command is send via serial from the "uMAMA_full_serial.py" python script
//Script partially based on the "PhysicalPixel" example

//H-Bridge Control Pins
const int IN_A = 6; //PWM Pin
const int IN_B = 5; //PWM Pin
const int LED_Brightness = 80; //Brightness of the LED (MAX = 255)

int incomingByte;

void setup() {
  pinMode(IN_A, OUTPUT);
  pinMode(IN_B, OUTPUT);
  //Initialize state of the pins
  //Try HIGH/HIGH if the LED is always ON
  digitalWrite(IN_A, LOW);
  digitalWrite(IN_B, LOW);
  //Begin serial communication [MAY HAVE TO CHANGE]
  Serial.begin(9600);
}

void loop() {
   if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();
    if (incomingByte == 'H') { //"H" command turns on the LED
      analogWrite(IN_A, LED_Brightness);
      digitalWrite(IN_B, LOW);
    }
    if (incomingByte == 'L') { //"L" command turns of the LED
      digitalWrite(IN_A, LOW);
      digitalWrite(IN_B, LOW);
    }
  }
  delay(100);
}
