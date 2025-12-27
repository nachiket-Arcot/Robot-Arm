'''
All Function Definitions Serial Connection Related
'''

import serial


print("Serial Connection File is running")


Arduino = 0

'''
Establishing Connection between Arduino And Python GUI
'''
def getportnum(port):

    com_port = 'COM{}'.format(port)

    try:
        print("Connecting to {}.... ".format(com_port)) 

        #Setting up the arduino
        global Arduino
        Arduino = serial.Serial(port = com_port, baudrate = 115200, timeout = 0.1)
        print("Connection to {} succesful".format(com_port))

    except serial.serialutil.SerialException as e:

        print("Connection to {} failed".format(com_port))



'''Getting value of the slider for the joint servos'''


def slider_status(slider_num, slider_var):

    slider_valint = int(slider_var.get())



    if slider_valint >= 0 and slider_valint <= 180:

        #Slider message for debugging purposes
        slider_message = "Slider Number: {}, Slider Value: {}".format(slider_num, slider_valint)

        #Sending data to arduino microcontroller
        data_send = "{},{}\n".format(slider_num, slider_valint)
        Arduino.write(data_send.encode())


    else:
        #Error message for if slider is not within bounds
        slider_message = "Slider Value for Slider {} not within limits".format(slider_num)

    #print(slider_message)




