/*
  Button

  Turns on and off a light emitting diode(LED) connected to digital pin 13,
  when pressing a pushbutton attached to pin 2.

  The circuit:
  - LED attached from pin 13 to ground through 220 ohm resistor
  - pushbutton attached to pin 2 from +5V
  - 10K resistor attached to pin 2 from ground

  - Note: on most Arduinos there is already an LED on the board
    attached to pin 13.

  created 2005
  by DojoDave <http://www.0j0.org>
  modified 30 Aug 2011
  by Tom Igoe

  This example code is in the public domain.

  https://www.arduino.cc/en/Tutorial/BuiltInExamples/Button
*/

const int analogPin = A5;  // Define the pin for analog input (A1 in this case)
const int joystickX = A1;  // X-axis on pin A1
const int joystickY = A0;  // Y-axis on pin A2
int sensorValue = 0;        // Variable to store the analog reading
//const int ledPin = 13;      // LED connected to pin 13 (built-in LED on most Arduinos


void setup() {
  Serial.begin(9600);  // Start serial communication at 9600 baud

  //pinMode(ledPin, OUTPUT);
}

void loop() {
  sensorValue = analogRead(analogPin);  // Read the analog input from A1 (0-1023)
  int xValue = analogRead(joystickX);
  int yValue = analogRead(joystickY);
  // Convert the sensor value to a voltage (optional)
  //float voltage = 
  

  Serial.print("X: ");
  Serial.print(xValue);
  Serial.print("  Y: ");
  Serial.print(yValue);

  /*if (buttonState == LOW) {
    Serial.print("  Button Pressed");
  }
  
  // Move to the next line for easier reading
  Serial.println();*/

  // Print the raw sensor value and the corresponding voltage
  Serial.print("Sensor Value: ");
  Serial.println(sensorValue);
  //Serial.print(" -> Voltage: ");
  //Serial.println(voltage);
  
  if (sensorValue > 730 && sensorValue < 750){
    Serial.println("F");
  }
  else if (sensorValue > 490 && sensorValue < 510){
    Serial.println("X");
  }
  else if (sensorValue > 310 && sensorValue < 340){
    Serial.println("Z");
  }
  else if (sensorValue > 130 && sensorValue < 150){
    Serial.println("D");
  }
  else if (sensorValue >=0 && sensorValue < 10){
    Serial.println("C");
  }
  else {
    Serial.println("Keyboard release");
  }

  if (xValue > 400 && xValue < 600 && yValue > 400 && yValue<600){
    Serial.println("Joystick release");
  }
  else if (xValue < yValue && xValue < (1000-yValue)){
    Serial.println("left");
  }
  else if (xValue > yValue && xValue > (1000-yValue)){
    Serial.println("right");
  }
  else if (xValue < yValue && xValue > (1000-yValue)){
    Serial.println("up");
  }
  else {
    Serial.println("down");
  }

  /*if (sensorValue < 1000) { // Adjust this threshold if necessary
    // Button is pressed, turn on the LED
    digitalWrite(ledPin, HIGH);
    //Serial.println("Button Pressed");
  } else {
    // Button is not pressed, turn off the LED
    digitalWrite(ledPin, LOW);
  }*/
    //Serial.println("Button Release");
// Wait for 500 milliseconds before the next reading
}
