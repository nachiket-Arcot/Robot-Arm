'''
All Function Definitions GUI Related
'''

import customtkinter
from tkinter import *
from Serial_Connection import *


print("GUI File is running")


'''Defining slider'''
def servoslider(screen, angle, slider_num, orientation):

    #Variables recording value of slider
    slider_value = IntVar()

    #Merging text entry and slider values together forming into just one list
    #Defining Slider
    slider = customtkinter.CTkSlider(screen, from_= 0, 
                                     to = angle, variable = slider_value, orientation = orientation, 
                                    command = lambda value: slider_status(slider_num + 1, slider_value))

    return slider, slider_value



'''Defining Labels on slider'''
def servosliderlabels(slider, screen, angle, slider_value):

    #Title of slider
    if slider == 5:
        servotext = "Gripper Servo:"
    else:
        servotext = "Servo {}:".format(slider + 1)

    servolabel = customtkinter.CTkLabel(screen, text = servotext)

    #Adding Limit Text on each side of slider
    limit_text_high = "{}".format(angle)
    limitlabel_low = customtkinter.CTkLabel(screen, text = "0")
    limitlabel_high = customtkinter.CTkLabel(screen, text = limit_text_high)

    #Displaying Slider Value on Screen
    slider_value_label = customtkinter.CTkLabel(screen, textvariable = slider_value)


    return servolabel, limitlabel_low, limitlabel_high, slider_value_label


'''Defining Angle Input for servo in text entry box'''
def servo_entry(screen, slider_num):

    #Variable representing text entry input
    input_value = StringVar(value = "0")

    #Definining text entry for angle
    servo_entry = customtkinter.CTkEntry(screen, textvariable = input_value, width = 50)
    servo_entry.bind("<Return>", lambda value: slider_status(slider_num + 1, input_value))


    return servo_entry, input_value




'''Updating Slider to the inputted value in the text entry'''
def update_slider(input_list, servo_list, slider):

    try:

        val = float(input_list[slider].get()) #Getting Entry Value input
        if 0 <= val <= 180:
            servo_list[slider].set(val) #Setting slider to the entry value

    except ValueError:
        pass



'''Recording Entry Value '''
def update_entry(slider_vars, input_list, slider):
    val = slider_vars[slider].get()
    input_list[slider].set(str(int(val)))


'''Dropdown Menu to select Port for connection'''
def port_combobox(available_ports, screen):

    combobox_var = customtkinter.StringVar(value = "1")

    combobox = customtkinter.CTkComboBox(screen, values = available_ports, variable = combobox_var, 
                                         command = getportnum)
    
    COM_Label = customtkinter.CTkLabel(screen, text = "COM: ", font = ("Roboto", 20))

    return combobox, COM_Label







