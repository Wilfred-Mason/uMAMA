//Pump 1 on the device is pump 4 here
//Pump 2 on the device is pump 3 here
//Pump 3 on the device is pump 1 here
//Pump 2 here is not active on the device
//Switch pins
const int PinPumpB1 = 14;
const int PinPumpB2 = 15;
const int PinPumpB3 = 16;
const int PinPumpB4 = 17;

//Switch states
bool PPB1CurrState;
bool PPB2CurrState;
bool PPB3CurrState;
bool PPB4CurrState;

bool PPB1NewState;
bool PPB2NewState;
bool PPB3NewState;
bool PPB4NewState;

//Motor pins
const int Pump1A1 = 3; //PWM pin
const int Pump1A2 = 4;
const int Pump2B1 = 5; //PWM pin
const int Pump2B2 = 7;
const int Pump3A1 = 6; //PWM pin
const int Pump3A2 = 8;
const int Pump4B1 = 9; //PWM pin
const int Pump4B2 = 10;

//Motor speeds (threshold for starting >100)
const int Speed1 = 150;
const int Speed2 = 150;
const int Speed3 = 150;
const int Speed4 = 120;
//Motor run time [milliseconds], adjusted to achieve the required volume delivery
const int Time1 = 3000; //uMAMA pump 
const int Time2 = 13400;//Not used
const int Time3 = 3000; //uMAMA pump
const int Time4 = 10000; //Receptacle filling pump
//Ramping Parameters
const int RampTime = 1000;
const int NumSteps = 20;
const int StepTimeLength = RampTime/NumSteps;
const int RampIntervalPWM1 = Speed1/NumSteps;
const int RampIntervalPWM2 = Speed2/NumSteps;
const int RampIntervalPWM3 = Speed3/NumSteps;
const int RampIntervalPWM4 = Speed4/NumSteps;

void setup() {
  Serial.begin(9600);
  Serial.println("Buttons must be pressed completely to activate the pumps"); 
  //Switch setup
  pinMode(PinPumpB1, INPUT_PULLUP);
  pinMode(PinPumpB2, INPUT_PULLUP);
  pinMode(PinPumpB3, INPUT_PULLUP);
  pinMode(PinPumpB4, INPUT_PULLUP);
  //Current state of buttons (pulled to HIGH)
  PPB1CurrState = digitalRead(PinPumpB1);
  PPB2CurrState = digitalRead(PinPumpB2);
  PPB3CurrState = digitalRead(PinPumpB3);
  PPB4CurrState = digitalRead(PinPumpB4);

  //Motor setup
  //Pump 1
  pinMode(Pump1A1, OUTPUT);
  pinMode(Pump1A2, OUTPUT);
  digitalWrite(Pump1A1, LOW);
  digitalWrite(Pump1A2, LOW);  
  //Pump 2
  pinMode(Pump2B1, OUTPUT);
  pinMode(Pump2B2, OUTPUT);
  digitalWrite(Pump2B1, HIGH);
  digitalWrite(Pump2B2, HIGH);  
  //Pump 3
  pinMode(Pump3A1, OUTPUT);
  pinMode(Pump3A2, OUTPUT);
  digitalWrite(Pump3A1, LOW);
  digitalWrite(Pump3A2, LOW);  
  //Pump 4
  pinMode(Pump4B1, OUTPUT);
  pinMode(Pump4B2, OUTPUT);
  digitalWrite(Pump4B1, HIGH);
  digitalWrite(Pump4B2, HIGH);
}

void loop() {
  //Read states of buttons
  PPB1NewState = digitalRead(PinPumpB1);
  PPB2NewState = digitalRead(PinPumpB2);
  PPB3NewState = digitalRead(PinPumpB3);
  PPB4NewState = digitalRead(PinPumpB4);
  //Check if buttons were pressed
  //Pump 1
  if (PPB1NewState != PPB1CurrState && PPB1NewState == LOW){
    //Button has been pressed, activate pump
    Serial.println("Button 1 Pressed: Pump 1 Activated");
    int PWMValue = 0;
    for (int i = 0; i <= NumSteps; i++){
      analogWrite(Pump1A1, PWMValue);
      digitalWrite(Pump1A2, LOW);
      PWMValue += RampIntervalPWM1;
      delay(StepTimeLength);
    }
    delay(Time1);
    digitalWrite(Pump1A1, LOW);
    digitalWrite(Pump1A2, LOW);
    Serial.println("Pump 1 Stopped");
  }
  PPB1CurrState = PPB1NewState;

  //Pump 2
  if (PPB2NewState != PPB2CurrState && PPB2NewState == LOW){
    //Button has been pressed, activate pump
    Serial.println("Button 2 Pressed: Pump 2 Activated");
    int PWMValue = 0;
    for (int i = 0; i <= NumSteps; i++){
      analogWrite(Pump2B1, PWMValue);
      digitalWrite(Pump2B2, LOW);
      PWMValue += RampIntervalPWM2;
      delay(StepTimeLength);
    }
    delay(Time2);
    digitalWrite(Pump2B1, HIGH);
    digitalWrite(Pump2B2, HIGH);
    Serial.println("Pump 2 Stopped");
  }
  PPB2CurrState = PPB2NewState;
  //Pump 3
  if (PPB3NewState != PPB3CurrState && PPB3NewState == LOW){
    //Button has been pressed, activate pump
    Serial.println("Button 3 Pressed: Pump 3 Activated");
    int PWMValue = 0;
    for (int i = 0; i <= NumSteps; i++){
      analogWrite(Pump3A1, PWMValue);
      digitalWrite(Pump3A2, LOW);
      PWMValue += RampIntervalPWM3;
      delay(StepTimeLength);
    }
    delay(Time3);
    digitalWrite(Pump3A1, LOW);
    digitalWrite(Pump3A2, LOW);
    Serial.println("Pump 3 Stopped");
  }
  PPB3CurrState = PPB3NewState;

//Pump 4
  if (PPB4NewState != PPB4CurrState && PPB4NewState == LOW){
    //Button has been pressed, activate pump
    Serial.println("Button 4 Pressed: Pump 4 Activated");
    digitalWrite(Pump4B1, HIGH);
    digitalWrite(Pump4B2, HIGH);
    int PWMValue = 0;
    for (int i = 0; i <= NumSteps; i++){
      analogWrite(Pump4B1, PWMValue);
      digitalWrite(Pump4B2, LOW);
      PWMValue += RampIntervalPWM4;
      delay(StepTimeLength);
    }
    delay(Time4);
    digitalWrite(Pump4B1, HIGH);
    digitalWrite(Pump4B2, HIGH);
    Serial.println("Pump 4 Stopped");
  }
  PPB4CurrState = PPB4NewState;

  delay(500);
}
