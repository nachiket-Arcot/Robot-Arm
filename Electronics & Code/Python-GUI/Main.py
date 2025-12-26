'''
Main File Where Functions from the other files are called and Variables are declared
'''

import customtkinter
from tkinter import *
from GUI import *
 
'''
Necessary Setup
'''

#Initializing variables
max_angle = 180
max_angle_gripper = 60
screen_size = [700, 500]
gripper_val = 5

#Making the list for available ports
available_ports = []

for ports in range(1, 11):

    available_ports.append(str(ports))



#Initializing widget positions
servo_x = screen_size[0] / 10
servo_y = screen_size[1] / 5

close_button_x = screen_size[0] / 2
open_button_x = screen_size[0] / (1000 /750)
button_y = screen_size[1] /5

dial_x = ((close_button_x + open_button_x) / 2) + 300

#Declaring servos
sliderservo_one = 0
sliderservo_two = 0
sliderservo_three = 0
sliderservo_four = 0

servo_list = [sliderservo_one, sliderservo_two, sliderservo_three, sliderservo_four]


#Declaring text entries
input_one = 0.0
input_two = 0.0
input_three = 0.0
input_four = 0.0


entry_list = [input_one, input_two, input_three, input_four]


#Empty List initialization
input_list = []
gripper_inputlist = []
slider_vars = []
gripper_slidervars = []

#arduino = Serial_Connection.Arduino

#Initializing Screen
screen = customtkinter.CTk()

#Screen Background Color
customtkinter.set_appearance_mode("dark")

#Screen Size 
size = "{}x{}".format(screen_size[0], screen_size[1])
screen.geometry(size)

screen.title("Robot Arm Control Interface")




'''
Function Calls and Other
'''

#Displaying Combobox at the top of the screen
[combobox, COM_Label] = port_combobox(available_ports, screen)
combobox.place(x = 100, y = 20)
COM_Label.place(x = 40, y = 20)


#Displaying slider and entries for each of the non base & gripper servos
for slider in range(len(servo_list)):

    
    '''Slider Related Content'''
    [servo_list[slider], slider_value] = servoslider(screen, max_angle, slider, "Horizontal")

    #Placing Slider
    servo_list[slider].place(x = servo_x, y = servo_y + slider * servo_y)


    '''Label Related Content '''
    #Extracting label variables from function
    [servolabel, limitlabel_low, limitlabel_high, slider_value_label] = servosliderlabels(slider, screen, max_angle, slider_value)

     #Placing Labels
    servolabel.place(x = servo_x, y = (servo_y - 30) + slider * servo_y)

    limitlabel_low.place(x = servo_x - 20, y = servo_y + slider * servo_y)
    limitlabel_high.place(x = servo_x + 210, y = servo_y + slider * servo_y)

    #Placing angle value
    slider_value_label.place(x = servo_x + 100, y = (servo_y + 20) + slider * servo_y)


    '''Text Entry Related Content'''
    #Extracting entry value from function
    [entry_list[slider], input_value] = servo_entry(screen, slider)


    #Placing Text Entry for Servo 
    entry_list[slider].place(x = servo_x + 150, y = (servo_y - 30) + slider * servo_y)

    slider_vars.append(slider_value)
    input_list.append(input_value)

    #Binding Text Entry to Slider
    entry_list[slider].bind("<Return>", lambda e, idx= slider : update_slider(input_list, servo_list, idx))
   



'''Gripper Slider Related Content'''

#Calling the functions
gripper_slider, gripslider_value = servoslider(screen, max_angle_gripper, gripper_val, "Vertical")
[gripperlabel, limlabgrip_low, limlabgrip_high, gripper_value_label] = servosliderlabels(gripper_val, 
                                                                                        screen, max_angle_gripper, gripslider_value)

gripper_entry, gripper_input = servo_entry(screen, gripper_val)


#Placing all the components
gripper_x = servo_x + 400
gripper_y = servo_y + 20

gripper_slider.place(x = gripper_x, y = gripper_y)
limlabgrip_low.place(x = gripper_x + 4.5, y = gripper_y + 200)
limlabgrip_high.place(x = gripper_x, y = servo_y - 10)
gripper_value_label.place(x = gripper_x + 20, y = gripper_y + 0.75 * gripper_y)
gripperlabel.place(x = gripper_x - 35, y = gripper_y - 60)
gripper_entry.place(x = gripper_x + 70, y = gripper_y - 60)

gripper_inputlist.append(gripper_input)



#Keeping Screen On Until Turned off
screen.mainloop()