/***************************************************************************************
Arduino Code:
This code will read the data from the python interface and turn the servos accordingly
***************************************************************************************/

#include <Servo.h>
#define SERVO_NUM 4


//Arrays for the Servos
Servo Joints[SERVO_NUM];
int Servo_Pins[SERVO_NUM] = {11, 10, 9 , 6};

//Same Variables for the gripper Servo
Servo Gripper_Servo;
int Gripper_Pin = 3;

//Received data
String data;
int commaIndex;

//Variables and arrays for the data received from the python file
int slider_num;
int slider_val;

//Data taken from Python GUI

void setup() {

  //Establishing Serial Connection to Python Based GUI
  Serial.begin(115200);
  Serial.setTimeout(10);
  setup_servo();
  init_servo();


}

void loop() {

  receive_data();
  write_servos();
}



/****************
UDF Definitions
****************/

//Attaching Servo Joints to their respective pins
void setup_servo(){

  for (int i = 0; i < SERVO_NUM; i++){

    Joints[i].attach(Servo_Pins[i]);
  }
  Gripper_Servo.attach(Gripper_Pin);
}

//Initializing all Servos to 0 degrees
void init_servo(){

  for (int i = 0; i < SERVO_NUM; i++){

    Joints[i].write(0);
  }
  Gripper_Servo.write(0);
}


//Function to read the data from the Python GUI
void receive_data(){

  if (Serial.available()){
    
    data = Serial.readStringUntil("\n");
    commaIndex = data.indexOf(",");

    slider_num = data.substring(0, commaIndex).toInt();
    slider_val = data.substring(commaIndex + 1).toInt();
  }
   
}


//Function to Rotate the servos according to the input from the GUI
void write_servos(){

  if (slider_num == 6){

    if (slider_val > 60) {

      Serial.println("Gripper Servo Out of Bounds");
    }
    
    else {
    Gripper_Servo.write(slider_val);
    }
  }
  else {
    Joints[slider_num - 1].write(slider_val);
  }
}
