#include <Servo.h>
#define SERVO_NUM 4

/**********
Declaration of variables and arrays
*********/

//Gripper Servo done seperately since max angle should be 60
Servo ServoGripper;

//Servos and Servo Pins array
Servo Servos[SERVO_NUM];
int servoPins[SERVO_NUM] = {10, 9, 6, 5};
int gripperServoPin = 3;

//Declaring Potentiometers
int potvalGripper;
int potvals[SERVO_NUM];
int potpins[SERVO_NUM] = {5, 4, 3, 2};
int potGripPin = 1;

//Declaring Angle Values
int angleGripper;
int angles[SERVO_NUM];

//Setting up servos by connecting them to their respective pins
void setupServo(){
  for (int i = 0; i < SERVO_NUM; i++){
    Servos[i].attach(servoPins[i]);
    delay(15);
  }
 ServoGripper.attach(gripperServoPin);
}

/**********
Individual functions made for each tasks
*********/

//Reading potentiometer values for joints and gripper
void readPotentiometers(){
  for (int i = 0; i < SERVO_NUM; i++){
     potvals[i] = analogRead(potpins[i]);
  }
  potvalGripper = analogRead(potGripPin);
}

//Adjusts the angle based on the potentiometer values so that they match
void adjustangles(){
  for (int i = 0; i < SERVO_NUM; i++){
    angles[i] = map(potvals[i], 0, 1023, 0 ,180);
  }
   angleGripper = map(potvalGripper, 0, 1023, 0 , 60);
}

//Rotates the servos based on the angle value
void rotateServos() {
  for (int i = 0; i < SERVO_NUM; i++){
     Servos[i].write(angles[i]);
     delay(15);
    }
  ServoGripper.write(angleGripper);
  delay(15);
}

//Printing angle and potval values for debugging purposes
void debug() {
  for (int i = 0; i < SERVO_NUM; i++) {
    Serial.println(" Servo ");
    Serial.print(i + 1);
    Serial.print(" | Potval: ");
    Serial.print(potvals[i]);
    Serial.print(" | Angle: ");
    Serial.print(angles[i]);
  }
  Serial.println(" Servo Gripper");
  Serial.print(" | Potval: ");
  Serial.print(potvalGripper);
  Serial.print(" | Angle: ");
  Serial.print(angleGripper);
  Serial.println("=============================");
}

/**********
Function Calls
*********/

void setup()
{
 Serial.begin(115200); //Beginning Serial Connection
 setupServo();
}

void loop()
{
  readPotentiometers();
  adjustangles();
  rotateServos();
  debug();
}
