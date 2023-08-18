# gui_components.py
import cv2
import numpy as np
from analytics import vedio

# Global variables and other code related to GUI components from the original main.py file...
mbuttons = []
pbuttons = []
button_width = 300
button_height = 50
button_margin = 20
main_window_name = 'Main Window'
popup_window_name = 'Popup Window'
vedio_player_window = 'Video Player'
nummain=0   #camera index

# Function to create buttons in the main window
def create_main_buttons():
    mbutton_labels = []
    for i in range(9):
        mbutton_labels.append(f"Camera {i + 1}")
    x = 10
    y = 30

    for label in mbutton_labels:
        button = {'label': label, 'x': x, 'y': y}
        mbuttons.append(button)
        y += button_height + button_margin
    

    #create canvas
    window1_width = 300
    window1_height = 1050
    window1 = np.ones((window1_height, window1_width, 3), dtype=np.uint8) * 255

    # Display buttons in the main window
    for button in mbuttons:
        cv2.rectangle(window1, (button['x'], button['y']), (button['x'] + button_width, button['y'] + button_height),
                      (128, 128, 128), -1)
        cv2.putText(window1, button['label'], (button['x'] + 20, button['y'] + 35), cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (0, 0, 0), 2, cv2.LINE_AA)
        
    while True:
        cv2.imshow(main_window_name,window1)
        cv2.setMouseCallback(main_window_name, main_button_click)
         # Exit when 'Esc' key is pressed
        if cv2.waitKey(1) == 27:    
            break





# Function to create buttons in the popup window
def create_popup_buttons():
    popup_button_labels = [
                           "Fall_Detection",
                           "Object_Tracking",
                           "Tampering",
                           "Object_Detection"]
                           
    x = 10
    y = 20

    for label in popup_button_labels:
        button = {'label': label, 'x': x, 'y': y}
        pbuttons.append(button)
        y += button_height + button_margin



# Function to show the popup window
def show_popup_window(nummain):
    create_popup_buttons()
    window2_height = 900
    window2_width = 900
    popup_window = np.ones((window2_height, window2_width, 3), dtype=np.uint8) * 255

    for button in pbuttons:
        cv2.rectangle(popup_window, (button['x'], button['y']),
                      (button['x'] + button_width, button['y'] + button_height),
                      (153,153,255), -1)
        cv2.putText(popup_window, button['label'], (button['x'] + 20, button['y'] + 35), cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (0, 0, 0), 2, cv2.LINE_AA)
    
    while True:
        cv2.imshow(popup_window_name,popup_window)
        cv2.setMouseCallback(popup_window_name,popup_button_click)
         # Exit when 'Esc' key is pressed
        if cv2.waitKey(1) == 27:   
            cv2.destroyWindow(popup_window_name)            
            break

   
# Function to handle button clicks in the main window
def main_button_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global nummain
        for button in mbuttons:
            if button['x'] < x < button['x'] + button_width and button['y'] < y < button['y'] + button_height:
                str = button['label']
                nummain = int(str[-1])-1
                show_popup_window(nummain)

# Function to handle button clicks in the popup window
def popup_button_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        for button in pbuttons:
            if button['x'] < x < button['x'] + button_width and button['y'] < y < button['y'] + button_height:
                print('Button Clicked:', button['label'])
                str = button['label']
                print(nummain,str)
                vedio(nummain,str)
