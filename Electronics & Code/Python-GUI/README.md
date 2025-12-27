Python GUI (Graphical User Interface) comprised of three files on the python side each for:

-Creating the interface  
-Connecting to the Arduino Microcontroller  
-A main file with the sole purpose of calling the functions created in the files aboce
  
And an Arduino Code that reads the data from the GUI and responds accordingly.

This GUI has allowed me to cut costs on unnecessary components to control the arm.  

It also provides and intuitive interface allowing simplicity when controlling, the features include:

-Dropdown menu to select to port to connect to the Arduino  
-Slider to Adjust the angle of the servo motors  
-Text Entry for if you want to adjust the servo to a specific angle  


To be able to use the Python Files you must install the customTkinter, Tkinter and PySerial Library as such:  

```
pip install customtkinter

pip install tkinter

pip install pyserial

```


Here is the Circuit Recreated on TinkerCad:  
https://www.tinkercad.com/things/eZ5IzaR9MzG-python-gui-robot-arm

WARNING: You must first load the arduino code into the microcontroller before running the Main GUI file, otherwise it could result in the port connection being refused. The Arduino must be plugged into your computer at all time for the serial connection to work.
