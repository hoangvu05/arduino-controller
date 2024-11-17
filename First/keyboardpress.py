import serial
import pyautogui
import time



# Open serial connection to Arduino (make sure to match the correct COM port)
ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with your actual COM port

current_held_key = None 
current_held_joystick = None  

while True:
    # Wait for data from Arduino
    data = ser.readline().decode('utf-8').strip()  # Read data from the serial port
    
    """if data == "F":
        pyautogui.press('F')
        print("Pressed 'F' key!")"""
    if data == "F" and current_held_key != "F":

        if current_held_key:
            pyautogui.keyUp(current_held_key)
            print(f"Released '{current_held_key}' F.")
        
        pyautogui.keyDown('F')
        current_held_key = "F"
        print("Holding 'F' key!")
    """if data == "X":
        pyautogui.press('X')
        print("Pressed 'X' key!")"""
    
    if data == "X" and current_held_key != "X":

        if current_held_key:
            pyautogui.keyUp(current_held_key)
            print(f"Released '{current_held_key}' X.")
        
        pyautogui.keyDown('X')
        current_held_key= "X"
        print("Holding 'X' key!")
    """if data == "Z":
        pyautogui.press('Z')
        print("Pressed 'Z' key!")"""
    
    if data == "Z" and current_held_key != "Z":

        if current_held_key:
            pyautogui.keyUp(current_held_key)
            print(f"Released '{current_held_key}' Z.")
        
        pyautogui.keyDown('Z')
        current_held_key = "Z"
        print("Holding 'Z' key!")
    """if data == "D":
        pyautogui.press('D')
        print("Pressed 'D' key!")"""
    
    if data == "D" and current_held_key != "D":

        if current_held_key:
            pyautogui.keyUp(current_held_key)
            print(f"Released '{current_held_key}' D.")
        
        pyautogui.keyDown('D')
        current_held_key = "D"
        print("Holding 'D' key!")
    """if data == "C":
        pyautogui.press('C')
        print("Pressed 'C' key!") """    
    
    if data == "C" and current_held_key != "C":

        if current_held_key:
            pyautogui.keyUp(current_held_key)
            print(f"Released '{current_held_key}' C.")
        
        pyautogui.keyDown('C')
        current_held_key = "C"
        print("Holding 'C' key!")       

    if data == "left" and current_held_joystick != "left":

        if current_held_joystick:
            pyautogui.keyUp(current_held_joystick)
            print(f"Released '{current_held_joystick}' left.")
        
        pyautogui.keyDown('left')
        current_held_joystick = "left"
        print("Holding 'left' key!")

    if data == "right" and current_held_joystick != "right":
        if current_held_joystick:
            pyautogui.keyUp(current_held_joystick)
            print(f"Released '{current_held_joystick}' right.")
        
        pyautogui.keyDown('right')
        current_held_joystick = "right"
        print("Holding 'right' key!")

    if data == "up" and current_held_joystick != "up":
        if current_held_joystick:
            pyautogui.keyUp(current_held_joystick)
            print(f"Released '{current_held_joystick}' up.")
        
        pyautogui.keyDown('up')
        current_held_joystick = "up"
        print("Holding 'up' key!")       

    if data == "down" and current_held_joystick != "down":
        if current_held_joystick:
            pyautogui.keyUp(current_held_joystick)
            print(f"Released '{current_held_joystick}' down.")
        
        pyautogui.keyDown('down')
        current_held_joystick = "down"
        print("Holding 'down' key!")   

    if data == "keyboard release"and current_held_key is not None:
        pyautogui.keyUp(current_held_key)
        current_held_key = None

    if data == "joystick release"and current_held_joystick is not None:
        pyautogui.keyUp(current_held_joystick)
        current_held_joystick = None    

    if data == "" and current_held_joystick is not None:
        pyautogui.keyUp(current_held_joystick)
        print(f"Released '{current_held_joystick}' key.")
        current_held_joystick = None
    #change here in pyautogui to press for many seconds