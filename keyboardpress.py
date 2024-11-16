import serial
import pyautogui

# Open serial connection to Arduino (make sure to match the correct COM port)
ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with your actual COM port

while True:
    # Wait for data from Arduino
    data = ser.readline().decode('utf-8').strip()  # Read data from the serial port
    
    if data == "F":
        # Simulate pressing the "A" key
        pyautogui.press('F')
        print("Pressed 'F' key!")