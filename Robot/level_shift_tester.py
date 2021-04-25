#Author: Akhil Nallacheruvu
#The purpose of this program is to test the level shifting integrated circuit that allows the sensors to work.
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
        if GPIO.input(r_line)==True:
            print("Right Line Sensor High")
        elif GPIO.input(r_obs)==True:
            print("Right Obstacle Sensor High")
        elif GPIO.input(l_line)==True:
            print("Left Line Sensor High")
        elif GPIO.input(l_obs)==True:
            print("Left Obstacle Sensor High")
        elif GPIO.input(echo)==True:
            print("Echo High")
        time.sleep(0.5)                   #Messages are printed onto screen to verify proper function and the program is given a rest time of 0.5s to prevent the Raspberry Pi from burning out.
except KeyboardInterrupt:
    GPIO.cleanup()

    
