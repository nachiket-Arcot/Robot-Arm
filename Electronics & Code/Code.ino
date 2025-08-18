#include <Servo.h>
#define SERVO_NUM 4

//Declaring Servos
Servo Servo1;
Servo Servo2;
Servo Servo3;
Servo Servo4;
Servo ServoGripper;

//Servos and Servo Pins array
Servo Servos[SERVO_NUM] = {Servo1, Servo2, 
                              Servo3, Servo4};
int servoPins[SERVO_NUM] = {10, 9, 6, 5};

//Declaring Potentiometer variables
int potval1 = 0;
int potval2 = 0;
int potval3 = 0;
int potval4 = 0;
int potvalGripper = 0;

//Potentiometer and Pot pins array
int potvals[SERVO_NUM] = {potval1, potval2, 
                          potval3, potval4};
int potpins[SERVO_NUM] = {5, 4, 3, 2};

//Declaring Angle Values
int angle1 = 0;
int angle2 = 0;
int angle3 = 0;
int angle4 = 0;
int angleGripper = 0;

int angles[SERVO_NUM] = {angle1, angle2, 
                         angle3, angle4};

void setup()
{
 Serial.begin(9600); //Beginning Serial Connection
 //Connecting Servos to Pin and setting servo angles to zero
  for (int i = 0; i < SERVO_NUM; i++){
    Servos[i].attach(servoPins[i]);
    Servos[i].write(0);
    delay(15);
  }
 //Setting up Gripper Servo
 //Done seperately since max angle should be 60
 ServoGripper.attach(3);
 ServoGripper.write(0);
}

void loop()
{
  for (int i = 0; i < SERVO_NUM; i++){
	 //Reading potentiometer values
     potvals[i] = analogRead(potpins[i]);
     //Adjusting potvalue to servo angle
     angles[i] = map(potvals[i], 0, 1023, 0 ,180);
     //Turning servo to given angle
     Servos[i].write(angles[i]);
     delay(15);
    }
  //Turning Servo for the Gripper
  potvalGripper = analogRead(1);
  angleGripper = map(potvalGripper, 0, 1023, 0 , 60);
  ServoGripper.write(angleGripper);
  delay(15);
}
