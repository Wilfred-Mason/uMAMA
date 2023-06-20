#include <OneWire.h>  //For temperature measurement
#include <Encoder.h> //Encoder library
#include <PID_v1.h> //PID Library
#include <DallasTemperature.h> //For temperature calibration

//Pins for the encoder
const int PinSW = 2; //interrupt pin
const int PinCLK = 3; //interrupt pin
const int PinDT = 4; // not an interrupt pin

//Variables for the encoder operation
volatile bool ClickDetected = LOW; //contained within the ISR loop
int OldPosition; //Keeps track of the encoder position
int NewPosition; //Update for the encoder position

//Pins for the stepper
const int PinDir = 5;
const int PinStep = 6;

//Variables for the stepper operation
const int NumSteps = 2;
const int StepperSpeed = 15000;

//Define the encoder
Encoder UserEncoder(PinCLK, PinDT);

//Variables and operation for the temperature measurement and switch
bool TempSwitchState;
const int PinTempSW = 7; //Temperature control switch (ON-initiates control loop)
const int PinTempWire = 8; //Temperature measurement wire
const int PinTempControl = 10; //PWM pin, controls the cartridge heater
const int DesiredTemp = 40; //In degrees celsius ***Change if required***
OneWire oneWire(PinTempWire);
DallasTemperature sensors(&oneWire);

//Define the PID controller
double SetpointTemp, InputTemp, OutputPWM;
double Kp = 1; //Adjust
double Ki = 1; //Adjust
double Kd = 1; //Adjust
const int PWMMin = 0; //Lower limit of PWM
const int PWMMax = 20; //Upper-limit of PWM
PID UserPID(&InputTemp, &OutputPWM, &SetpointTemp, Kp, Ki, Kd, DIRECT);

void setup() {
  Serial.begin(9600); //for the serial plotter

  //Encoder setup
  pinMode(PinSW, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(PinSW), ClickDetection, FALLING);

  //Temperature switch setup
  pinMode(PinTempSW, INPUT_PULLUP);
  
  //Stepper setup
  pinMode(PinDir, OUTPUT);
  pinMode(PinStep, OUTPUT);
  digitalWrite(PinDir, LOW);
  digitalWrite(PinStep, LOW);
  OldPosition = 0;
  UserEncoder.write(OldPosition);
  
  //Temperature measurement setup
  sensors.begin();
  sensors.requestTemperatures(); 
  InputTemp = sensors.getTempCByIndex(0);

  //PID controller setup
  pinMode(PinTempControl, OUTPUT);
  SetpointTemp = DesiredTemp;
  UserPID.SetMode(AUTOMATIC);
  UserPID.SetOutputLimits(PWMMin, PWMMax);
}

void loop() {
//Stepper operation
  if (ClickDetected){ //only rotates the stepper if it has been "unlocked" by the click
    NewPosition = UserEncoder.read();
    if (NewPosition > OldPosition){ //CW
      digitalWrite(PinDir, HIGH); //Set the direction "CW"
      for(int x = 0; x < NumSteps; x++){
        digitalWrite(PinStep, HIGH);
        delayMicroseconds(StepperSpeed);
        digitalWrite(PinStep, LOW);
        delayMicroseconds(StepperSpeed);
      }
      OldPosition = NewPosition;
    }
    else if(NewPosition < OldPosition){
      digitalWrite(PinDir, LOW); //Set the direction "CW"
      for(int x = 0; x < NumSteps; x++){
        digitalWrite(PinStep, HIGH);
        delayMicroseconds(StepperSpeed);
        digitalWrite(PinStep, LOW);
        delayMicroseconds(StepperSpeed);
      }
      OldPosition = NewPosition;        
    }     
  }

//Temperature control loop
  TempSwitchState = digitalRead(PinTempSW);
  if (!TempSwitchState){ //Switch if 'off' when the signal is HIGH (pull-up), switch is 'on' when the signal is LOW (!TempSwitchState)
    sensors.requestTemperatures(); 
    InputTemp = sensors.getTempCByIndex(0); //Temperature in degrees celsius
    UserPID.Compute();
    analogWrite(PinTempControl, OutputPWM);
    Serial.println(InputTemp); //plots the current temperature
    Serial.println(OutputPWM);       
  }
  else{
    analogWrite(PinTempControl, 0); //Prevents runaway heating of the cartridge heater
  }
  delay(100);   
}

void ClickDetection() {
  delayMicroseconds(10);
  ClickDetected = !ClickDetected;
}
