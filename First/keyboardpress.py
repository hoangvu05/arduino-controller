import serial
import pyautogui
import time



# Open serial connection to Arduino (make sure to match the correct COM port)
ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with your actual COM port

currently_held_key = None  

while True:
    # Wait for data from Arduino
    data = ser.readline().decode('utf-8').strip()  # Read data from the serial port
    
    if data == "F":
        pyautogui.press('F')
        print("Pressed 'F' key!")
    if data == "X":
        pyautogui.press('X')
        print("Pressed 'X' key!")
    if data == "Z":
        pyautogui.press('Z')
        print("Pressed 'Z' key!")
    if data == "D":
        pyautogui.press('D')
        print("Pressed 'D' key!")
    if data == "C":
        pyautogui.press('C')
        print("Pressed 'C' key!")                
    if data == "left" and currently_held_key != "left":

        if currently_held_key:
            pyautogui.keyUp(currently_held_key)
            print(f"Released '{currently_held_key}' left.")
        
        pyautogui.keyDown('left')
        currently_held_key = "left"
        print("Holding 'left' key!")

    if data == "right" and currently_held_key != "right":
        if currently_held_key:
            pyautogui.keyUp(currently_held_key)
            print(f"Released '{currently_held_key}' right.")
        
        pyautogui.keyDown('right')
        currently_held_key = "right"
        print("Holding 'right' key!")
    if data == "up" and currently_held_key != "up":
        if currently_held_key:
            pyautogui.keyUp(currently_held_key)
            print(f"Released '{currently_held_key}' up.")
        
        pyautogui.keyDown('up')
        currently_held_key = "up"
        print("Holding 'up' key!")       
    if data == "down" and currently_held_key != "down":
        if currently_held_key:
            pyautogui.keyUp(currently_held_key)
            print(f"Released '{currently_held_key}' down.")
        
        pyautogui.keyDown('down')
        currently_held_key = "down"
        print("Holding 'down' key!")   
    if data == "joystick release"and currently_held_key is not None:
        pyautogui.keyUp(currently_held_key)
        currently_held_key = None
    if data == "" and currently_held_key is not None:
        pyautogui.keyUp(currently_held_key)
        print(f"Released '{currently_held_key}' key.")
        currently_held_key = None
    #change here in pyautogui to press for many seconds