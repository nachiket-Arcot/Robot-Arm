#include <Servo.h>
#define SERVO_NUM 4

//Declarations

//Gripper Servo done seperately since max angle should be 60
Servo ServoGripper;

//Servos and Servo Pins array
Servo Servos[SERVO_NUM];
int servoPins[SERVO_NUM] = {10, 9, 6, 5};

//Declaring Potentiometers
int potvalGripper;
int potvals[SERVO_NUM];
int potpins[SERVO_NUM] = {5, 4, 3, 2};

//Declaring Angle Values
int angleGripper;
int angles[SERVO_NUM];

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
