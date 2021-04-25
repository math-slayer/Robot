#Author: Akhil Nallacheruvu
#The purpose of this program is to test the infrared sensors so that robot can navigate corners
import RPi.GPIO     #The 5V inputs from the sensors are outputted at 3.3V from the Raspberry Pi GPIO.
import time
pins=[4,17,27,22,21]  #GPIO pins being used
r_line=4             #Right Line Sensor is placed at GPIO pin 4
r_obs=17             #Right Obstacle Sensor is placed at GPIO pin 17
l_line=27           #Left Line Sensor is placed at GPIO pin 27
l_obs=22             #Left Obstacle Sensor is placed at GPIO pin 22
echo=21              #Ultrasonic Echo Sensor is placed at GPIO pin 21 
GPIO.setmode(GPIO.BCM)
GPIO.setup(pins, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
try:
    while True:
        if GPIO.input(r_line)==False:
            print("Right Line Sensor Detects Black")   #The Line sensors are being programmed so that robot can only go on black lines
        elif GPIO.input(r_obs)==False:
            print("Right Obstacle Sensor Detects Object") #The obstacle sensors are programmed to avoid objects
        elif GPIO.input(l_line)==False:
            print("Left Line Sensor Detects Black")
        elif GPIO.input(l_obs)==False:
            print("Left Obstacle Sensor Detects Object")
        elif GPIO.input(echo)==True:
            print("Echo High")
        time.sleep(0.5)                   #Messages are printed onto screen to verify proper function and the program is given a rest time of 0.5s to prevent the Raspberry Pi from burning out.
except KeyboardInterrupt:
    GPIO.cleanup()

    
