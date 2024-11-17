import serial
import pyautogui
import time



# Open serial connection to Arduino (make sure to match the correct COM port)
ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with your actual COM port

  

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
    if data == "left":
        pyautogui.press('left')
        print("Pressed 'left' key!")  
    if data == "right":
        pyautogui.press('right')
        print("Pressed 'right' key!")
    if data == "up":
        pyautogui.press('up')
        print("Pressed 'up' key!")        
    if data == "down":
        pyautogui.press('down')
        print("Pressed 'down' key!")      

    #change here in pyautogui to press for many seconds